from itertools import combinations
import sys


def get_score(team):
    score = 0
    for player in team:
        for others in (set(team)-set([player])):
            score += board[player][others]
    return score


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
teams = list(combinations(range(N), N//2))
teams = teams[:len(teams)//2]
min_diff = 1000

# 팀의 경우의 수를 다 루핑
for team in teams:
    # 팀A와 팀B를 구함
    teamA, teamB = team, tuple((set(range(N)) - set(team)))
    # 각 팀의 점수를 구함
    teamA_score, teamB_score = get_score(teamA), get_score(teamB)
    # 최소값 갱신
    min_diff = min(min_diff, abs(teamA_score - teamB_score))

print(min_diff)
