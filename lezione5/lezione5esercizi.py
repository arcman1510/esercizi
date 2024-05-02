"""
Q1
La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.
 
TROVA L'ERRORE E CORREGGI IL CODICE



def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        return False
"""   
def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        else:
            return False
print(find_element)