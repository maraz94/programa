operacion = input("que operacion quieres realizar? (Suma / Resta / multiplicacion / division").upper()
primer_numero = int(input("primer numero"))
segundo_numero = int(input("Segundo numero"))

if operacion == "SUMA":
    resultado= primer_numero + segundo_numero

elif operacion == "RESTA":
    resultado= primer_numero - segundo_numero

elif operacion == "MULTIPLICACION":
    resultado= primer_numero * segundo_numero

elif operacion == "DIVISION":
    resultado= primer_numero / segundo_numero

print("al hacer la {} entre el numero {} y el numero {} el resultado es {}".format(operacion, primer_numero, segundo_numero, resultado))


