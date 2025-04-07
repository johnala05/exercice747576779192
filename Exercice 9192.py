#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

#9.2
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

odds = list(get_odds())
print(odds[2])  # Print the third value returned