print(".................................................................................................")
print("                                 Welcome to Appie V.1.1.0                                        ")
print(".................................................................................................")

wscore = []
welo = []
lscore = []
lelo = []
count = 0
for i in range(3):
    data = int(input("Enter the score of winning teams speaker" + str(i+1) + ": "))
    wscore.append(data)
print(".................................................................................................")

for k in range(3):
    data2 = int(input("Enter the score of losing teams speaker" + str(k+1) + ": "))
    lscore.append(data2)

print(".................................................................................................")


for j in range(3):
    data1 = int(input("Enter the old ELO score winning teams speaker" + str(j+1) + ": "))
    welo.append(data1)

print(".................................................................................................")

for l in range(3):
    data3 = int(input("Enter the Old ELO score of losing teams speaker" + str(l+1) + ": "))
    lelo.append(data3)

flag = False

print(".................................................................................................")
