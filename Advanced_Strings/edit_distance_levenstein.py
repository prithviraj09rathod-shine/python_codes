def edit_distance_levenstein(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a distance matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the distance matrix
    for i in range(m + 1):
        dp[i][0] = i  # Deletion
    for j in range(n + 1):
        dp[0][j] = j  # Insertion

    # Compute the edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution

    return dp[m][n]

# Example usage:
s1 = "kitten"
s2 = "sitting"
print(edit_distance_levenstein(s1, s2))  # Output: 3
s1 = "flaw"
s2 = "lawn"
print(edit_distance_levenstein(s1, s2))  # Output: 2
s1 = "intention"
s2 = "execution"    
print(edit_distance_levenstein(s1, s2))  # Output: 5