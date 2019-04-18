import time

for x in range(140, 0, -1):
    print("\r %d" % x, end="")
    time.sleep(1)

print("Los Librillos estan aqui!")

import winsound

duration = 400
freq = 100
winsound.Beep(freq, duration)

