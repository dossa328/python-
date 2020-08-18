A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = []
len_A = len(A)
count = 0
for i in range(len_A):
    B.append(min(A))
    A.remove(min(A))
print(B)
print('\n')
print(count)
