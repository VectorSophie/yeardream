money = int(input())

if money >= 1000:
    print("택시")
elif money >= 500:
    print("버스")
elif money >= 300:
    print("지하철")
else:
    print("도보")