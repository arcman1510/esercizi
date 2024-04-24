
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
""""
def blackjack_hand_total(card: list[int]) -> int:
    total = 0
    aces = 0
    for card in blackjack_hand_total:
        card = str(card)
        if card == "J" or card == "Q" or card== "K":
            total+=10
            continue
        elif card == "2" or card == "3" or card == "4" or card == "5" or card == "6" or card == "7" or card == "8" or card == "9" or card == "10":
            total += int(card)
        elif card == "A":
            total += 1
            aces += 1
    for _ in range(aces):
        if total <= 11:
            total += 10
    return total
    """

#Q3
# Scrivi una funzione che accetta una stringa come input, 
# rimuove le parole non significative comuni stop_words 
# e restituisce un dizionario in cui le chiavi sono 
# parole univoche nel testo rimanente 
# (ignorando la distinzione tra maiuscole e minuscole 
# e la punteggiatura) e i valori sono le frequenze di quelle 
# parole.
#For example:

# Test
# stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
# text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
# print(word_frequency(text, stopwords))
# Result
# {'quick': 1, 'brown': 1, 'fox': 1, 
# 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}
"""
# def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:

    stopwords == [input()]
    text == input()
    for i in text:
        x = text.split()
        if i in x == stopwords:
            text.remove(i)
        else:
            text.count(i)
    """





            
        
