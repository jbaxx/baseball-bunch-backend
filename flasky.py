from app import create_app
import os

config_name = os.getenv('flask_config') or 'development'

app = create_app(config_name)
