# NOMBRE (Carranco, Ignacio): 

import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

def download_pubmed (VIRUELA):
    """
    Funcion que pide como input la palabra de busqueda en tipo str del pubmed y como output guarda un documento con extensión
    txt que contiene los datos de la busqueda y se hace un llamado de librería data de pubmed importando desde biopython para 
    el gen HPV18I1 (CANCERHPV) perteneciente al Herpex virus en humanos:
    El code `efetch` Recupera registros en el formato solicitado de una lista
    """ 

    Entrez.email = "ignacio.carranco@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term="VIRUELA",
                        usehistory="y")
    record = Entrez.read(handle)

    
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text", 
                       retstart=0,
                       retmax=543, 
                       webenv=webenv,
                       query_key=query_key)

    out_handle = open("VIRUELA_pub.txt", "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    
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
    
    with open("data/VIRUELA_pub.txt", errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    unique_countries = list(set(countries_1))
    conteo=Counter(countries_1)
    resultado={} 
    for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ordenar = (sorted(resultado.values()))
    ordenar.sort(reverse=True) 
    import operator
    pais = [] 
    contador = []
    reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        pais.append(name[1][0])
        contador.append(resultado[name[1][0]])
    cinco_paises = pais[0:5] 
    frecuencia_cinco = contador [0:5]  
    fig = plt.figure(figsize =(10, 7))
    plt.pie(frecuencia_cinco, labels = cinco_paises)
    (plt.savefig("img/VIRUELA.jpg", dpi=100, bbox_inches='tight'))
    plt.show()
    return (count_pais)
    
    
    
    
    
    
    
    
    
    
    
 

    