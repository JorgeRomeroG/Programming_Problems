class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        maxLen = 1
        startIndex = 0
        for i in range(len(A)):
            #first find longest odd palindrome
            low = i-1
            high = i+1

            while low >= 0 and high < len(A) and A[low] == A[high]:
                if (high - low + 1) > maxLen:
                    startIndex = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

            #second find longest even palindrome
            low = i
            high = i+1
            while low >= 0 and high < len(A) and A[low] == A[high]:
                if (high - low + 1) > maxLen:
                    startIndex = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

        return A[startIndex:startIndex+maxLen]


A = 'palindrome'

print(Solution().longestPalindrome(A))
