from pathlib import Path
import typer

def read_file(file: Path) -> str:
    if not file.exists():
        typer.echo(f"❌ Le fichier {file} n'existe pas.")
        raise typer.Exit(code=1)

    try:
        return file.read_text(encoding="utf-8")
    except Exception as e:
        typer.echo(f"❌ Erreur lecture fichier : {e}")
        raise typer.Exit(code=1)
