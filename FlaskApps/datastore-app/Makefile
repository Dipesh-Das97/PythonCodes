activate_env:
		venv\Scripts\activate

start:
		python main.py

install_deps:
		pip install -r requirements.txt

deploy:
		gcloud app deploy --version=datastore-app --no-promote

browse_app:
		gcloud app browse