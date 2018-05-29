import random
esc=True
a = set([])
while esc:

    a.add(random.randrange(1,46))
    if len(a)==6:
        esc=False
print(a)