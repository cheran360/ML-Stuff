A = [1, 2, 0, 1, 2]
K = 3
#A[i] <= A[i + K],i = 1,2,3,..,N-K

# A = [2,3,2,3]

# 1 2 0 1 2
flag = 1
i = 0
steps = 0
while i + K < len(A) - 1:

  if A[i] > A[i + k]):
    flag = 0
    steps += 1
  i += 1

if flag == 1:
  print(0)
else:
  print(steps)