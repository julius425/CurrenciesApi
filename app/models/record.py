from app import db


class Record(db.Model):
    """
    Модель записи.
    Каждый пользовательский запрос оставляет в базе такую запись.  
    """
    __tablename__ = 'record'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    record_uri = db.Column(
        db.Text
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'), 
        nullable=False
    )

    users = db.relationship(
        'User', 
        lazy='select',
        backref=db.backref(
            'records', 
            lazy='dynamic'
        )
    )     

    @classmethod
    def create_record(cls, app, db, record_uri, user_id):
        """
        Метод создания записи
        """
        with app.app_context():
            record = cls(
                record_uri=record_uri,
                user_id=user_id
            )
            db.session.add(record)
            db.session.commit()

