# 초기 값 세팅
board = []
line = []
turn = "Black"
cases = [[-1, 1], [0, 1], [1, 1], [1, 0]]  # ↗, →, ↘, ↓ 

# 보드 틀 만들기
for i in range(9):
    line.append("+")
for i in range(9):
    board.append(line.copy())


# 보드 그리는 함수
def draw():
    print(end='  ')
    for j in range(1, 10):
        print(j, end=' ')
    print()
    for j in range(1, 10):
        print(j, *board[j-1])


# 승부 났는지 확인
def check():
    for a in range(9):
        for b in range(9):
            stone = board[a][b]
            if stone == "+":
                continue
            for case in cases:
                count = 1
                for i in range(1, 5):
                    try:
                        if board[a + case[0] * i][b + case[1] * i] == stone:
                            count += 1
                        else:
                            continue
                    except:
                        continue
                if count == 5:
                    print("The winner is Black.") if stone == "●" else print("The winner is White.")
                    quit()



draw()

while True:
    print("{}'s turn.".format(turn))

    while True:
        try:
            x, y = map(int, input("Place a stone. ").split())
        except:
            print("Please put the stone again.")

        if board[x-1][y-1] == "●" or board[x-1][y-1] == "○":
            print("Please put the stone again.")
        else:
            break

    if turn == "Black":
        board[x-1][y-1] = "●"
        turn = "White"
    else:
        board[x-1][y-1] = "○"
        turn = "Black"

    draw()
    check()
    