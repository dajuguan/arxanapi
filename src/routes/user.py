"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import UserResource

#对应的路由为/api/user/<string:last_name>/<string:first_name>
USER_BLUEPRINT = Blueprint('user', __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource,#在这个文件里书写相应的get，post等函数
    '/user/<string:last_name>/<string:first_name>'
)
