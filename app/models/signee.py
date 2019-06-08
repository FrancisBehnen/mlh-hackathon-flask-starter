from app.extensions import db

class Signee(db.Model):
    __tablename__ = 'signee'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    @staticmethod
    def signUp(email):
        instance = Signee(email)

        db.session.add(instance)
        db.session.commit()

        return instance

    # @staticmethod
    # def find_or_create_from_token(access_token):
    #     data = GitHub.get_user_from_token(access_token)
    #
    #     """Find existing user or create new User instance"""
    #     instance = User.query.filter_by(username=data['login']).first()
    #
    #     if not instance:
    #         instance = User(data['login'], data['avatar_url'], data['id'])
    #         db.session.add(instance)
    #         db.session.commit()
    #
    #     return instance

    def __repr__(self):
        return "<User: {}>".format(self.username)
