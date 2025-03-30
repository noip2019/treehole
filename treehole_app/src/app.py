from flask import Flask
from routes import routes as routes_bp  # Import the blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

app.register_blueprint(routes_bp)  # Register the blueprint

if __name__ == "__main__":
    app.run(debug=True)