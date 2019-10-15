from heimdall.models import db


class User(db.Model):

    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    __table_args__ = {"schema": "heimdall"}
    # __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return f"{self.to_json()!r}"

    def to_json(self):
        return {attr.name: getattr(self, attr.name) for attr in self.__table__.columns}
