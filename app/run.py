from flask import Flask
from interface.routes import routes

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
