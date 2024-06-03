from models import SessionLocal, User

# Create a new session
session = SessionLocal()

# Add a new user
new_user = User(name="Jane Doe", age=25)
session.add(new_user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
