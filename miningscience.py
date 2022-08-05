# NOMBRE (apellido, nombre): 

from Bio import Entrez

Entrez.email="ignacio.carranco@est.ikiam.edu.ec"

handle=Entrez.einfo(db="genome")
record=Entrez.read(handle)

handle=Entrez.esearch(db="pubmed", term = "cancer hpv")
record=Entrez.read(handle)
print(record)



def download_pubmed(HPVCANCER): 
    """
    Se hace un llamado de librería data de pubmed importando desde biopython
    """
    
    
    return 



def mapscience(HPVCANCER): # DEBE IR EN DATA
    """
    Definimos una función la cual llamaremos más adelante
 
    """
    PUB1=PUB.txt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 

    