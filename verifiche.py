
#Q4
#Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

#For example:
#print(prime_factors(4)) [2, 2]
"""
def prime_factors(n: int) -> list[int]:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
print(prime_factors(4))
"""

# Q1 Nel gioco del blackjack, il valore di una mano 
# è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 compresi. 
# Tuttavia, se una mano contiene un asso, 
# il valore dell'asso può essere 1 o 11, a seconda di quale 
# sia più favorevole al giocatore in quel momento. 
# Dato un elenco di valori delle carte che rappresentano 
# una mano di blackjack, scrivi una funzione 
# per determinare il valore totale della mano.

