#Manuel Archer
#18/04/2024

print("Hello World")

#2-3. Personal Message: Use a variable to represent a person’s name, and 
#print a message to that person. Your message should be simple, 
#such as, “Hello Eric, would you like to learn some Python today?”




# Questa variabile contiene il nome
name: str = "Mario"
print(f"Ciao {name}, etc....")

# Questa variabile contiene il messaggio
name: str = "Mario"
message: str = (f"Ciao {name} , ti va di imparare un po di python insieme?")

print(message)




#
#2-4. Name Cases: Use a variable to represent a person’s name 
#then print that person’s name in lowercase, uppercase, and title case.

#Questa è una variabile che contiene il nome di una persona
name: str = "Mario"


#Questa è una variabile che contiene il nome minuscolo
name_lower: str = name.lower()


#Questa è una variabile che contiene il nome maiuscolo
name_upper: str = name.upper()

print(f"{name}, {name_upper()}, {name_lower()}")