import json
import nltk
from nltk.corpus import stopwords
import spacy

# Télécharger les ressources nécessaires
#nltk.download('stopwords')

# Charger les stop words et le modèle spaCy
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Prétraite un texte : suppression des stop words et lemmatisation.
    """
    if not text:  # Gère None ou une chaîne vide
        return ""
    
    # Supposons que `nlp` et `stop_words` soient déjà définis
    doc = nlp(text.lower())  # Conversion en minuscule
    return " ".join([
        token.lemma_ for token in doc if token.text not in stop_words and token.is_alpha
    ])




def preprocess_json(input_file, output_file):
    """
    Prétraite un fichier JSON et écrit les résultats dans un nouveau fichier.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)  # Charger le fichier JSON

        #documents = data.get("TREC", {}).get("DOC", [])
        documents = data
        print(f"Nombre total de documents à traiter : {len(documents)}")

        # Appliquer le prétraitement à chaque document
        for i, record in enumerate(documents, start=1):
           # for field in ["BYLINE", "HEAD", "NOTE", "TEXT"]:
            for field in ["title","desc"]:
                content = record.get(field, "")
                if isinstance(content, list):  # Si le champ est une liste
                    # Filtrer les valeurs `None` et convertir en chaîne
                    content = ", ".join([str(item) for item in content if item])
                record[field] = preprocess_text(content)  # Appliquer le prétraitement

            if i % 50 == 0:  # Afficher une mise à jour tous les 100 documents
                print(f"Documents traités : {i}")

        # Écrire les données prétraitées dans un nouveau fichier JSON
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

        print(f"Prétraitement terminé. Fichier sauvegardé sous : {output_file}")

    except Exception as e:
        print(f"Erreur lors du prétraitement : {e}")



# Exemple d'utilisation
#input_file = "../preparation/file_trec.json"   # Fichier JSON d'origine
#output_file = "../preparation/pre_file_trec.json"  # Fichier JSON prétraité

input_file = "../TREC_requete/long_request.json"   # Fichier JSON d'origine
output_file = "../TREC_requete/pre_long_request.json"  # Fichier JSON prétraité

preprocess_json(input_file, output_file)



def preprocess_jsonn(input_file, output_file):
    """
    Prétraite un fichier JSON et écrit les résultats dans un nouveau fichier.
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)  # Charger le fichier JSON

    # Appliquer le prétraitement à chaque champ pertinent
    for record in data["TREC"]["DOC"]:
        if 'BYLINE' in record:  # Modifier selon le champ contenant le texte
            byline = record['BYLINE']

            if byline and isinstance(byline, list):
               byline = ", ".join(byline)

        record['BYLINE'] = preprocess_text(byline)

        
        if 'HEAD' in record:  # Modifier selon le champ contenant le texte
            head = record['HEAD']

            if head and isinstance(head, list):
                head = ", ".join(head)
            record['HEAD'] = preprocess_text(head)
    
        if 'NOTE' in record:  # Modifier selon le champ contenant le texte
            note = record['NOTE']

            if note and isinstance(note,list):
               note = ", ".join(note)
            record['NOTE'] = preprocess_text(note)

        if 'TEXT' in record:  # Modifier selon le champ contenant le texte
            text = record['TEXT']

            if text and isinstance(text, list):
                text = ", ".join(text)
            record['TEXT'] = preprocess_text(text)

    # Écrire les données prétraitées dans un nouveau fichier JSON
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

    print(f"Prétraitement terminé. Fichier sauvegardé sous : {output_file}")
