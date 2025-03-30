from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True)
    pd = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.String, primary_key=True)
    time = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    uid = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='posts')

    def __repr__(self):
        return f'<Post {self.id}>'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.String, primary_key=True)
    time = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    belong = db.Column(db.String, db.ForeignKey('post.id'), nullable=False)
    uid = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    post = db.relationship('Post', backref='comments')
    user = db.relationship('User', backref='comments')

    def __repr__(self):
        return f'<Comment {self.id}>'

class FavoritePost(db.Model):
    __tablename__ = 'favorite_post'
    pid = db.Column(db.String, db.ForeignKey('post.id'), primary_key=True)
    uid = db.Column(db.String, db.ForeignKey('user.id'), primary_key=True)

    post = db.relationship('Post', backref='favorites')
    user = db.relationship('User', backref='favorites')

    def __repr__(self):
        return f'<FavoritePost {self.pid} by {self.uid}>'