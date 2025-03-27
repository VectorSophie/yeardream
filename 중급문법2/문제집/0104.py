def num_fight(player1, player2):
    # 문제의 조건들에 맞추어 코딩하세요.
    p1cnt = 0
    p2cnt = 0
    for i in range(6):
        if player1[i] > player2[i]:
            p1cnt += 1
        elif player1[i] < player2[i]:
            p2cnt += 1
        elif player1[i] == player2[i]:
            pass
        if len(player1) != len(set(player1)) or len(player2) != len(set(player2)):
            return "동작그만 밑장빼기냐?"
        if player1[i]>= 7 or player1[i]<=0 or player2[i]>= 7 or player2[i]<=0:
            return "동작그만 밑장빼기냐?"
    if p1cnt > p2cnt:
        return "player1 승리!"
    elif p2cnt > p1cnt:
        return "player2 승리!"
    elif p1cnt == p2cnt:
        return "서로 비겼습니다."

print(num_fight([1,3,2,4,5,6], [2,3,1,4,6,5]))