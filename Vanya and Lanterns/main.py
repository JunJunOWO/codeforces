# URL: https://codeforces.com/problemset/problem/492/B

# In Python, the input() function always returns a string. For example, entering `0 1 2 3` will result in the string "0 1 2 3". All spaces entered by the user will be captured in the string.
# Therefore, we use the `split()` function to separate the numbers by spaces.

firstLine = input().split()
numOfLanterns = int(firstLine[0])  # The number of lanterns given
length = int(firstLine[1])  # The length of the street

# Capturing the positions of the lanterns
# The following line of code converts each substring into an integer. Observe the square brackets, which denote a "list comprehension" - a concise way to create a list in Python.
# Here's an equivalent breakdown of the process:
# lanternPositions = []
# user_input = input().split()
# for i in user_input:
#     lanternPositions.append(int(i))
lanternPositions = sorted([int(i) for i in input().split()])
# This function separates the numbers in the string by spaces, producing a list of substrings.
# After this, the list will look like ['0', '1', '2', '3']. Notice the numbers are still strings, so we should convert them to integers.
# The function then determines the largest gap between two adjacent numbers in the array.


# This represents the maximum gap between two adjacent lanterns.
def MaxLanternDistance(n, lanternPositions):
    maxDiff = 0
    for i in range(n-1):
        diff = lanternPositions[i+1]-lanternPositions[i]
        maxDiff = max(maxDiff, diff)
    return maxDiff


# We also need to consider the distances from the first lantern to the street's start and from the last lantern to its end.
print(max(lanternPositions[0], length-lanternPositions[numOfLanterns-1],
      MaxLanternDistance(numOfLanterns, lanternPositions)/2))