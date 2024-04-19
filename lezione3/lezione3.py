lista = ["manamana", "102938", "plis", "wut"]

x = max(lista)
print(lista)

y = min(lista)
print(lista)

#definiamo le variabile che useremo per calcolare l'area
#scrivo la riga di stampa dove chiamo le variabili x ed y
# il return mi serve per restituirmi le due variabili moltiplicate
#   l'unico modo per "comunicare col mondo esterno"
# posso assegnare un'altra variabile out che equivale a questa molt.
#
def area(x:float,y:float) -> float:
    print (f' x={x}, y={y}')
    #return x * y
    out = x * y
    print(f"l'area è {out}")

""""
print("bella")
x,y = (2, 3)
#print(area(x,y))
out = area(x, y)
print(out)
"""