# Implement a function to reverse a linked list (you don't need to define a full linked list class, just the logic).
# Complexity: 
# Desired time: 
# Time taken to solve: 

class Solution:
  def distinctSubsequences(self, S):
     # code here
     MOD = 10**9 + 7  # Modulo value
     n = len(S)
     dp = [0] * (n + 1)  # dp array to store subsequences count
     dp[0] = 1  # Base case: the empty subsequence
     # Dictionary to store the last occurrence of each character
     last_occurrence = {}
     
     for i in range(1, n + 1):
      dp[i] = (2 * dp[i - 1]) % MOD  # Add subsequences using current character
      if S[i - 1] in last_occurrence:  # If character has appeared before
        #print(S[i-1],' ',last_occurrence)
        dp[i] -= dp[last_occurrence[S[i - 1]] - 1]  # Subtract overlapping subsequences
        dp[i] %= MOD
        
        last_occurrence[S[i - 1]] = i  # Update last occurrence
        
     return dp[n]		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.distinctSubsequences(s)
        print(answer)
        print("~")

# } Driver Code Ends