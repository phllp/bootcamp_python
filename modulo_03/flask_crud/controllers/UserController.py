from flask import Response, request
from models.User import User
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

def index():
  session = db.session()
  users = session.query(User).all()
  users_json = [user.serialize() for user in users]
  session.close()
  return Response(json.dumps(users_json))

def create():
  body =  request.get_json()
  session = db.session()
  
  try:
    user = User(
      name=body['name'], 
      age=body['age'],
      adress=body['adress']
    )
    session.add(user)
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    print('EXCEPTION:', e)
    session.rollback()
    return {"error": f"an error ocurred while atempting to create a new user"}
  finally:
    session.close()
  
def show(user_id):
  session = db.session()

  try:
    user = session.query(User).get(user_id)
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    print('EXCEPTION:', e)
    session.rollback()
    return {"error": f"an error ocurred while looking for the register of user: {user_id}"}
  finally:
    session.close()

def update(user_id):
  session = db.session()

  try:
    body = request.get_json()
    user = session.query(User).get(user_id)

    if body and body['name']:
      user.name = body['name']
    if body and body['age']:
      user.age = body['age']
    if body and body['adress']:
      user.adress = body['adress']

    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"error": f"error while atempting to upload data for user {user_id}: {e}"}
  finally:
    session.close()

def delete(user_id):
  session = db.session()

  try:
    user = session.query(User).get(user_id)

    session.delete(user)
 
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except:
    session.rollback()
    return {"error": f"error while atempting to delete data for user {user_id}"}
  finally:
    session.close()
