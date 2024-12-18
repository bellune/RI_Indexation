import sys
sys.path.append("../")
import Configuration.connexion as con
import json
import Configuration.config as conf
import calcul_map as mapc
import expansionRequete as exp


def get_req(data_query,bool=False):
     
   return {
        "query": {
            "multi_match" : {
                    "fields": [
                    "TEXT^3",
                    "NOTE",
                    "FIRST",
                    "SECOND",
                    "HEAD",
                    "DATELINE",
                    "BYLINE"
                    ],
                "type": "best_fields",
                "query" : data_query,
                "tie_breaker":1.0,
                "minimum_should_match": "30%",
                "auto_generate_synonyms_phrase_query" : False
            }
        }, 
       "sort": [
    {
      "_score": "desc"
    }
  ]
}


 # "fields":['FIRST','SECOND','BYLINE','TEXT','HEAD','OTE']

def search_doc(index_name, file_request, result_file, typ, run_name="Baseline", expand='N'):
    # Initialize Elasticsearch client
    es = con.tbm_connexion_elasticsearc()

    # Load queries and qrels
    with open(file_request, 'r', encoding='utf-8') as f:
        request = json.load(f)
    qrels = mapc.load_qrels()

    # Prepare result variables
    # all_retrieved_docs = []
    # all_relevant_docs = []
    result_lines = []
    i=0

    # Process each query
    for rec in request:
        # Formulate the query
        query_text = rec["title"]
        if typ != 'S':  # Add description if type is not 'S'
            query_text += " " + rec["desc"]
        
        if expand =='Y':
           reques = exp.get_reqexpand(query_text)
           query = get_req(reques, True)
        else:
           query = get_req(query_text)
           

        # Perform the search
        response = es.search(index=index_name, body=query, size=10000)
        
        # Prepare retrieved and relevant docs
        topic_id = rec["id_topic"]  # ID of the topic
        relevant_docs = list(qrels.get(topic_id, {}).keys())
        retrieved_docs = []

        for rank, hit in enumerate(response["hits"]["hits"], start=1):
            doc_id = hit["_id"]
            score = hit["_score"]
            retrieved_docs.append(doc_id)
            i+=1
            # Format for TREC_eval
            result_lines.append(f"{topic_id} Q0 {doc_id} {rank} {score} {run_name}\n")
        
        # all_retrieved_docs.append(retrieved_docs)
        # all_relevant_docs.append(relevant_docs)

    # Calculate MAP
    print(i, "docs")
    # map_score = mapc.calculate_map(all_retrieved_docs, all_relevant_docs)
    # print(f"MAP Score for {run_name}: {map_score:.4f}")

    # Write results to file
    with open(result_file, "w", encoding="utf-8") as file:
        file.writelines(result_lines)
    

    # with open("../Result/map_score.txt", "a+", encoding="utf-8") as file:
    #     file.write(f"-{typ} - MAP Score for {run_name}: {map_score:.4f}\n")

    print(f"Results saved to {result_file}")


    


#Baseline 
#short request / MAP Score for Baseline: 0.1405
#search_doc(conf.index_name_notreat,"../TREC_requete/short_request.json","../Result/baseline/short_req_result.txt", "S")


#long request
#long request / MAP Score for Baseline: 0.1646
#search_doc(conf.index_name_notreat,"../TREC_requete/long_request.json","../Result/baseline/long_req_result.txt", "L")


#baseline_pre_process 
#short request / 
#search_doc(conf.index_name_withtreat,"../TREC_requete/pre_short_request.json","../Result/pre_process/short_req_result.txt", "S", "pre_process")


#long request / 
#search_doc(conf.index_name_withtreat,"../TREC_requete/pre_long_request.json","../Result/pre_process/long_req_result.txt", "L","pre_process")


#baseline_pre_process / Amelioration
#short request / 
#search_doc(conf.index_name_withtreat,"../TREC_requete/pre_short_request.json","../Result/amelioration/BM25short_req_result.txt", "S", "Expansion_requetes_Synonyme","Y")


#long request / Amelioration
search_doc(conf.index_name_withtreat,"../TREC_requete/pre_long_request.json","../Result/amelioration/BM25long_req_result.txt", "L","Expansion_requetes_Synonyme","Y")


#############################################################

#Baseline DFR
#short request / 
#search_doc(conf.index_name_notreatdfr,"../TREC_requete/short_request.json","../Result/baseline/DFRshort_req_result.txt", "S")


#long request DFR
#long request / 
#search_doc(conf.index_name_notreatdfr,"../TREC_requete/long_request.json","../Result/baseline/DFRlong_req_result.txt", "L")


#baseline_pre_process DFR
#short request / 
#search_doc(conf.index_name_withtreatdfr,"../TREC_requete/pre_short_request.json","../Result/pre_process/DFRshort_req_result.txt", "S", "pre_process_DFR")


#long request DFR / 
#search_doc(conf.index_name_withtreatdfr,"../TREC_requete/pre_long_request.json","../Result/pre_process/DFRlong_req_result.txt", "L","pre_process_DFR")

#baseline_pre_process  
#short request / 
#search_doc(conf.index_name_withtreatdfr,"../TREC_requete/pre_short_request.json","../Result/amelioration/DFRshort_req_result.txt", "S", "Expansion_requetes_Synonyme","Y")


#long request / 
#search_doc(conf.index_name_withtreatdfr,"../TREC_requete/pre_long_request.json","../Result/amelioration/DFRlong_req_result.txt", "L","Expansion_requetes_Synonyme","Y")