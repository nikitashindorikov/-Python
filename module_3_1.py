calls = 0
def count_call():
    global calls
    calls += 1
def string_info(string):
    count_call()
    return (string.lower(), string.upper(), len(string))
def is_contains(string, list_to_search):
    count_call()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)




