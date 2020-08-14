def pick_up(m, board):
    m = m-1
    doll = None
    for i in range(len(board)):
        if board[i][m]:
            doll = board[i][m]
            board[i][m] = 0
            break
    return doll


def solution(board, moves):
    result = 0
    basket = []
    for m in moves:
        pickUp = pick_up(m, board)
        if pickUp:
            basket.append(pickUp)
            if len(basket) > 1 and basket[-1] == basket[-2]:
                result += 2
                basket = basket[:-2]
    return result
