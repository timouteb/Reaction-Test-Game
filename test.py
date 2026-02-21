from random import random
import time

times: list[float] = []

print('\nPress Enter when the prompt appears. The prompt will take up to ten seconds to appear. Type exit to exit.\n')
input('Press Enter to begin: ')

for i in range(1,101):
    print('\nWait for the prompt...', end='', flush=True)
    time.sleep(random()*10)
    print()
    start = time.perf_counter()
    if input("Press Enter or type exit and press enter to exit: ").upper() == 'EXIT':
        break
    timetaken = time.perf_counter()-start
    times.append(timetaken)
    print(f'Your time was {timetaken:.2f}') 
    if i == 100:
        break

print('\n---------------------------------------------------------------------------------------------------------------------------------------------\n')
if len(times) == 100:
    print('You played 100 rounds and beat the game. CONGRATULATIONS. Now go do something else.\n\n')
if len(times) == 0:
    print('You played zero rounds.\n\n')
else:
    print(f'You played {len(times)} rounds. Your best time was {min(times):.2f} seconds. Your average response time was {sum(times) / len(times):.2f}\n\n')
