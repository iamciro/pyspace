from flask import Blueprint, render_template
from .utils import get_space_launches

main = Blueprint('main', __name__, template_folder="templates")


@main.route('/')
def home():
    launches = get_space_launches()
    print(launches)
    return render_template('index.html')
