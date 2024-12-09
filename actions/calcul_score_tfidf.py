from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd # type: ignore



def convertlist(text):
    if text is None:  # Si l'entrée est None, retourner une chaîne vide
        return ""
    if isinstance(text, list):  # Si c'est une liste, gérer les valeurs `None`
        text = [str(item) if item is not None else "" for item in text]
        return ", ".join(text)
    return str(text)  # S'assurer que la sortie est une chaîne



def calcul_tfidf(df):
    # Vérifier que toutes les colonnes nécessaires sont présentes
    required_columns = ["DOCNO","TEXT", "DATELINE", "BYLINE", "NOTE", "HEAD", "SECOND"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = ""  # Ajouter une colonne vide si elle manque

    # Gérer les valeurs manquantes
    df.fillna("", inplace=True)

    # Fusionner les champs texte
    df["combined_text"] = (
        df["TEXT"].apply(convertlist) + " " +
        df["DATELINE"].apply(convertlist) + " " +
        df["BYLINE"].apply(convertlist) + " " +
        df["NOTE"].apply(convertlist) + " " +
        df["HEAD"].apply(convertlist) + " " +
        df["SECOND"].apply(convertlist)
    )

    # Initialiser le vectoriseur TF-IDF
    vectorizer = TfidfVectorizer()

    # Calculer le TF-IDF
    tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

    # Récupérer les mots et leurs scores TF-IDF
    features = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()

    # Créer un DataFrame des résultats
    tfidf_df = pd.DataFrame(tfidf_scores, columns=features)
    # print(tfidf_df)

    return tfidf_df
