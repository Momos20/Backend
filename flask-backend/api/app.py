from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.cliente import bp as bpcliente
    from modules.fabricante import bp as bpfabricante

    app.register_blueprint(bpcliente)
    app.register_blueprint(bpfabricante)

    return app