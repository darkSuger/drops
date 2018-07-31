txt = open('filter.txt', 'r')
str_s = txt.read()
str_s = str_s.replace('，', '')
test = str_s.split()
print(test)
talk = input()
for i in test:
    if i in talk:
        talk = talk.replace(i, "**")
print(talk)
