from flask import Flask
from app.interface.routes import routes

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

app = create_app()
    #app.run(debug=True)
