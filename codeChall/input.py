# x, y, z, n = int(input()), int(input()), int(input()), int(input())
# print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1)
#        for c in range(0, z+1) if a + b + c != n])

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arranged = set(list(arr))
#     listed = list(arranged)

#     print(sorted(listed)[-2])

# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     print(students)
# if __name__ == '__main__':
#     students = []
#     names = []
#     scores = []
#     smalls = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     for item in students:
#         scores.append(item[1])
#     small = min(scores)
#     large = max(scores)
#     for val in scores:
#         if val > small:
#             smalls.append(val)
#     for i in students:
#         if i[1] == min(smalls):
#             names.append(i[0])
#     for j in sorted(names):
#         print(j)

# from statistics import mean
# import math


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print("%.2f" % mean(student_marks[query_name]))
from itertools import combinations_with_replacement

a = ''.join(input())
b = int(input())
c = sorted(list(combinations_with_replacement(a, b)))

for i in c:
    print(i)
