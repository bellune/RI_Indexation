import subprocess

# Liste des commandes
commands = [

#short request 
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/baseline/short_req_result.txt > ../Result/baseline/req_short_eval_results.txt',

#Long request
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/baseline/long_req_result.txt > ../Result/baseline/req_long_eval_results.txt',

##pre_process
#short request 
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/pre_process/short_req_result.txt > ../Result/pre_process/req_short_eval_results.txt',

#Long request
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/pre_process/long_req_result.txt > ../Result/pre_process/req_long_eval_results.txt',

##amelioration
#short request 
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/amelioration/BM25short_req_result.txt > ../Result/amelioration/BM25req_short_eval_results.txt',

#Long request
'./trec_eval -q ../TREC_juge_pert/all_juge_pert_final.txt  ../Result/amelioration/BM25long_req_result.txt > ../Result/amelioration/BM25req_long_eval_results.txt'

]

# Exécution en parallèle avec subprocess.Popen
processes = []
for command in commands:
    print(f"Exécution de la commande : {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes.append(process)

# Attente de la fin de toutes les commandes
for process in processes:
    stdout, stderr = process.communicate()
    
    # Affichage de la sortie de la commande
    print(stdout.decode())
    
    # Affichage des erreurs éventuelles
    if stderr:
        print("Erreurs :")
        print(stderr.decode())
