import collections

def solution(S):
    """
    Calculate smallest sub-array length from an array in which all integer exists from the original array

    Sample Input                    ==> Sample Output
    [7, 3, 7, 3, 1, 3, 4, 1]        ==> 5
    [2, 1, 1, 3, 2, 1, 1, 3]        ==> 3
    [7, 5, 2, 7, 2, 7, 4, 7]        ==> 6
    [1, 1, 2, 3, 4, 5, 1, 1, 1]     ==> 5

    :param [] S: orignal array
    :return int: length of smallest subarray
    """

    alphabet = set(S)                               # get all unique numbers
    var_count = collections.defaultdict(int)        # make dict to hold count of all number in sub array
    start = 0
    for end in range(len(S)):
        var_count[S[end]] += 1                      # Count all number
        if len(var_count) == len(alphabet):         # Get possible best end if 0 is best start for subarray
            break

    best_start = start
    best_end = end

    while end < len(S):
        while var_count[S[start]] > 1:              # Check if starting element is more than once so we can remove
            var_count[S[start]] -= 1
            start += 1
        if end - start < best_end - best_start:     # Check if we have better subarray than previous
            best_start = start
            best_end = end
        var_count[S[end]] += 1                      # Move end forward for we can check we have best array here or ahead
        end += 1

    return 1 + best_end - best_start                # len of best array; +1 cause we incluse both end in smallest array

print(solution([7, 3, 7, 3, 1, 3, 4, 1]))
print(solution([2, 1, 1, 3, 2, 1, 1, 3]))
print(solution([7, 5, 2, 7, 2, 7, 4, 7]))
print(solution([1, 1, 2, 3, 4, 5, 1, 1, 1]))
