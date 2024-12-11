
import numpy as np

def extract_precision_recall_multiple(file_path):
    recall_levels = []
    precision_by_query = {}

    # Ouvrir le fichier contenant les résultats de trec_eval
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("iprec_at_recall_"):
                parts = line.split()
                if parts[1]=='all':
                    recall = float(parts[0].split('_')[-1])  # Niveau de rappel
                    query_id = 150  # Identifiant de la requête
                    precision = float(parts[2])  # Précision
                    
                    # Ajouter les niveaux de rappel une seule fois
                    if recall not in recall_levels:
                        recall_levels.append(recall)
                    
                    # Stocker les précisions par requête
                    if query_id not in precision_by_query:
                        precision_by_query[query_id] = []
                    precision_by_query[query_id].append(precision)
    
    return recall_levels, precision_by_query




def average_precision_at_recall(recall_levels, precision_by_query):
    # Calculer la moyenne des précisions pour chaque niveau de rappel
    precision_matrix = np.array([precision_by_query[qid] for qid in precision_by_query])
    average_precision = np.mean(precision_matrix, axis=0)
    return average_precision


