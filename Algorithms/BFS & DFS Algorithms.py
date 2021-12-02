# Name: AQIL MAHMUD, ID: 18341010, Section:10
# -----------------------------------------------------------------------------------
# Answer --> 1
from collections import deque


def max_effected_region(mat):
    max_counter = 0
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            if mat[row][column] == "Y":
                region_cell_count = count_effected_region(mat, row, column)
                max_counter = max(max_counter, region_cell_count)
    return max_counter


def count_effected_region(mat, row, col):
    if any([row<0, col<0, row>=len(mat), col>=len(mat[0])]):
        return 0
    if mat[row][col] == "N":
        return 0
    count = 1
    mat[row][col] = 'N'
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if any([r!=row, c!=col]):
                count += count_effected_region(mat, r, c)
    return count


matrix = [["N", "N", "N", "Y", "Y", "N", "N"],
          ["N", "Y", "N", "N", "Y", "Y", "N"],
          ["Y", "Y", "N", "Y", "N", "N", "Y"],
          ["N", "N", "N", "N", "N", "Y", "N"],
          ["Y", "Y", "N", "N", "N", "N", "N"],
          ["N", "N", "N", "Y", "N", "N", "N"]]

# matrix = [["Y", "Y", "N", "N", "N"],
#          ["N", "Y", "Y", "N", "N"],
#          ["N", "N", "Y", "N", "N"],
#          ["Y", "N", "N", "N", "N"]]
print("Output of Question 1...")
print(max_effected_region(matrix))

# -----------------------------------------------------------------------------------
# Answer --> 2


def apocalypse(dead_zone, r, c):

    global t
    row, column = len(dead_zone), len(dead_zone[0])

    dead_zone[r][c] = "A"
    q = deque()
    q.append((r, c, 0))
    while q:
        r, c, t = q.popleft()
        for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
            if 0<=nr< row and 0<= nc<column and dead_zone[nr][nc] == "H":
                dead_zone[nr][nc] = "A"
                q.append((nr, nc, t+1))
    return dead_zone, t


area = [["A", "H", "H"],
        ["T", "H", "H"],
        ["H", "T", "H"]]

# area = [["A", "H", "T", "H"],
#        ["H", "H", "T", "A"],
#        ["T", "T", "H", "H"],
#        ["A", "H", "T", "H"],
#        ["H", "T", "H", "H"]]
sr = sc = t = 0
alien = "A"


area, time = apocalypse(area, sr, sc)

survival_count = 0
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == "H":
            survival_count+=1

print("--------------------------")
print("Output of Question 2...")
print("Time:", time, "minutes")
if survival_count <=0:
    print("No one Survived")
else:
    print(survival_count, "survived")
