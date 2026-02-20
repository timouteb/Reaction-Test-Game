from random import random
import time

while True:
    wait = random()*10
    print(wait)
    time.sleep(wait)
    start = time.perf_counter()
    input("Press Enter")
    print(f'Your time was {time.perf_counter()-start}')
