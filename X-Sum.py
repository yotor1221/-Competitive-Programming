def max_bishop_attack_sum(t, test_cases):
    results = []
    for case in test_cases:
        n, m, board = case
        primary_diagonal_sum = {}
        secondary_diagonal_sum = {}
        
        # Calculate the sum of each diagonal
        for i in range(n):
            for j in range(m):
                if (i - j) not in primary_diagonal_sum:
                    primary_diagonal_sum[i - j] = 0
                if (i + j) not in secondary_diagonal_sum:
                    secondary_diagonal_sum[i + j] = 0
                primary_diagonal_sum[i - j] += board[i][j]
                secondary_diagonal_sum[i + j] += board[i][j]
        
        max_sum = 0
        
        # Find the maximum sum of attacked cells
        for i in range(n):
            for j in range(m):
                current_sum = primary_diagonal_sum[i - j] + secondary_diagonal_sum[i + j] - board[i][j]
                max_sum = max(max_sum, current_sum)
        
        results.append(max_sum)
    
    return results
 
# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    test_cases.append((n, m, board))
 
# Get results
results = max_bishop_attack_sum(t, test_cases)
 
# Print results
for result in results:
    print(result)
