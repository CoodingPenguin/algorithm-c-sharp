# 두 명 같은 팀일 때의 점수
def check(team):
    score = 0
    for i in team:
        for j in team:
            score += board[i-1][j-1]
    return score


team = []


def dfs(player):
    global minScore
    if team and team[0] > 1:
        return
    if len(team) == N//2:
        teamA = check(team)
        teamB = check(list(set(range(1, N+1))-set(team)))
        minScore = min(minScore, abs(teamA - teamB))
        return
    for i in range(player+1, N+1):
        team.append(i)
        dfs(i)
        team.pop()


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
minScore = 1000
dfs(0)

print(minScore)
