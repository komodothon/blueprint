from app import create_app, db, bcrypt
from app.models import User, Post
from datetime import datetime, timedelta
from random import randint

def main():
    app = create_app()

    with app.app_context():
        db.create_all()

        add_sample_users()
        add_sample_posts()

        db.session.commit()

def add_sample_users():
    for i in range(1,10):
        username = f'user{i}'
        email = f'user{i}@sample.com'
        password = bcrypt.generate_password_hash(f'Hello{i}').decode("utf-8")

        user = User(username=username, email=email, password=password)
        db.session.add(user)


def add_sample_posts():
    for i in range(1,25):
        title = f'title{i}'
        content = f'content{i}'

        random_days = randint(3,12)

        date = datetime.now() + timedelta(days=random_days)

        user_id = randint(1,9)

        post = Post(title=title, content=content, date=date, user_id=user_id)

        db.session.add(post)



if __name__ == "__main__":
    main()