# URL: https://codeforces.com/problemset/problem/492/B

# In python, the input() function always return a string. If the user enters a sequence `0 1 2 3`, the `input()` function will return a string `"0 1 2 3"`. Each spaces the user entered will be captured and included in the string.
# So, it's time to make use of the function `split()` to separate the numbers by spaces.
firstLine = input().split()
numOfLanterns = int(firstLine[0])  # The number of lanterns given
length = int(firstLine[1])  # The length of the street
# The positions of the lanterns
# See this line of code, it transfers every substring which contains a single number under this condition. Notice that a pair of square brackets covers the loop progress of transfering strings into integers. It is called "list comprehension," it is a neat way to create a list.
# Here is an equilavent expression of the progress:
# lanternPositions = []
# user_input = input().split()
# for i in user_input:
#     lanternPositions.append(int(i))

lanternPositions = sorted([int(i) for i in input().split()])
# This function separate the numbers in the string by spaces and make them substrings in a list.
# After that, the string are gonna be like `"'0', '1', '2', '3'"`. Notice that the numbers in this list are still strings. So it's better to transfer them in to integer type.
# This function finds out the largest difference between two adjacent numbers of an array


def MaxLanternDistance(n, lanternPositions):
    # this is the maximum difference bewteen two adjacent lanterns.
    maxDiff = 0
    for i in range(n-1):
        diff = lanternPositions[i+1]-lanternPositions[i]
        maxDiff = max(maxDiff, diff)
    return maxDiff


# Now consider the distances from the first lantern to the start of the street and from the last lantern to the end of the street.
print(max(lanternPositions[0], length-lanternPositions[numOfLanterns-1], MaxLanternDistance(numOfLanterns, lanternPositions)/2))
