import numpy as np

def remove_max(arr):
  max_val = np.max(arr)
  max_ind = np.where(arr == max_val)
  return np.delete(arr, max_ind)

def dq(n):
  if n == 1:
    return np.array([0])
  a = dq((n + 1) // 2) * 2
  l = a
  r = a + 1
  if n % 2 == 1:
    r = remove_max(r)
  return np.concatenate((l, r))

#sorted(dq(16))
def check(arr):
  n = arr.shape[0]
  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        x1, x2, x3 = arr[i], arr[j], arr[k]
        if x2 * 2 == (x1 + x3):
          return False
  return True

x=dq(16)
if check(x):
  print(x)
# print(check(dq(7)))
