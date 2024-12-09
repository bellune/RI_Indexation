import courbe_recall_precision as cur

run_name = "Baseline"
#long request
req = "Requete longue"
result_file = "../Result/baseline/req_long_eval_results.txt"  # Fichier contenant les résultats

cur.get_curve(result_file,req,run_name)
