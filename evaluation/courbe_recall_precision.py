import matplotlib.pyplot as plt
import extraire_prerecal as precall
import eval_file_path as fileval
import seaborn as sns
import matplotlib.pyplot as plt



def get_curve():
    # Palette de 6 couleurs
    colors = ['r', 'g', 'b', 'c', 'm', 'y']
   
    eval_infos = fileval.path_eval  # Assurez-vous que cette variable est définie correctement
    plt.figure(figsize=(8, 6))  # Créez la figure avant de tracer les courbes

    for i, ev in enumerate(eval_infos):
        # Obtenez les données de rappel et précision
        recall_levels, precision_by_query = precall.extract_precision_recall_multiple(ev["path"])
        
        # Calculer la précision moyenne à chaque niveau de rappel
        average_precision = precall.average_precision_at_recall(recall_levels, precision_by_query)
        
        # Tracer la courbe avec une couleur unique
        plt.plot(
            recall_levels, 
            average_precision, 
            marker='o', 
            linestyle='-', 
            color=colors[i % len(colors)],  # Réutilise les couleurs si >6 courbes
            label=f'{ev["req"]} : {ev["run_name"]}'
        )

    plt.xlim(0, 1)  # L'axe X commence à 0
    plt.ylim(0, 0.75)  # Ajuster pour inclure le point zéro    
    
    # Ajoutez les titres, légendes et grille
    plt.title('Courbes Precision-Recall')
    plt.ylabel('Precision')
    plt.xlabel('Recall')
  
    plt.legend()
    plt.grid()
    
    # Affichez la figure
    plt.show()


get_curve()


def get_one_curve(result_file, req, run_name):

    recall_levels, precision_by_query = precall.extract_precision_recall_multiple(result_file)

    # Calculer la précision moyenne à chaque niveau de rappel
    average_precision = precall.average_precision_at_recall(recall_levels, precision_by_query)

    print(average_precision)
    print(recall_levels)
    
    #Tracer la courbe
    plt.figure(figsize=(8, 6))
    plt.plot(recall_levels, average_precision, marker='o', linestyle='-', color='g', label=req+' : Courbe Precision-Recall')
     # Exemple de configuration correcte
    plt.axhline(y=0, color='gray', linestyle='--')  # Ligne horizontale pour 0
    plt.axvline(x=0, color='gray', linestyle='--')  # Ligne verticale pour 0
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Courbe Precision-Recall ('+run_name+')')
    plt.legend()
    plt.grid()
    plt.show()