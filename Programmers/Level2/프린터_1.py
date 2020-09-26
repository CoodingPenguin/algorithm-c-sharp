def exists_large(paper, waitingList, priorities):
    if len(waitingList) == 0:
        return False
    for i in waitingList:
        if priorities[paper] < priorities[i]:
            return True
    return False


def solution(priorities, location):
    waitingList = list(range(len(priorities)))
    orderList = []
    while waitingList:
        paper = waitingList.pop(0)
        if exists_large(paper, waitingList, priorities):
            waitingList.append(paper)
        else:
            orderList.append(paper)
    return orderList.index(location)+1
