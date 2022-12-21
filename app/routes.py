from flask.views import MethodView
from flask import render_template, request, redirect
from app import app, db

class ItemAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model
        self.validator = generate_validator(model)

    def _get_item(self, id):
        return self.model.query.get_or_404(id)

    def get(self, id):
        user = self._get_item(id)
        return jsonify(item.to_json())

    def patch(self, id):
        item = self._get_item(id)
        errors = self.validator.validate(item, request.json)

        if errors:
            return jsonify(errors), 400

        item.update_from_json(request.json)
        db.session.commit()
        return jsonify(item.to_json())

    def delete(self, id):
        item = self._get_item(id)
        db.session.delete(item)
        db.session.commit()
        return "", 204

class GroupAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model
        self.validator = generate_validator(model, create=True)

    def get(self):
        items = self.model.query.all()
        return jsonify([item.to_json() for item in items])

    def post(self):
        errors = self.validator.validate(request.json)

        if errors:
            return jsonify(errors), 400

        db.session.add(self.model.from_json(request.json))
        db.session.commit()
        return jsonify(item.to_json())

def register_api(app, model, url):
    item = ItemAPI.as_view(f"{name}-item", model)
    group = GroupAPI.as_view(f"{name}-group", model)
    app.add_url_rule(f"/{name}/<int:id>", view_func=item)
    app.add_url_rule(f"/{name}/", view_func=group)

register_api(app, User, "users")
register_api(app, Story, "stories")