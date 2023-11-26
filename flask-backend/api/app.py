from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.users import bp as bpusers
    from modules.patients import bp as bppatients
 
    app.register_blueprint(bpusers) 
    app.register_blueprint(bppatients) 

    return app
