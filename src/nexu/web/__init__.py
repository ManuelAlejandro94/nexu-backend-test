from flask import Flask
import logging.config
from src.nexu.scouts import Scouts
from pymongo import MongoClient
from src.nexu.web.services import search_brands, search_models, new_brand, new_model_brand, update_model, \
    search_model_filter


def logging_config(config):
    if config:
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.DEBUG)


def create_application(config):
    logging.debug("Creando aplicación")

    logging_config(config.get('logging'))

    app = Flask(__name__)

    mongodb_config = config.get('mongo')

    client = MongoClient(mongodb_config['host'])

    if mongodb_config['authentication'] is not None:
        auth_db = client.get_database(mongodb_config['authentication'])

        auth_db.authenticate(
            mongodb_config['user'],
            mongodb_config['pass']
        )

    database = client.get_database(mongodb_config['database'])
    collection = mongodb_config['collection']

    scouts = Scouts(
        database=database,
        collection=collection
    )

    search_brands.register_routes(app, scouts)
    search_models.register_routes(app, scouts)
    new_brand.register_routes(app, scouts)
    new_model_brand.register_routes(app, scouts)
    update_model.register_routes(app, scouts)
    search_model_filter.register_routes(app, scouts)

    return app
