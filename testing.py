from powerballsim import generate

goal = generate()

whitetuple = goal[0]

white = (f'{whitetuple[0]:>02} {whitetuple[1]:>02} {whitetuple[2]:>02} {whitetuple[3]:>02} {whitetuple[4]:>02} ')
pb = (f'{goal[1]:>3}')

print(f'{white} {pb}')