# take the input

n = int(input())


# do the math
for i in range(n):
    w = input()
    if len(w) > 10:
        new = w[0] + str(len(w) - 2) + w[-1]
    else : new = w
    
    print(new)