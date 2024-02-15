# def solution(K, A):
#     count = len(A)
#     for i, value_i in enumerate(A):
#         print((i, i))
#         for j in range(i + 1, len(A)):
#             if max(value_i, A[j]) - min(value_i, A[j]) <= K:
#                 print((i, j))
#                 count += 1
#             else:
#                 break

#     return count


# def solution(K, A):
#     count = len(A)
#     for i, value_i in enumerate(A):
#         print((i, i))
#         j = i + 1
#         l = [value_i]
#         while j <= len(A) - 1:
#             l.append(A[j])
#             if (max(l) - min(l)) <= K:
#                 print((i, j))
#                 count += 1
#                 j += 1
#             else:
#                 break
#     return count




from collections import deque

def solution(K, A):
    # Initialize count and two deques
    count = 0
    max_dq = deque()  # To keep track of the maximum element's index
    min_dq = deque()  # To keep track of the minimum element's index

    j = 0
    for i in range(len(A)):
        # Expand the window
        while j < len(A):
            # Update max_dq
            while max_dq and A[max_dq[-1]] <= A[j]:
                max_dq.pop()
            max_dq.append(j)
            
            # Update min_dq
            while min_dq and A[min_dq[-1]] >= A[j]:
                min_dq.pop()
            min_dq.append(j)
            
            # Check if current window satisfies the condition
            if A[max_dq[0]] - A[min_dq[0]] <= K:
                j += 1
            else:
                break
        
        # Count the number of subarrays that satisfy the condition
        # All subarrays starting at i and ending before j satisfy the condition
        count += j - i
        
        # Shrink the window
        if max_dq and max_dq[0] == i:
            max_dq.popleft()
        if min_dq and min_dq[0] == i:
            min_dq.popleft()

    return count



K = 2
A = [3, 5, 7, 6, 3]
print(solution(K, A))


K = 0
A = [1000000000, 1000000000]
print(solution(K, A))
