from flask import Blueprint
from .utils import get_space_launches

main = Blueprint('main', __name__)


@main.route('/')
def home():
    launches = get_space_launches()
    print(launches)
    return '<h1>This is the home page</h1>'
