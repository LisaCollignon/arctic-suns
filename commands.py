import click
from flask import Blueprint
from models import User
from app import bcrypt, db

usersbp = Blueprint('users', __name__)

@usersbp.cli.command('create')
@click.argument('name', nargs=1)
@click.argument('email', nargs=1)
@click.argument('password', nargs=1)
def create(name, email, password):
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=name, email=email, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    print("Create user: {}, {}".format(name, email))