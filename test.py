from random import random
import time

rounds = 0
besttime = 1000
totaltime = 0

print('\nPress Enter when the prompt appears. The prompt will appear every 0-10 seconds. Type exit to exit.\n')
input('Press Enter to begin: ')

for i in range(1,101):
    print('\nWait for the prompt...', end='', flush=True)
    time.sleep(random()*10)
    print()
    start = time.perf_counter()
    if input("Press Enter or type exit and press enter to exit: ").upper() == 'EXIT':
        break
    timetaken = time.perf_counter()-start
    if timetaken < besttime:
        besttime = timetaken
    rounds += 1
    totaltime += timetaken
    print(f'Your time was {timetaken:.2f}')
    if i == 100:
        break

print('\n---------------------------------------------------------------------------------------------------------------------------------------------\n')
if rounds == 100:
    print('You played 100 rounds and beat the game. CONGRATULATIONS. Now go do something else.\n\n')
if rounds == 0:
    print('You played zero rounds.\n\n')
else:
    print(f'You played {rounds} rounds. Your best time was {besttime:.2f} seconds. Your average response time was {totaltime / rounds:.2f}\n\n')
