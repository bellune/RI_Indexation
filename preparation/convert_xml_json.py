import xmltodict
import json
from xml.parsers import expat
from lxml import etree


def convert_xml_json(my_xml, my_json):

    with open (my_xml, 'r', encoding='utf-8') as file :
        contentxml = ' <TREC>'+file.read()+"</TREC>"


        # Parseur lxml pour traiter les entités HTML
    parser = etree.XMLParser(resolve_entities=True, recover=True)
    root = etree.fromstring(contentxml.encode(), parser)

# Convertir l'arbre XML en chaîne de caractères
    cleaned_xml = etree.tostring(root, encoding="unicode")

# Analyser avec xmltodict
    data_dict = xmltodict.parse(cleaned_xml)
        
        
#conversion en dict python
    #data_dict = xmltodict.parse(contentxml,disable_entities=False)
   

    #conversion dict python en JSON
    get_json = json.dumps(data_dict, indent=4,ensure_ascii=False)


    with open (my_json, 'w', encoding='utf-8') as files:
        files.write(get_json)

convert_xml_json("TREC_decompress/all_in_one_file","file_Json.json")
# Exemple d'utilisation
