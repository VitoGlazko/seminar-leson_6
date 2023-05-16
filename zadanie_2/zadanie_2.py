import random
random_numbers = [random.randint(0, 9) for _ in range(15)]
print(random_numbers)
number = input("Введите трехзначное натуральное число: ")

N = []
for i in number:
    N.append(int(i))
print(N)

start_index = []

i = 0
while i < len(random_numbers):
    if random_numbers[i] == N[0]:
        start_index.append(i)
    i += 1

length = len(start_index)

bool_array = []

def check_sequence(start_point, length):
    array = []
    i = 0
    while i < len(N):
        try:
            j = start_point
            while j <= start_point + length:
                if N[i] == random_numbers[j]:
                    array.append(j)
                j += 1
        except:
            break
        i += 1
    array = sorted(set(array))
    check_array = []
    for i in array:
        check_array.append(random_numbers[i])
    bool_array.append(check_array == N)

for start_point in start_index:
    check_sequence(start_point, length)

def result():
    if True in bool_array:
        print("Последовательность из ваших 3 элементов есть в массиве")
    else:
        print("Последовательности нет")
result()
