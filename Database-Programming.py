"""
SQLAlchemy is a powerful Python library that provides a full suite of ORM tools for working with relational databases.
The library allows you to write Python classes that map to database tables, making it easy to interact with the database using objects and methods instead of raw SQL queries.
This abstraction simplifies database interactions and allows developers to focus on the application logic.
"""
pip install sqlalchemy

#######################################################Defining a Database Model#######################################################
"""
In SQLAlchemy, database tables are represented as Python classes, and table columns are represented as class attributes.
To define a database model, create a Python class that inherits from sqlalchemy.ext.declarative.declarative_base. 
This base class provides useful methods and attributes for working with the database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    
#######################################################Create the connection#######################################################
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db')

####################################################Performing CRUD Operations#####################################################
"""
SQLAlchemy allows you to perform Create, Read, Update, and Delete (CRUD) operations on the database using the ORM. 
These operations are done through the Session class, which is a part of the sqlalchemy.orm module.
"""
from sqlalchemy.orm import sessionmaker

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()

# Create a new user object
new_user = User(name='John Doe', age=30, email='john.doe@example.com')

# Add the new user to the session
session.add(new_user)

# Commit the changes to the database
session.commit()

# Close the session
session.close()

#######################################################Querying Data from the Database###################################################
"""
To query data from the database, you can use the query method provided by the Session class. 
This method allows you to build queries using the ORM, which are then translated to SQL and executed on the database.
"""
# Create a new session
session = Session()

# Query all users from the database
users = session.query(User).all()

# Print the users
for user in users:
    print(user.id, user.name, user.age, user.email)

# Filter users by age
older_users = session.query(User).filter(User.age > 25).all()

# Print the older users
for user in older_users:
    print(user.id, user.name, user.age, user.email)

# Close the session
session.close()


#######################################################Updating and Deleting Records###################################################
# Create a new session
session = Session()

# Query a specific user
user = session.query(User).filter(User.id == 1).first()

# Update the user's email
user.email = 'updated.email@example.com'

# Commit the changes
session.commit()

# Close the session
session.close()

# Create a new session
session = Session()

# Query a specific user
user = session.query(User).filter(User.id == 1).first()

# Delete the user
session.delete(user)

# Commit the changes
session.commit()

# Close the session
session.close()



