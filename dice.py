import random
num_trials = 10
face1 = 0
face2=0
face3 = 0
face4=0
face5 = 0
face6=0
for i in range(num_trials):
    random_num = random.random()
    #print(random_num)
    new_string = str(random_num)
    shortened = float(new_string[:3])

    if((shortened==0.0)|(shortened==0.1)):
        face1 +=1
    elif(shortened==0.2):
        face2 +=1
    elif ((shortened == 0.3) | (shortened == 0.4)):
        face3 += 1
    elif ((shortened == 0.5) | (shortened == 0.6)):
        face4 += 1
    elif ((shortened == 0.7) | (shortened == 0.8)):
        face5 += 1
    elif ((shortened == 0.9) ):
        face6 += 1
    else:
        print("ERROR")


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



