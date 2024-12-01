calls = 0

def string_info(string):
    len_ = len(string)
    str_a = string.upper()
    str_l = string.lower()
    global calls
    calls += 1
    return len_, str_a, str_l

def is_contains (string, list_to_search):
    global calls
    calls += 1
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('abobus'))
print(string_info('Beshbarmak'))
print(is_contains('Agusha', ['agusha', 'Hello']))
print(is_contains('aqua', ['aqua', 'adhafae']))
print(calls)
