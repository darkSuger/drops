# coding = utf-8

print("input your age,heigth,weight and your earning")
manData = [4]
for i in range(4):
    manData[i] = input()
print("input your max request to girl :age,heigth,weight and earning")
manReMax = [4]
for i in range(4):
    manReMax[i] = input()
print("input your min request to girl :age,heigth,weight and earning")
manReMin = [4]
for i in range(4):
    manReMin[i] = input()

print("input your age,heigth,weight and your earning")
femaleData = [4]
for i in range(4):
    femaleData[i] = input()
print("input your max request to man :age,heigth,weight and earning")
femaleReMax = [4]
for i in range(4):
    femaleReMax[i] = input()
print("input your min request to man :age,heigth,weight and earning")
femaleReMin = [4]
for i in range(4):
    femaleReMin[i] = input()

flag = 1
for i in range(4):
    if manData[i] < femaleReMin[i] or manData[i] > femaleReMax[i]:
        flag = 0
    if femaleData[i] < manReMin[i] or femaleData[i] > manReMax[i]:
        flag = 0
if flag == 1:
    print "succeed"
else:
    print "fail"
