from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    jsonify,
    Blueprint,
)
from . import db
from .models import Item
import os

bp = Blueprint("routes", __name__)


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(bp.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/todos", methods=["GET"])
def get_todos():
    todos = Item.query.all()
    return jsonify([todo.to_dict() for todo in todos])


@bp.route("/api/todos", methods=["POST"])
def add_todo_api():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    if title and content:
        new_item = Item(title=title, content=content)
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    return jsonify({"error": "Title and content are required"}), 400


@bp.route("/api/todos/<int:item_id>", methods=["DELETE"])
def delete_todo_api(item_id):
    item = db.session.get(Item, item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return "", 204

    return jsonify({"error": "Item not found"}), 404
