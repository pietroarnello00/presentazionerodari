#Come ti chiami?

print("Ciao! Come ti chiami?")
nome = input()
lenght_nome = len(nome)
print(" Ciao" + " " + nome + "!" +  " Il tuo nome è lungo" + " " +  str(lenght_nome) + " lettere!")

#Sei maschio o femmina?

print("Sei maschio o femmina?")
print("...digita 0 se sei maschio e 1 se sei femmina!")

sesso = ["maschio", "femmina"]
numero_sesso = int(input())
sesso_scelto = sesso[numero_sesso]
print("Oh, allora sei" + " " + sesso_scelto + "!")





