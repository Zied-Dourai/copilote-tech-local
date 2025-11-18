\# 🚀 Copilote Tech Local  

\*\*Assistant IA en ligne de commande (CLI) pour développeurs\*\*  

Basé sur Python, Typer et l'API OpenAI.



---



\## 📌 1. Présentation



\*\*Copilote Tech Local\*\* est un outil CLI conçu pour aider les développeurs à travailler plus vite directement depuis leur terminal :



\- 🧠 \*Explain\* — Explique un fichier ou un extrait de code grâce à l’IA  

\- ✍️ \*Commit-msg\* — Génère automatiquement un message de commit intelligent à partir du `git diff`  

\- 🧪 (À venir) Génération de tests  

\- 🛠️ (À venir) Suggestions de refactor  

\- 🔍 (À venir) Analyse de tracebacks  



Ce projet a été construit comme un \*\*exemple éducatif\*\*, pour montrer comment créer un assistant IA local modulaire avec Python.



---



\## 📦 2. Installation



\### 🔧 Prérequis



\- Python \*\*3.10+\*\* (idéalement 3.12)

\- Git

\- Une clé API \*\*OpenAI\*\* (modèles `gpt-4o-mini`, `gpt-4.1`, etc.)



---



\## ⬇️ 3. Installation depuis GitHub



\### 1) Cloner le projet



```bash

git clone https://github.com/TON\_COMPTE\_GITHUB/copilote-tech-local.git

cd copilote-tech-local



\### 2) Créer et activer l’environnement virtuel

Windows PowerShell :

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1



macOS / Linux :

python3 -m venv .venv

source .venv/bin/activate



\### 3) Installer les dépendances

pip install -r requirements.txt



\### 4) Configurer la clé OpenAI



À la racine du projet, crée un fichier :

.ctl-config.json

{

&nbsp; "openai\_api\_key": "TA\_CLE\_API\_ICI"

}



\### 5) Utilisation

Après activation de ton environnement virtuel, tu peux appeler l’outil :

python -m copilote\_tech\_local --help



💬 Commandes disponibles

1\) hello

Test simple pour valider l'installation.

python -m copilote\_tech\_local hello

python -m copilote\_tech\_local hello --name "Jean"



2\) explain

Explique un fichier complet ou un extrait de lignes.

python -m copilote\_tech\_local explain chemin/fichier.py



Plage de lignes :

python -m copilote\_tech\_local explain fichier.py --start-line 10 --end-line 40



Afficher les lignes dans le terminal :

python -m copilote\_tech\_local explain fichier.py -n



Changer la langue (fr/en) :

python -m copilote\_tech\_local explain fichier.py --lang en



3\) commit-msg

Génère automatiquement des messages de commit basés sur ton git diff.



⚠️ N’oublie pas de faire :

git add .



Puis :

python -m copilote\_tech\_local commit-msg



Le copilote te proposera :

\#un message Conventional Commits

\#un message court

\#un message descriptif





📂 6. Structure du projet



copilote-tech-local/

│

├── copilote\_tech\_local/

│   ├── \_\_main\_\_.py

│   ├── \_\_init\_\_.py

│   ├── commands/

│   │   ├── hello.py

│   │   ├── explain.py

│   │   └── commit\_msg.py

│   └── services/

│       ├── file\_reader.py

│       └── openai\_client.py

│

├── .gitignore

├── .ctl-config.json (non commité)

└── README.md





🧭 7. Roadmap (améliorations prévues)

Commande tests → Génération automatique de tests unitaires

Commande refactor → Suggestions de refactor structurées

Commande debug → Analyse des tracebacks Python

Intégration OCR (explication d’images de code)

Packaging : pip install copilote-tech-local



📝 8. Licence

MIT – libre de modifier, distribuer, utiliser.



⭐ 9. Contribuer

Toute contribution est la bienvenue !

Fork → modif → PR.





