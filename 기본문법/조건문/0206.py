tasu = 0
anta = 0
while tasu == 0:
    tasu = int(input())
while anta == 0:
    anta = int(input())

init_tasu = 16
init_anta = 6
tayul = int(anta + init_anta) / (tasu + init_tasu)

hal = int(tayul * 10)  
pun = int(tayul * 100) % 10  
li = int(tayul * 1000) % 10 
if hal != 0:
    print(hal,end = "")
    print("할")
if pun != 0:
    print(pun,end = "")
    print("푼")
if li != 0:
    print(li,end = "")
    print("리")