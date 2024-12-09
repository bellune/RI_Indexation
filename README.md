# RI_Indexation

-**Preparation**

ce repertoire renferme les scripts utilisés pour la preparation des documents. J'ai pu générer  les fichiers suivants :
"file_trec.json" --> la baseline
"pre_file_trec.json" --> pré-traitement (Lemmatization et stop-words)
https://drive.google.com/drive/folders/1-L6cztKN9AMcqft-kTf3nA5TW97Zdmqj?usp=share_link

-**Result**
Ce repertoire contient les resultats des 150 requetes et les fichiers générés par "trec_eval" après l'evaluation. Vous y trouverez à l'interieur le repertoire "amelioration", "baseline", "pre_process" avec les fichiers qui leurs sont associées avec les schemas de ponderation "BM25", "TF-IDF". 

-**TREC_EVAL_LATEST**
Le systeme d'evaluation des documents de la collection TREC 88-90

-**TREC-juge_pert**
ce repertoire renferme les jugements de pertinences extraites de la collection TREC. "all_juge_pert_final.txt" est le fichier utilisé dans ce projet car il ne contient pas de doublons.

-**TREC_requete**
Ce repertoire contient l'ensemble des requetes courtes et longues (non-traités et traités) au format **JSON**

-**Evaluation**
Ce repertoire contient les scripts pour générer les courbes suivant chaque experimentation..Les scripts vont récupérer les rappels et precisions dans les fichiers générer par **trec_eval**.

-**Actions**
Ce repertoire renferme les scripts pour indexer, rechercher, pre_traiter, etendre les requetes

-**Configuration**
Ce repertoire contient le script de la connexion à EleasticSearch et un fichier de configuration. 
