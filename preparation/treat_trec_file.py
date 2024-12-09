# import os
# import re
# import json 


# def manage_trec_file(file_path, wfile_path):
# #
#     docs = []
#     with open (file_path, 'r', encoding='latin1') as file:
#         content = file.read()

#         all_doc = re.findall(r"<DOC>(.*?)</DOC>", content, re.DOTALL)

#  #parcourir le fichier afin de separer les documents   
#         for docu in all_doc:
           
#             no_docu = re.search(r"<DOCNO>(.*?)</DOCNO>",docu).group(1).strip()
#             id_file = re.search(r"<FILEID>(.*?)</FILEID>",docu, re.DOTALL).group(1)
#             text_docu = re.search(r"<TEXT>(.*?)</TEXT>",docu, re.DOTALL)
#             if text_docu:
#                   text_docu = text_docu.group(1).replace("\n"," ").strip()
#                   docs.append({"nodoc":no_docu, "idfile":id_file, "text":text_docu})

# #ecrire dans un fichier json
#     with open(wfile_path,'w', encoding='utf-8') as files:
#          json.dump(docs, files, ensure_ascii=False, indent=4 )

#     return f"Fin Extraction : {len(docs)} documents"


# print(manage_trec_file("TREC_decompress/all_in_one_file", "file_Json.json")) 



