def create_pattern(num):
  for i in range(num+1):
    for j in range(i):
      print('*', end=' ')
    print("\r")

if __name__ == "__main__":
  num = int(input('Enter the count for pattern: '))
  create_pattern(num)