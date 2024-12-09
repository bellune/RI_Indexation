import os
import re
import json 

def manage_request_file(file_path, short_request, long_request):
    short_docs = []
    long_docs = []

    with open(file_path, 'r', encoding='latin1') as file:
        content = file.read()

        # Trouver tous les documents entre les balises <top>...</top>
        all_doc = re.findall(r"<top>(.*?)</top>", content, re.DOTALL)

        # Parcourir chaque document
        for docu in all_doc:
            # Initialiser des valeurs par défaut
            title = None
            desc = None

            # Extraire le titre
            id_topic_match = re.search(r"<num>(.*?)<", docu, re.DOTALL)
            if id_topic_match:
                id_topic = id_topic_match.group(1).replace("Number:","").replace('\n', '').strip()
                id_topic = int(id_topic)

            title_match = re.search(r"<title>(.*?)<", docu, re.DOTALL)
            if title_match:
                title = title_match.group(1).replace("Topic:","").replace('\n', '').strip()

            # Extraire la description
            desc_match = re.search(r"<desc>(.*?)<", docu, re.DOTALL)
            if desc_match:
                desc = desc_match.group(1).replace("Description:","").replace('\n', '').strip()

            # Ajouter aux listes uniquement si le titre existe
            if title:
                short_docs.append({"id_topic":id_topic,"title": title})
                long_docs.append({"id_topic":id_topic,"title": title, "desc": desc})

    # Écrire dans un fichier JSON
    with open(short_request, 'w', encoding='utf-8') as files:
        json.dump(short_docs, files, ensure_ascii=False, indent=4)

    with open(long_request, 'w', encoding='utf-8') as files2:
        json.dump(long_docs, files2, ensure_ascii=False, indent=4)

    return f"Fin Extraction : {len(short_docs)} Short documents et {len(long_docs)} Long documents"



print(manage_request_file("TREC_requete/all_request.txt", "TREC_requete/short_request.json", "TREC_requete/long_request.json")) 



