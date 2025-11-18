import typer

def register(app: typer.Typer):
    @app.command()
    def hello(name: str = "dev"):
        """
        Dit bonjour à l'utilisateur.
        """
        typer.echo(f"👋 Salut {name} ! Bienvenue dans Copilote Technique Local.")
