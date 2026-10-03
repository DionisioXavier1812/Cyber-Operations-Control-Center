import random
import time

while True:
    pressure = random.uniform(1.0, 5.0)
    temperature = random.uniform(20.0, 80.0)

    print(f"Pressure={pressure:.2f} | Temp={temperature:.2f}")

    if pressure > 4.5:
        print("[ALERTA] Pressão acima do limite operacional!")

    time.sleep(1)
