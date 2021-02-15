def result(v, votes):
    votes = sorted(votes)

    if v % 2 != 0:
        return votes[v//2]
    else:
        if votes[v//2-1] == votes[v//2]:
            return votes[v//2]
        else:
            return "Tie"


V = int(input())
votes = input()
print(result(V, votes))
