out = {'twords': [{'optmap': {'অ': ['অ'], 'আ': ['আ']}, 'word': True, 'options': ['অ', 'এ', 'আ']}], 'itrans': 'অ', 'inString': 'a'}

print(type(out))
print(out)
print(out['twords'])
print((out['twords'][0]['options']))
print(type(out['twords'][0]['options']))
print(out['itrans'])

primary = out['twords'][0]['options']
second = out['itrans']

if second not in primary:
    primary.append(second)

print(primary)

