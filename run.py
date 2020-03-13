import os

from src.app import create_app

# load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
  # port = os.getenv('PORT')
  # run app
  app.run()