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
def find_element(lst: list[int], n: int) -> bool:
    i=0
    for value in lst:
        if value == n:
            return True
        i += 1
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
"""
def rounded_average(numbers: list[int]) -> int:
    average:int = round(sum(numbers)/len(numbers))
    return average
print(rounded_average([1, 1, 2, 2]))
"""

"""
Q4
La funzione dovrebbe calcolare 
la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.
"""

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) / len(numbers)
    else:
        return len(numbers) / sum(numbers) - 1