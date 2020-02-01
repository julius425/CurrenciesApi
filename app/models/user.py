from app import db


class User(db.Model):
    """
    Модель пользователя. 
    """

    __tablename__ = 'user'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text
    )

    password = db.Column(
        db.Text
    )

    @classmethod
    def create_sample_user(cls, app, db):
        """
        Метод создания тестового пользователя
        """
        with app.app_context():
            user = cls(
                username='sampleuser', 
                password=guard.hash_password('password')
            )
            db.session.add(user)
            db.session.commit()


    # методы для работы с flask_praetorian
    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @property
    def identity(self):
        return self.id

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()


    
