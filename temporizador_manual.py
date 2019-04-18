import time
import winsound
#1
numero_inicial = int(input("tiempo en segundos "))
print(numero_inicial)

while numero_inicial > 0:
    numero_inicial -= 1
    time.sleep(1)
    print(numero_inicial)

print("Librillos!")

