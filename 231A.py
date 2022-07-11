# take the number of steps

n = int(input())

# make a counter

count = 0

# take the numbers and put it in a list

for i in range(n):
    
  num = list(map(int,input().split()))
  
  n = n - 1
  
  if (num[0] + num[1] + num[2] ) > 1:
    count = count + 1


# print the result

print(count) 