from models import User, Comment
from main import session

user1 = User(
    username = 'Sanil',
    email_address = 'sattarkars45@gmail.com',
    comments = [
        Comment(text = "Hello SQLAlchemy"),
        Comment(text = "Django")
    ]
)

user2 = User(
    username='Database',
    email_address='user.database.2024@gmail.com',
    comments=[
        Comment(text="Hello SQLAlchemy"),
        Comment(text="Check MongoDB")
    ]
)

user3 = User(
    username='Sanil-2.0',
    email_address='bt20ece001@iiitn.ac.in',
    comments=[
        Comment(text="Hello IIITN"),
        Comment(text="Django")
    ]
)

session.add_all([user1, user2, user3])
session.commit()