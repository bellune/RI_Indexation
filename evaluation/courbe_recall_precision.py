import matplotlib.pyplot as plt
import extraire_prerecal as precall




def get_curve(result_file, req, run_name):

    recall_levels, precision_by_query = precall.extract_precision_recall_multiple(result_file)

    # Calculer la précision moyenne à chaque niveau de rappel
    average_precision = precall.average_precision_at_recall(recall_levels, precision_by_query)


    # Tracer la courbe
    plt.figure(figsize=(8, 6))
    plt.plot(recall_levels, average_precision, marker='o', linestyle='-', color='g', label=req+' : Courbe Precision-Recall')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Courbe Precision-Recall ('+run_name+')')
    plt.legend()
    plt.grid()
    plt.show()

