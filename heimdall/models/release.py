from heimdall.models import db


class Release(db.Model):

    __tablename__ = "Releases"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("Projects.id"), nullable=False)
    revision = db.Column(db.String(32), unique=True, nullable=False)
    request_id = db.Column(db.String(36), unique=True, nullable=False)
    success = db.Column(db.Boolean, nullable=False, default=False)

    __table_args__ = (
        db.UniqueConstraint("project_id", "version", name="_project_revision_uniq"),
        {"schema": "heimdall"},
    )

    def __repr__(self):
        return f"{self.to_json()!r}"

    def to_json(self):
        return {attr.name: getattr(self, attr.name) for attr in self.__table__.columns}
