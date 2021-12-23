
class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI="sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SPOTIFY_API_KEY = os.environ['SPOTIFY_API_KEY']
    SPOTIFY_API_SECRET = os.environ['SPOTIFY_API_SECRET']
    TEMPLATE_FOLDER = '../frontend/dist'
    CORS_ALLOW_HEADERS = '*'
    CORS_ORIGINS = '*'
