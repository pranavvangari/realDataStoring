from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/input', methods=['GET', 'POST'])
def input():
    return render_template("input.html")