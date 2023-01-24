import random
from tabulate import tabulate
num_trials = 1000
face1 = 0
face2=0
face3 = 0
face4=0
face5 = 0
face6=0
for trail in range(num_trials):
    random_number = random.random()
    #print(random_number)
    if (random_number >0 and random_number<1/6):
        face1 += 1
    elif (random_number >1/6 and random_number<2/6):
        face2 += 1
    elif (random_number >2/6 and random_number<3/6):
        face3 += 1
    elif (random_number >3/6 and random_number<4/6):
        face4 += 1
    elif (random_number >4/6 and random_number<5/6):
        face5 += 1
    elif (random_number >5/6 and random_number<6/6):
        face6 += 1
    else:
        print("error")

print("the numbers")
print(face1)
print(face2)
print(face3)
print(face4)
print(face5)
print(face6)
print("the %")
print((face1/num_trials)*100)
print((face2/num_trials)*100)
print((face3/num_trials)*100)
print((face4/num_trials)*100)
print((face5/num_trials)*100)
print((face6/num_trials)*100)

def findPercentage(face):
    percentage = (face/num_trials)*100
    rounded = round(percentage,1)
    return rounded

totalFrequency = face1+face2+face3+face4+face5+face6
totalPercentage = findPercentage(face1)+findPercentage(face2)+findPercentage(face3)+findPercentage(face4)+findPercentage(face5)+findPercentage(face6)
data = [
    [1,face1,findPercentage(face1)],
    [2,face2,findPercentage(face2)],
    [3,face3,findPercentage(face3)],
    [4,face4,findPercentage(face4)],
    [5,face5,findPercentage(face5)],
    [6,face6,findPercentage(face6)],
    ["TOTALS",totalFrequency,totalPercentage]
]

print(tabulate(data,headers=["FACE","FREQUENCY","PERCENTAGE"]))
