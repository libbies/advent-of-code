"""advent of code 2021 day 4 part 2"""
# from pprint import pprint
inputs = open("input.txt").read().splitlines()

numbers = [int(_) for _ in inputs[0].split(',')]

def check_winner(card):
    """check if a bingo card is a winner"""
    # rows
    if any(True for r in range(5) if sum(card[r])==-5):
        return True
    # columns
    if any(True for c in range(5) if sum(card[r][c] for r in range(5))==-5):
        return True
    return False

boards = []
board = []
for line in inputs[1:]:
    if not line:
        if board:
            boards.append(list(board))
        board = []
    else:
        board.append([int(_) for _ in line.split()])
boards.append(list(board))

winners = []
answer = 0
for num in numbers:
    for i, board in enumerate(boards):
        if i in winners:
            continue
        for row in range(5):
            if num in board[row]:
                board[row][board[row].index(num)] = -1
        if check_winner(board):
            # pprint(board)
            # print(boards.index(board))
            # print(num * sum(c for row in board for c in row if c>0))
            winners.append(i)
            answer = num * sum(c for row in board for c in row if c>0)

print("part 2 answer:", answer)
