# import sys
# sys.path.append("../")
# import Configuration.connexion as con
# import json
# import Configuration.config as conf
# import calcul_map as mapc
# import pandas as pd # type: ignore
# import calcul_score_tfidf as actf


# def get_req(data_query):
#     return {
#             "query": {
#                 "multi_match": {
#                 "query": data_query,
#                 "fields": ["*"]
#                 }
#             }
#         }



# def search_doctfidf(index_name, file_request, result_file, typ, run_name="Baseline"):
#     # Initialize Elasticsearch client
#     es = con.tbm_connexion_elasticsearc()

#     # Load queries and qrels
#     with open(file_request, 'r', encoding='utf-8') as f:
#         request = json.load(f)
#     qrels = mapc.load_qrels()

#     # Prepare result variables
#     all_retrieved_docs = []
#     all_relevant_docs = []
#     result_lines = []
#     documents = []

#     # Process each query
#     for rec in request:
#         # Formulate the query
#         query_text = rec["title"]
#         if typ != 'S':  # Add description if type is not 'S'
#             query_text += " " + rec["desc"]
#         query = get_req(query_text)

#         # Perform the search
#         response = es.search(index=index_name, body=query)
        
#         # Prepare retrieved and relevant docs
#         topic_id = rec["id_topic"]  # ID of the topic
#         relevant_docs = list(qrels.get(topic_id, {}).keys())
#         retrieved_docs = []
             
#         for rank, hit in enumerate(response["hits"]["hits"], start=1):
#             doc_id = hit["_id"]
#             score = hit["_score"]
#             source = hit["_source"]
#             retrieved_docs.append(doc_id)
#              # Extraire les documents retournés
#             documents.append(source)
            
#         df = pd.DataFrame(documents)
#         tfidf_df = actf.calcul_tfidf(df)
     
#         result_lines.append(format_tfidf_results(tfidf_df, topic_id, run_name))
#         # all_retrieved_docs.append(retrieved_docs)
#         # all_relevant_docs.append(relevant_docs)
#     # Charger dans un DataFrame pandas pour traitement
   
   
#     # Format for TREC_eval
       
#     # Calculate MAP
#     # map_score = mapc.calculate_map(all_retrieved_docs, all_relevant_docs)
#     # print(f"MAP Score for {run_name}: {map_score:.4f}")

#     # Write results to file
#     with open(result_file, "w", encoding="utf-8") as file:
#         file.writelines(result_lines)
    
#     # with open("../Result/map_score.txt", "a+", encoding="utf-8") as file:
#     #     file.write(f"-{typ} - MAP Score for {run_name}: {map_score:.4f}\n")

#     print(f"Results saved to {result_file}")





# def format_tfidf_results(tfidf_df, topic_id, run_name):
#     results = " "
#     doc_ids = tfidf_df.index  # Utiliser l'index comme `doc_id`

#     # Calculer les scores globaux pour chaque document (somme des scores TF-IDF)
#     tfidf_df["score"] = tfidf_df.sum(axis=1)

#     # Trier les documents par score décroissant
#     sorted_docs = tfidf_df.sort_values(by="score", ascending=False)

#     # Générer les lignes de résultat au format attendu
#     for rank, (doc_id, row) in enumerate(sorted_docs.iterrows(), start=1):
#         score = row["score"]
#         # docname = row["DOCNO"]
#         results += f"{topic_id} Q0 {doc_ids} {rank} {score:.4f} {run_name} \n"

#     return results


# #Baseline 
# #short request
# search_doctfidf(conf.index_name_notreattfidf,"../TREC_requete/short_request.json","../Result/baseline/tfidfshort_req_result.txt", "S")


# #long request
# search_doctfidf(conf.index_name_notreattfidf,"../TREC_requete/long_request.json","../Result/baseline/tfidflong_req_result.txt", "L")


# #baseline_pre_process 
# #short request
# search_doctfidf(conf.index_name_withtreattfidf,"../TREC_requete/pre_short_request.json","../Result/pre_process/tfidfshort_req_result.txt", "S", "pre_process")


# #long request
# search_doctfidf(conf.index_name_withtreattfidf,"../TREC_requete/pre_long_request.json","../Result/pre_process/tfidflong_req_result.txt", "L","pre_process")