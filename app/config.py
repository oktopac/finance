import os
# Flask Config
UPLOAD_FOLDER = '/Users/chrisfuller/Dropbox/Programs/finance_v2/finance/data/uploads/'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = True


#Mongo Finance Config
MONGO_PORT = 27017
MONGO_DBNAME = 'finance'
MONGO_HOST = os.environ['DB_PORT_27017_TCP_ADDR']

#Mongo Config
MONGO2_PORT = 27017
MONGO2_DBNAME = 'config'
MONGO_HOST = os.environ['DB_PORT_27017_TCP_ADDR']
