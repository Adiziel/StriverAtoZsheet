def create_pattern(num):
  for i in range(num):
    for j in range(i+1):
      print(i+1, end=' ')
    print("\r")

if __name__ == "__main__":
  num = int(input('Enter the count for pattern: '))
  create_pattern(num)