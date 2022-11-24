import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)
    answer = 0
    try:
        while heap[0] < K:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            answer += 1
        return answer
    except:
        return -1
        
    