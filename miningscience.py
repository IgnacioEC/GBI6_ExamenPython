# NOMBRE (Carranco, Ignacio): 

def download_pubmed (VIRUELA):
    """
    Funcion que pide como input la palabra de busqueda en tipo str del pubmed y como output guarda un documento con extensión
    txt que contiene los datos de la busqueda y se hace un llamado de librería data de pubmed importando desde biopython para 
    el gen HPV18I1 (CANCERHPV) perteneciente al Herpex virus en humanos:
    El code `efetch` Recupera registros en el formato solicitado de una lista
    """ 
    from Bio import Entrez
    handle = Entrez.read(Entrez.esearch(db="pubmed",
                    term="VIRUELA",
                    usehistory="y"))
    record = Entrez.read(handle)
    webenv=Entr["WebEnv"]
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key=Entr["QueryKey"]
    handle=Entrez.efetch(db="pubmed",
                     rettype='medline',
                     retmode="text",
                     retstart=0,
                     retmax=543, 
                     webenv=webenv, 
                     query_key=query_key)
    out_handle = open("data/VIRUELA_pubs.txt", "w")
    data = handle.read()
    out_handle.write(data)
    out_handle.close()
    handle.close()
   
    return id_list



    
def science_plots(VIRUELA): 
    """
    Definimos una función con la cual llamaremos los datos de la pregunta 1 yse guardará 
    como archivo de extensión .txt
    
    """
    import matplotlib.pyplot as plt
    import csv
    import re
    import pandas as pd
    from collections import Counter
    with out_handle as OH: 
        my_text = OH.read()
        if tipo == "AD": 
            text = re.sub(r" [A-Z]{1}\.","", my_text)
            text = re.sub(r"Av\.","", my_text)
            text = re.sub(r"Vic\.","", my_text)
            text = re.sub(r"Tas\.","", my_text)
            AD = text.split("AD  - ")
            n_country = []
        for i in range(len(AD)): 
            country = re.findall("\S, ([A-Za-z]*)\.", AD[i])
            if not country == []: 
                if not len(country) >= 2:  
                    if re.findall("^[A-Z]", country[0]): 
                        n_country.append(country[0])
        count=Counter(n_country)
        result = {}
        for clave in count:
            valor = count[clave]
            if valor != 1: 
                result[clave] = valor 
        count_pais = pd.DataFrame()
        count_pais["pais"] = result.keys()
        count_pais["numero de autores"] = result.values()
        return (count_pais)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

    