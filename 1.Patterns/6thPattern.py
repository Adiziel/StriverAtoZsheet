def create_pattern(num):
  for i in range(1,num+1)[::-1]:
    for j in range(1,i+1):
      print(j, end=' ')
    print("\r")

if __name__ == "__main__":
  num = int(input('Enter the count for pattern: '))
  create_pattern(num)