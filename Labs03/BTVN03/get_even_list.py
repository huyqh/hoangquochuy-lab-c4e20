from random import randint
def get_even_list(l):
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
l = []
for i in range(randint(2,6)):
    l.append(randint(-50,50))
print(l)
even_list = get_even_list(l)
print(even_list)