ANSWER = [3, 1, 3, 5, 5, 1, 2, 2, 4, 4]

student = list(map(int,input().split()))

score = 0

for i in range(10):
    if ANSWER[i] == student[i]:
        score += 1

print("점수:", score)