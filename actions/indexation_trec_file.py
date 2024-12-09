import sys
sys.path.append("../")
import Configuration.connexion as con
import json
import Configuration.config as conf



def tbm_index_elasticsearch(index_name, file_name):
    # Connexion à Elasticsearch
    # Créer l'index s'il n'existe pas
    es = con.tbm_connexion_elasticsearc()

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    # Charger le fichier JSON
    with open(file_name, 'r', encoding='utf-8') as f:
        documents = json.load(f)
   
    # Indexer chaque document
    for doc in documents["TREC"]["DOC"]:
        es.index(index=index_name, id=doc["DOCNO"], document=doc)

    print("Indexation terminée.")
    return f"Fin Indexation : {len(documents["TREC"]["DOC"])} documents"



def tbm_index_(index_name, file_name):
    # Connexion à Elasticsearch
    # Créer l'index s'il n'existe pas
    es = con.tbm_connexion_elasticsearc()

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    # Charger le fichier JSON
    with open(file_name, 'r', encoding='utf-8') as f:
        documents = json.load(f)
   
    # Indexer chaque document
    for doc in documents["TREC"]["DOC"]:
        es.index(index=index_name, id=doc["DOCNO"], document=doc)

    print("Indexation terminée.")
    return f"Fin Indexation : {len(documents["TREC"]["DOC"])} documents"

#sans pre-traitement
#tbm_index_elasticsearch(conf.index_name_notreat, "file_trec.json")

#avec pre-traitement
print(tbm_index_elasticsearch(conf.index_name_withtreat, "../preparation/pre_file_trec.json"))
