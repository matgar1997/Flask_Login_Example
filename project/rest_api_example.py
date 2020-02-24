from flask import Blueprint, jsonify 
from flask_login import login_required, current_user
import random

rest_api_example = Blueprint('rest_api_example', __name__)

@rest_api_example.route('/data')
@login_required
def profile():
    return jsonify({'name' : current_user.name, 'age' : random.randint(15, 30)})
