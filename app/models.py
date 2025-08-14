from . import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return f"<Item {self.id}: {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "title": self.title,
            "content": self.content,
        }
