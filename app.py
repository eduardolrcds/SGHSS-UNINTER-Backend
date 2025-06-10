from flask import Flask
from flask_jwt_extended import JWTManager
from routes.pacientes import pacientes_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(pacientes_bp, url_prefix='/api/pacientes')

if __name__ == "__main__":
    app.run(debug=True)


