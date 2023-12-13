from main import session
from models import User

se1 = session.query(User).filter_by(
    username='Sanil').first()

print(se1)
