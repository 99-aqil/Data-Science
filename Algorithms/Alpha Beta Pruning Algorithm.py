from random import*
import math
maximum = math.inf
minimum = -math.inf
count = 0


def alpha_beta_pruning(dep, nod, maximizing_player, v, alpha, beta, branfac, c):
    if dep == 0:
        return v[nod], c+1
    if maximizing_player:
        best = minimum
        for k in range(0, branfac):
            value, c = alpha_beta_pruning(dep-1, nod*branfac+k, False, v, alpha, beta, branfac, c)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                c-1
                break
        return best, c
    else:
        best = maximum
        for k in range(0, branfac):
            value, c = alpha_beta_pruning(dep-1, nod*branfac+k, True, v, alpha, beta, branfac, c)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                c-1
                break
        return best, c


node = 0
bracu_id = list(map(int, input("Please enter your BRACU ID: ")))
depth = 2 * bracu_id[0]
branching_factor = bracu_id[2]
b = [bracu_id[-1], bracu_id[-2]]
string = ""
for j in b:
    string += str(j)
HP = int(string)
f = int(input("Enter the minimum value for the negative range of HP: "))
g = int(input("Enter the maximum value for the negative range of HP: "))
Bin = lambda m: [randint(f, g) for _ in range(1, m+1)]
leaf_nodes = Bin(branching_factor ** depth)
print("1. Depth and Branch ratio is", depth, ":", branching_factor)
print("2. Terminal States (leaf node values) are ", end="")
print(*leaf_nodes, sep=",")
x, y = alpha_beta_pruning(depth, node, True, leaf_nodes, minimum, maximum, branching_factor, count)
remaining_HP = HP - x
if remaining_HP < 0:
    print("3. Left life(HP) of the defender after maximum damage caused by the attacker is", 0)
else:
    print("3. Left life(HP) of the defender after maximum damage caused by the attacker is", remaining_HP)
print("4. After Alpha-Beta Pruning Leaf Node Comparisons", y)
