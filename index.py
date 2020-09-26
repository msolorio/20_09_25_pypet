cat = {
    'name': 'Fluffy',
    'hungry': True,
    'weight': 9.5,
    'age': 5,
    'photo': '(=^o.o^=)__',
    'health': 9,
    'asleep': False,
    'phrases': ['meowwww', 'hey you', 'tssssssssss']
}

mouse = {
    'name': 'Mouse',
    'hungry': False,
    'weight': 1.5,
    'age': 6,
    'photo': '<:3 )~~~',
    'health': 3,
    'asleep': False,
    'phrases': ['...', 'im mickey mouse', 'all aboardddddd']
}

pets = [cat, mouse]

def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print(pet['name'], ': ', 'The Pypet is not hungry')

def play(pet):
    pet['weight'] = pet['weight'] - .2
    pet['health'] = pet['health'] + 1
    pet['hungry'] = True

for pet in pets:
    feed(pet)
    print(pet)

user_input = input('Please give us your input: ')

print('Is this what you just said')
answer = input(user_input)

print(answer)
