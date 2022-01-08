# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

run_streamlit_with_running_api_on_port_8000:
	streamlit run streamlit_app.py http://localhost:8000

#replace by your own app that you can create on the web interface
HEROKU_APP_NAME=toto22222

create_remote_to_heroku:
	heroku git:remote -a ${HEROKU_APP_NAME}

push_to_heroku:
	git push heroku master