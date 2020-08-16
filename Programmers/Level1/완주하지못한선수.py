def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)
    lenPart = len(participant)
    for i in range(lenPart):
        if i == lenPart-1 or (participant[i] != completion[i]):
            return participant[i]