import random
my_list = []


for i in range(20):
    losowa_liczba = random.randint(1, 100)
    my_list.append(losowa_liczba)

print(f'Pierwotna lista: {my_list}')


def bubble_sort(lista):
    n = len(lista)
    # iterowanie przez wszystkie liczby z listy
    for i in range(n):
        # ostatnie i elementow jest juz posortowane
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # zamiana miejscami, jesli kolejnosc byla odwrotna
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


posortowana_lista = bubble_sort(my_list)
print(f"Posortowana lista: {posortowana_lista}")


def linear_search(lista, x):
    n = len(lista)
    for i in range(n):
        if x == lista[i]:
            return i


def binary_search(lista, x):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if lista[mid] < x:
            low = mid + 1
        elif lista[mid] > x:
            high = mid - 1
        else:
            return mid


print("Wynik wyszukiwania: ", binary_search(my_list, 15))


"""while a > 5:
    print(a)

imiona = ["Maks", 'Maciek', 'Krystian', 'Kamil']

for imie in imiona:
    print(imie)

for i in range(15):
    print(i)"""