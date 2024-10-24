# Realizando una piramide lateral con un texto

text = "Python"
x = 0

for i in text:
    x = x + 1
    print(text[0:x])
    
for i in text:
    x = x - 1
    print(text[0:x])
