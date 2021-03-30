export SECRET_KEY=12345
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql+psycopg2://charity:21193@localhost/blog'

# python3 manage.py test
# # python3 manage.py db migrate -m "redo migrations"
# # python manage.py db migrate -m "Deployment"
# # python manage.py db upgrade


python manage.py server