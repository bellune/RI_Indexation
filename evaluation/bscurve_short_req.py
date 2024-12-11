import courbe_recall_precision as cur

run_name = "Baseline BM25"
req = "Requete courte"
result_file = "../Result/baseline/req_short_eval_results.txt"  # Fichier contenant les résultats

cur.get_one_curve(result_file,req,run_name)
