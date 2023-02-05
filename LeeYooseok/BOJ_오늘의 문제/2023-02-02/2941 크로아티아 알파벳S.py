croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()

for c in croatia_alpha:
    text = text.replace(c, '*')

print(len(text))