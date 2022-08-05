# NOMBRE (Carranco, Ignacio): 

def download_pubmed(HPV18I1): 
    """
    Se hace un llamado de librería data de pubmed importando desde biopython para el gen HPV18I1 
    perteneciente al Herpex virus en humanos
    """
    from Bio import Entrez

Entrez.email="ignacio.carranco@est.ikiam.edu.ec"

handle=Entrez.einfo(db="genome")
handle=Entrez.esearch(db="pubmed", term = "cancer hpv")
record=Entrez.read(handle)
handle.close()
print(rec.keys())
print(record)
    
    return 



def mapscience(HPV18I1): # DEBE IR EN DATA
    """
    Definimos una función la cual llamaremos más adelante
 
    """
     print('El número artículos para HPV18I1 es:') # Que se cargue con inserción de texto o valor que correspondea KEYWORD y XX
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 

    