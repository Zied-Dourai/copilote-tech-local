import typer

from .commands.hello import register as hello_register
from .commands.explain import register as explain_register
from .commands.commit_msg import register as commitmsg_register

app = typer.Typer(help="Copilote Technique Local - IA / Dev Tools en CLI")

# On “branche” les commandes dans la CLI
hello_register(app)
explain_register(app)
commitmsg_register(app)

def main():
    app()

if __name__ == "__main__":
    main()
