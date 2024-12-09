from elasticsearch import Elasticsearch
from elasticsearch.exceptions import AuthenticationException

def tbm_connexion_elasticsearc():
    es = Elasticsearch(
        ['https://localhost:9200'],
        basic_auth = ('elastic', 'sXDB*3VSFhi5VH*f4AZX'),  # Replace 'your_password' with your actual password
        ca_certs='../../elastic-stack/elasticsearch/config/certs/http_ca.crt',  # Path to your CA certificate
        verify_certs=True  # To verify the server's certificate
    )
   
    # Send a GET request to the root endpoint
    try:
        response = es.info()  # This is equivalent to the curl command
        print(response)
    except AuthenticationException as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return es
