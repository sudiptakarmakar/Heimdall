import datetime
from heimdall.models import db


class Project(db.Model):

    __tablename__ = "Projects"

    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(255), unique=True, nullable=False)
    repository = db.Column(db.String(255), unique=True, nullable=False)
    registrar = db.Column(
        db.String(120), unique=False, nullable=True, default="unknown"
    )
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("organization", "repository", name="_org_repo_uniq"),
        {"schema": "heimdall"},
    )

    def __repr__(self):
        return f"{self.to_json()!r}"

    def to_json(self):
        return {attr.name: getattr(self, attr.name) for attr in self.__table__.columns}
