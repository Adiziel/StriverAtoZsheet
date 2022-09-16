def create_pattern(num):
  k=num
  for i in range(1,num+1)[::-1]:
    for j in range(num-i):
      print(end=" ")
    k=k-1
    for j in range(i):
      print('*', end=" ")
    print("\r")

if __name__ == "__main__":
  num = int(input('Enter the count for pattern(please keep it ODD for good result): '))
  create_pattern(num)