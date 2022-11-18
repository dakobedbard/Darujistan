from darujistan_api.views.upload_api import api


def mount_app_blueprints(app):
    app.register_blueprint(api)