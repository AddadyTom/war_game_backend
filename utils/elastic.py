from elasticsearch import Elasticsearch
from config import CONFIG

elastic_client = Elasticsearch(hosts=[CONFIG.ELASTIC_HOST])
