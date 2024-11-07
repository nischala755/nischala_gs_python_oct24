''' Sorting Boys and Girls'''
def can_arrange(n, boys, girls):
    boys.sort()
    girls.sort()

    # Try alternating starting with a boy first
    option1 = []
    for i in range(n):
        option1.append(boys[i])
        option1.append(girls[i])

    # Try alternating starting with a girl first
    option2 = []
    for i in range(n):
        option2.append(girls[i])
        option2.append(boys[i])

    # Check if option1 is in non-decreasing order
    def is_non_decreasing(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    if is_non_decreasing(option1) or is_non_decreasing(option2):
        return "YES"
    else:
        return "NO"

# Read input
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    results.append(can_arrange(n, boys, girls))

# Print results
for result in results:
    print(result)

