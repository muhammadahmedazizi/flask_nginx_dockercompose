from app import app
import os

@app.route("/")
def index():
	# use os.getenv(key) to get environment variable 
	app_name = os.getenv("APP_NAME")

	if app_name:
		return f"Hello from {app_name} running in Docker container behind Nginx!"
	return "Hello from Flask"


