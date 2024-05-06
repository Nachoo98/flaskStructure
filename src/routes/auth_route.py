from flask import Blueprint, request, jsonify

import traceback

from utils.logger import Logger

from models.user_model import UserModel as User
from utils.security import Security
from services.auth_service import AuthService

main = Blueprint('auth_blueprint', __name__)

@main.route('/login', methods=['POST'])
async def login():
    try:
        await AuthService.login_user(request.form['username'], request.form['password'])
        return "Ok"
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})
    

@main.route('/register', methods=['POST'])
async def register():
    try:
        user = await AuthService.register_user(request.json)
        return jsonify(user)
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})