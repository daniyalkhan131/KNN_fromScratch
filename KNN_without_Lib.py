import random as r

dataset = list()
for j in range(2):
    for i in range(5):
        temp = list()
        temp.append(r.randrange(1, 50))
        temp.append(r.randrange(1, 50))
        temp.append(j)
        dataset.append(temp)
for j in range(2):
    for i in range(5):
        temp = list()
        temp.append(r.randrange(40, 90))
        temp.append(r.randrange(40, 90))
        temp.append(j)
        dataset.append(temp)
print(dataset)
print('-------' + '\n' + '--------')
import matplotlib.pyplot as plt

for j in range(2):
    x = list()
    y = list()
    z = list()
    for i in dataset:
        if i[2] == j:
            x.append(i[0])
            y.append(i[1])
    if (j == 0):
        plt.plot(x, y, 'ro')
    else:
        plt.plot(x, y, 'go')

point = [50, 75]
plt.plot(50, 75, 'bx')
plt.show()

def distance_fn(l1, l2):
    diff = 0
    for i in range(len(l1)):
        diff = diff + (l1[i] - l2[i]) ** 2
    return diff ** 0.5


distance = list()
for i in dataset:
    distance.append(distance_fn(i[0:2], point))
for i, j in zip(dataset, distance):
    print(i, j)
print('-------' + '\n' + '--------')


def sorting(dataset, distance):
    for i in range(len(distance) - 1):
        for j in range(len(distance) - i - 1):
            if (distance[j] > distance[j + 1]):
                distance[j], distance[j + 1] = distance[j + 1], distance[j]
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]


print('-------' + '\n' + '--------')
sorting(dataset, distance)
for i, j in zip(dataset, distance):
    print(i, j)

k = 4
k_list = list()
for i in range(k):
    k_list.append(dataset[i])
print('-------' + '\n' + '--------')
print(k_list)


def freq_class(k_list):
    c0, c1 = 0, 0
    for i in k_list:
        if (i[2] == 0):
            c0 += 1
        else:
            c1 += 1
    if (c0 > c1):
        return 0
    else:
        return 1


clas = freq_class(k_list)
print(clas)