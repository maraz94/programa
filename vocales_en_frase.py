
frase_del_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]

vocales_en_frase =[]
n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales +=1

    else:
        n_consonantes +=1

print("las vocales son {}".format(n_vocales))
print("las consonantes son {}".format(n_consonantes))
print(vocales_en_frase)