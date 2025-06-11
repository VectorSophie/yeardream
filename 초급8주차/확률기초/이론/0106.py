import random
answer_Q1andQ2 = 0
answer_Q2 = 0
answer_Q1orQ2 = 0
random.seed(4)

def random_answer():
    return random.choice(["A", "B"])

for i in range(30):
    Q1 = random_answer()
    Q2 = random_answer()
    if Q2 == "A":
        answer_Q2 += 1
    if Q2 == "A" and Q1 == "A":
        answer_Q1andQ2 += 1
    if Q2 == "A" or Q1 == "A":
        answer_Q1orQ2 += 1


print( "P(Q1 and Q2 | Q2 ):", answer_Q1andQ2 / answer_Q2)
print( "P(Q1 and Q2 | Q1 or Q2 ):", answer_Q1andQ2 / answer_Q1orQ2)