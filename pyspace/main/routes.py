from flask import Blueprint, render_template
from .utils import get_space_launches, convert_str_to_datetime

main = Blueprint('main', __name__, template_folder="templates")


@main.route('/')
def home():
    launches = get_space_launches(10)
    if launches:
        return render_template('index.html',
                               launches=launches,
                               convert_str_to_datetime=convert_str_to_datetime)
    return render_template('index.html')
