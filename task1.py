from this import s
from datetime import datetime


# print(date)
# print(date)
s = s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

text_this = "".join([d.get(c, c) for c in s])
#print(text_this)
date = str(datetime.now())
# with open("Tekstas.txt", 'w') as file:
#     file.write(text_this)


# with open("Tekstas.txt", 'a') as file:
#     file.write(f"\n{date}\n")

# with open("Tekstas.txt", 'r') as file:
#     i = 1
#     for row in file:
#         with open("Tekstas_4.txt", 'a') as file:
#             file.write(f"{i} - {row}")
#             i += 1

with open("Tekstas.txt", 'r') as file:
    filer = file.read()
print(filer[::-1])

uppers = 0
lowers = 0
for i in filer:
    if i.isupper():
        uppers +=1
    elif i.islower():
        lowers +=1
print(uppers, lowers)
# tekstas_5 = filer.replace("Beautiful is better than ugly", "Gražu yra geriau nei bjauru.")
# print(tekstas_5)
# with open("Tekstas_5.txt", 'w', encoding="utf-8") as file:
#     file.write(tekstas_5)
with open("Tekstas_8.txt", 'w') as file:
    file.write(filer.upper())


