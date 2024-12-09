import sys
sys.path.append("../")
from elasticsearch import Elasticsearch
import Configuration.connexion as con
import Configuration.config as conf
# Initialize the Elasticsearch client
es = con.tbm_connexion_elasticsearc()

# Get the document count for a specific index
index_name = conf.index_name_notreat  # Replace with your index name
try:
    response = es.count(index=index_name)
    print(f"Number of documents in '{index_name}': {response['count']}")
except Exception as e:
    print(f"Error: {e}")
