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
"""
def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        else:
            return False
print(find_element([1, 2, 3, 4, 5], 5))
"""

"""
Q2
Scrivi una funzione che calcola la media 
di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

For example:
Test 
print(rounded_average([1, 1, 2, 2]))
	
Result
2
"""

def rounded_average(numbers: list[int]) -> int:
    for num in list:
        return sum(list) / len(list)
print(rounded_average([1, 1, 2, 2]))