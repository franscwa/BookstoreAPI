first-setup:
	python3 -m venv venv
	pip install -r requirements.txt
	echo "PORT=8080\n\nFLASK_DEBUG=1\nFLASK_APP=app.py\n\nSQLALCHEMY_TRACK_MODIFICATIONS=False\nSQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite" >> .env
	