from flask import Blueprint, request


api = Blueprint("upload_api", __name__)


@api.route("/")
def index():
    return "darujistan_api"


def mount_app_blueprints(app):
    app.register_blueprint(api)
