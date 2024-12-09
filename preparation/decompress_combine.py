import os
import gzip
import shutil

def decompress_file(file_path, destination_folder):
  
    if file_path.endswith(".gz"):
        # Extraire le fichier GZ (Gzip)
        output_file_path = os.path.join(destination_folder, os.path.splitext(os.path.basename(file_path))[0])
        with gzip.open(file_path, 'rb') as gz_ref:
            with open(output_file_path, 'wb') as out_file:
                shutil.copyfileobj(gz_ref, out_file)
                print(f"GZ décompressé : {file_path} -> {output_file_path}")

    else:
        print(f"Format non pris en charge : {file_path}")




def decompress_all_files(source_folder, destination_folder):
    """
    Décompresse tous les fichiers du dossier source vers le dossier de destination.
    """
    os.makedirs(destination_folder, exist_ok=True)
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        decompress_file(file_path, destination_folder)
    
    print("Tous les fichiers ont été décompressés.")




def combine_files(source_folder, destination_folder, combined_filename):
    """
    Combine tous les fichiers texte dans le dossier de destination en un seul fichier texte.
    """
    combined_file_path = os.path.join(destination_folder, combined_filename)
    
    with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
   
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Éviter d'inclure le fichier combiné lui-même
                if file == combined_filename:
                    continue
                
                # Lire et ajouter le contenu de chaque fichier
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        combined_file.write(content)
                        print(f"Ajouté au fichier combiné : {file}")
                except Exception as e:
                    print(f"Erreur de lecture pour {file}: {e}")
        

    print(f"Combinaison terminée. Fichier créé : {combined_file_path}")


# source_folder = "TREC/collection_documents/AP"
# destination_folder = "TREC_decompress"
# combined_filename = "all_in_one_file"


# source_folder = "TREC/Topics-requetes"
# destination_folder = "TREC_requete"
# combined_filename = "all_request.txt"


source_folder = "TREC/jugements_pertinence"
destination_folder = "TREC_juge_pert"
combined_filename = "all_juge_pert.txt"

# Décompression et combinaison
#decompress_all_files(source_folder, destination_folder)
#combine_files(destination_folder, combined_filename)

#pour les requetes
combine_files(source_folder, destination_folder, combined_filename)

