frase_del_usuario = input("Introduce una frase: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
n_mayusc = 0

for letra in frase_del_usuario:
    if letra in mayusculas:
        n_mayusc +=1

print("el numero de Mayusculas es de {}".format(n_mayusc))
