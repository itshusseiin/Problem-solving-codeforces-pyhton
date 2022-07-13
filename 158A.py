# take user input 

list1 = list(map(int,input().split()))

scores = list(map(int,input().split()))

number = list1[0]

lowest_score = list1[1]

# make a counter

qualified = 0 

# compare the input with lowest score for qualifing 

for i in scores :
    if i > 0 :
        if i >= scores[lowest_score - 1]:
            qualified = qualified + 1
        

# print result

print(qualified)
