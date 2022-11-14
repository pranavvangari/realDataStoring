from flask import Flask, appcontext_popped, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello world'


    from .views import views

    app.register_blueprint(views, url_prefix='/')
    

    return app

    

