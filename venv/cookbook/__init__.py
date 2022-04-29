from flask import jsonify, request, Flask, make_response
from .extensions import mongo
from flask_cors import CORS

config_object = 'cookbook.settings'
app = Flask (__name__)
app.config.from_object(config_object)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
mongo.init_app(app)

@app.route('/')
def index():
  user_collection = mongo.db.users
  user_collection.insert_one({'name': 'H', 'age': 17})
  response = make_response()
  return response

@app.route('/api/user', methods = ['POST'])
def addUser():
  request_data = request.get_json()
  email = request_data['email']
  clerkGeneratedId = request_data['id']
  user_collection = mongo.db.users
  user_collection.find_one_and_update({'_id' : clerkGeneratedId}, {"$set": {"email": email}}, upsert=True)
  return 'Added user to Database'