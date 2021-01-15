activate_env:
		venv\Scripts\activate

start:
		python main.py

install_deps:
		pip install -r requirements.txt

deploy_stage:
		gcloud app deploy --version=hello-app --no-promote

browse_app:
		gcloud app browse