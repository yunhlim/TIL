ch = input()

if ch.islower():
    print(f'{ch}(ASCII: {ord(ch)}) => {ch.upper()}(ASCII: {ord(ch.upper())})')
else:
    print(f'{ch}(ASCII: {ord(ch)}) => {ch.lower()}(ASCII: {ord(ch.lower())})')