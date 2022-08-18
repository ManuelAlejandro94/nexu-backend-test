import os

import yaml

from src.nexu.web import create_application

path = os.environ.get('NEXUS_CONFIG', 'config.yml')
with open(path, mode="r", encoding='utf-8') as yaml_file:
    config = yaml.load(yaml_file)

app = create_application(config)
