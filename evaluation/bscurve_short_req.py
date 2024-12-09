import courbe_recall_precision as cur

run_name = "Baseline"
req = "Requete courte"
result_file = "../Result/baseline/req_short_eval_results.txt"  # Fichier contenant les résultats

cur.get_curve(result_file,req,run_name)
