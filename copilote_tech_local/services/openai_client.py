import json
import typer
from pathlib import Path
from openai import OpenAI

def load_config():
    config_path = Path(".ctl-config.json")
    if not config_path.exists():
        typer.echo("Fichier de config .ctl-config.json introuvable.")
        raise typer.Exit(code=1)

    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        typer.echo(f"Erreur lecture config : {e}")
        raise typer.Exit(code=1)

def get_client():
    config = load_config()
    api_key = config.get("openai_api_key")

    if not api_key:
        typer.echo("Clé API manquante dans .ctl-config.json")
        raise typer.Exit(code=1)

    return OpenAI(api_key=api_key)

def ask_openai(prompt: str) -> str:
    client = get_client()

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        typer.echo(f"Erreur OpenAI : {e}")
        raise typer.Exit(code=1)
