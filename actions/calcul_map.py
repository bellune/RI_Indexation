import sys
sys.path.append("../")
import json
import Configuration.connexion as con
import Configuration.config as conf

# Charger les jugements de pertinence TREC
qrels_file = "../TREC_juge_pert/all_juge_pert.txt"

def load_qrels():
    qrels = {}
    with open(qrels_file, 'r') as f:
        for line in f:
            query_id, _, doc_id, relevance = line.split()
            query_id = int(query_id)
            relevance = int(relevance)
            
            if query_id not in qrels:
                qrels[query_id] = {}
            
            qrels[query_id][doc_id] = relevance
    return qrels

load_qrels()

# Calculer la précision moyenne (AP) pour une requête
def calculate_ap(retrieved_docs, relevant_docs, k=1000):
    retrieved_docs = retrieved_docs[:k]  # Limiter à 1000 documents
    relevant_set = set(relevant_docs)
    
    num_relevant = 0
    precision_sum = 0.0
    
    for i, doc_id in enumerate(retrieved_docs, start=1):  # Positions commencent à 1
        if doc_id in relevant_set:
            num_relevant += 1
            precision_sum += num_relevant / i  # Precision à cette position
    
    return precision_sum / len(relevant_docs) if relevant_docs else 0.0



# Calculer la MAP (Mean Average Precision)
def calculate_map(all_retrieved_docs, all_relevant_docs, k=1000):
    ap_list = [
        calculate_ap(retrieved, relevant, k)
        for retrieved, relevant in zip(all_retrieved_docs, all_relevant_docs)
    ]
    return sum(ap_list) / len(ap_list) if ap_list else 0.0



# Exécution des requêtes dans Elasticsearch et récupération des résultats
# def get_elasticsearch_results(query, es, index, size=1000):
#     response = es.search(index=index, body={"query": {"query_string": {"query": query}}}, size=size)
#     return [hit["_id"] for hit in response["hits"]["hits"]]

# Charger les données TREC
 # Nom du fichier qrels
#queries_file = "query.txt"  # Nom du fichier des requêtes

# Charger les jugements de pertinence TREC

