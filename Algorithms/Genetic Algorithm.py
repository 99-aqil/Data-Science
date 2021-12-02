import numpy as np
from random import*

transaction_register = []
number_of_transactions = int(input("Enter the number of transactions: "))
for i in range(number_of_transactions):
    transaction_type = input("Enter the transaction type: ")
    if transaction_type == "l":
        lend = int(input("Enter the money withdrawn: "))
        lend = lend*(-1)
        transaction_register.append(lend)
    elif transaction_type == "d":
        deposit = int(input("Enter the money deposited: "))
        transaction_register.append(deposit)

# transaction_register = [-100, 150, -400, -500, 1000, -460, 160, 200, -500, 100]
# transaction_register = [-120, -289, 475, -195, 6482, -160, 935]
# transaction_register = [-100, -450, 500, -7923, 9055]


def fitness(population, n):
    if all(element == 0 for element in population):
        return
    Sum = 0
    updated_register = []
    for k in range(n):
        updated_register.append((transaction_register[i]) * (population[i]))
    for j in range(len(updated_register)):
        Sum = Sum + updated_register[j]
    if -500 <= Sum <= 500:
        return Sum
    else:
        return -1


def select():
    Bin = lambda n: [randint(0, 1) for _ in range(1, n+1)]
    genome = Bin(len(transaction_register))

    return genome


def crossover(x, y):
    if len(x) != len(y):
        return ValueError()

    length = len(x)
    if length < 2:
        return x, y

    p = randint(1, length-1)
    t = x[0:p] + y[p:]
    return list(t)


def mutate(chromosome):
    total_gen = 2
    pm = 0.1
    no_of_mutations = int(np.round(pm * total_gen))
    gen_num = np.random.randint(0, total_gen - 1, no_of_mutations)
    Replacing_num = np.random.randint(0, 30, no_of_mutations)
    for j in range(no_of_mutations):
        b = gen_num[i]
        row = b // 4
        col = b % 4
        chromosome[row, col] = Replacing_num[i]

    return chromosome


flag = 0


def genetic_algorithm():
    global flag
    best_fit = 0
    population = []
    max_iteration = 10000
    n = max_iteration
    while n > 0:
        for m in range(len(transaction_register)):
            x = select()
            y = select()
            population = crossover(x, y)
            child = mutate(population)
            if fitness(child, len(transaction_register)) == best_fit:
                flag = 1
                return child
            population.append(child)
        n-=1
    return population


a = genetic_algorithm()
if flag == 0:
    print(-1)
else:
    print(*a, sep='')
