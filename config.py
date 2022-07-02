import os

class config(object):
  
  LOG_GROUP_ID = -1001696319819
  API_ID = os.environ.get("API_ID", None)
  API_HASH = os.environ.get("API_HASH", None)
  SESSION = os.environ.get("SESSION", None) 
