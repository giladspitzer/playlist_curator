
class Config:
    SECRET_KEY = 'gilad'
    SQLALCHEMY_DATABASE_URI="sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SPOTIFY_API_KEY = '***REMOVED***'
    SPOTIFY_API_SECRET = '***REMOVED***'
    TEMPLATE_FOLDER = '../frontend/dist'
