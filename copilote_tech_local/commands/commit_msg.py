import subprocess
import typer
from ..services.openai_client import ask_openai


def get_git_diff() -> str:
    try:
        result = subprocess.run(
            ["git", "diff", "--staged"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        typer.echo(f"❌ Impossible de récupérer git diff : {e}")
        raise typer.Exit(code=1)


def register(app: typer.Typer):
    @app.command()
    def commit_msg():
        """
        Génère des propositions de message de commit à partir du git diff.
        """
        typer.echo("🔍 Récupération du git diff...")
        diff = get_git_diff()

        if not diff:
            typer.echo("❌ Aucun changement indexé. Fais d'abord : git add .")
            raise typer.Exit(code=1)

        typer.echo("🤖 Envoi du diff à l'IA...")

        prompt = f"""
        Voici un git diff. Génère 3 messages de commit pertinents :
        
        1. Un message en format Conventional Commits.
        2. Un message descriptif court.
        3. Un message descriptif long.
        
        Diff :
        -------
        {diff}
        -------
        """

        response = ask_openai(prompt)

        typer.echo("\n📘 Messages de commit proposés :\n")
        typer.echo(response)
