import sys
sys.path.append("../")
import Configuration.connexion as con
import Configuration.config as conf

# Connexion à Elasticsearch
es = con.tbm_connexion_elasticsearc()

# Index et document à expliquer
index = conf.index_name_notreat
doc_id = "AP880709-0005"

# Récupérer l'explication
response = es.explain(index=index, id=doc_id, body={
    "query": {
        "match": {
            "query": "Dumps Grenade"
        }
    }
})

# Afficher l'explication
print(response)
