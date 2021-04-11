from dotenv import load_dotenv

from flask import Flask

# Load .env config 
load_dotenv()


def create_app():
    app = Flask(__name__)

    from pyspace.main.routes import main

    app.register_blueprint(main)

    return app
