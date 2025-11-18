import typer
from pathlib import Path
from typing import Optional

from ..services.file_reader import read_file
from ..services.openai_client import ask_openai


def register(app: typer.Typer):
    @app.command()
    def explain(
        file: Path,
        start_line: Optional[int] = typer.Option(
            None,
            "--start-line",
            "-s",
            help="Première ligne à expliquer (1 = première ligne du fichier).",
        ),
        end_line: Optional[int] = typer.Option(
            None,
            "--end-line",
            "-e",
            help="Dernière ligne à expliquer (incluse).",
        ),
        lang: str = typer.Option(
            "fr",
            "--lang",
            "-l",
            help="Langue de l'explication (fr ou en).",
        ),
        show_lines: bool = typer.Option(
        False,
        "--show-lines",
        "-n",
        help="Affiche le code avec les numéros de lignes avant l'analyse IA.",
        ),
    ):
        """
        Explique un fichier (ou un extrait) en utilisant l'IA.
        """
        content = read_file(file)
        lines = content.splitlines()
        total_lines = len(lines)

        # Petit debug pour comprendre ce qui se passe (tu peux le laisser, c'est utile)
        typer.echo(f"ℹ Fichier : {file} ({total_lines} lignes)")
        typer.echo(f"ℹ start_line = {start_line}, end_line = {end_line}")

        # Si aucune plage, on prend tout le fichier
        if start_line is None and end_line is None:
            snippet = content
            typer.echo(f" Lecture du fichier complet : lignes 1 à {total_lines}")
        else:
            # Valeurs par défaut si une seule des deux est fournie
            if start_line is None:
                start_line = 1  # début du fichier
            if end_line is None:
                end_line = total_lines  # fin du fichier

            # Convertir en index 0-based pour le slicing Python
            start_idx = max(start_line - 1, 0)
            end_idx_exclusive = min(end_line, total_lines)

            if start_idx >= end_idx_exclusive:
                typer.echo(" Plage de lignes invalide (start_line >= end_line).")
                raise typer.Exit(code=1)

            selected_lines = lines[start_idx:end_idx_exclusive]
            snippet = "\n".join(selected_lines)

            typer.echo(
                f" Lecture d'un extrait : lignes {start_idx + 1} à {end_idx_exclusive} / {total_lines}"
            )

        # Choix de la langue
        lang = lang.lower()
        if lang == "fr":
            instruction = (
                "Explique ce code en français, de manière claire et pédagogique, "
                "comme à un développeur qui découvre ce fichier."
            )
        elif lang == "en":
            instruction = (
                "Explain this code in English, clearly and pedagogically, "
                "as if to a developer who is discovering this file."
            )
        else:
            typer.echo(" Langue non supportée. Utilise 'fr' ou 'en'.")
            raise typer.Exit(code=1)

        if show_lines:
            typer.echo("\n🔢 Aperçu du code avec numéros de lignes :\n")
            for idx, line in enumerate(snippet.splitlines(), start=start_line or 1):
                typer.echo(f"{str(idx).rjust(4)} | {line}")
            typer.echo("\n")

        prompt = f"""
{instruction}

--- DEBUT DU CODE ---
{snippet}
--- FIN DU CODE ---
"""

        typer.echo("Envoi à l'IA...")

        result = ask_openai(prompt)

        typer.echo("\n Explication générée par l'IA :\n")
        typer.echo(result)
