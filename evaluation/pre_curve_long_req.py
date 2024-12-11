import courbe_recall_precision as cur

run_name = "baseline_pre_process BM25"
#long request
req = "Requete longue"
result_file = "../Result/pre_process/req_long_eval_results.txt"  # Fichier contenant les résultats

cur.get_one_curve(result_file,req,run_name)
