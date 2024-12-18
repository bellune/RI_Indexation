from nltk.corpus import wordnet
from nltk.wsd import lesk  # Algorithme Lesk pour la désambiguïsation
import spacy

nlp = spacy.load("en_core_web_sm")


def get_synonymsss(term, context=None, max_synsets=1, synset_types=['n','r']):

    
    if not isinstance(synset_types, (list, tuple)):
        raise ValueError("L'argument 'synset_types' doit être une liste ou un tuple.")
    
    if context:
        # Désambiguïsation avec Lesk
        synset = lesk(context, term, pos=None)  # Désambiguïser le terme
    else:
        # Si aucun contexte, prendre le premier synset (par défaut dans WordNet)
        synset = wordnet.synsets(term)[0] if wordnet.synsets(term) else None

    if not synset or synset.pos() not in synset_types:
        return []  # Aucun synset pertinent trouvé

    # Récupérer les synonymes pour le synset désambiguïsé
    expanded_terms = set()
    for lemma in synset.lemmas():
         
        synonym = lemma.name().replace("_", " ")  # Nettoyer le format de WordNet
        # Lemmatise le synonyme avec spaCy
        doc = nlp(synonym)
        lemmatized = " ".join([token.lemma_ for token in doc])
        expanded_terms.add(lemmatized)

        if len(expanded_terms) >= max_synsets:
            break

    return list(expanded_terms)[:max_synsets]




def get_reqexpand(data_query):

    #word = data_query
    # Ajouter les synonymes à la requête
    expanded_query_terms = []
    for word in data_query.split():
        synonyms = get_synonymsss(word, data_query.split())

        if synonyms:
            expanded_query_terms.append(f"({word} {' '.join(synonyms)}")
        else:
            expanded_query_terms.append(word)

    expanded_query = " ".join(expanded_query_terms)
   
    return expanded_query
    
    # return {
    #     "query": {
    #         "multi_match": {
    #             "query": expanded_query
    #         }
    #     }
    # }

