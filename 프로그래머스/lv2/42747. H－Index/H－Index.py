def solution(citations):
    citations.sort()
    for i in citations:
        if i >= len(citations[citations.index(i):]):
            return len(citations[citations.index(i):])
    return 0