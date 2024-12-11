from nltk.corpus import wordnet

# Fonction pour obtenir les synonymes d'un terme
def get_synonyms(term, max_synonyms=7):
    synonyms = set()
    for syn in wordnet.synsets(term):
        for lemma in syn.lemmas(): 
            synonyms.add(lemma.name())  # Ajouter le synonyme
        if len(synonyms) >= max_synonyms:  # Limiter à 'max_synonyms' synonymes
            break
    return list(synonyms)[:max_synonyms]

def get_reqexpand(data_query,max_synonyms=7):

    # Ajouter les synonymes à la requête
    expanded_query_terms = []
    for word in data_query.split():
        synonyms = get_synonyms(word,max_synonyms)
        if synonyms:
            expanded_query_terms.append(f"({word} {' '.join(synonyms)})")
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