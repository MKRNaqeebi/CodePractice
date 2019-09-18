import collections

def solution(S):

    # initialization: stage 1
    alphabet = set(S)                         # the unique values ("symbols") in S
    var_count = collections.defaultdict(int)      # how many times each symbol appears in the sequence

    # initialization: stage 2
    start = 0
    for end in range(len(S)):
        var_count[S[end]] += 1
        if len(var_count) == len(alphabet):         # seen all the symbols yet?
            break
    end += 1

    best_start = start
    best_end = end

    # the induction
    while end < len(S):
        var_count[S[end]] += 1
        while var_count[S[start]] > 1:
            var_count[S[start]] -= 1
            start += 1
        end += 1
        if end - start < best_end - best_start: # new shortest sequence?
            best_start = start
            best_end = end

    if S[best_start] in S[best_start + 1: best_end]:
        best_start = best_start+1
    if S[best_end-1] in S[best_start: best_end-1]:
        best_end = best_end-1

    return len(S[best_start: best_end])

print(solution( [7, 3, 7, 3, 1, 3, 4, 1] ))
print(solution([2, 1, 1, 3, 2, 1, 1, 3]))
print(solution([7, 5, 2, 7, 2, 7, 4, 7] ))
