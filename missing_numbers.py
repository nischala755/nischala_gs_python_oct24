from collections import Counter

def find_missing_numbers():
    # Read the size of the first list
    n = int(input().strip())
    # Read the first list
    list_a = list(map(int, input().strip().split()))
    
    # Read the size of the second list
    m = int(input().strip())
    # Read the second list
    list_b = list(map(int, input().strip().split()))
    
    # Count occurrences of each number in both lists
    count_a = Counter(list_a)
    count_b = Counter(list_b)
    
    # Find the missing numbers
    missing_numbers = []
    
    for number in count_b:
        if count_b[number] > count_a.get(number, 0):
            missing_numbers.append(number)
    
    # Sort the missing numbers
    missing_numbers.sort()
    
    # Print the result
    print(" ".join(map(str, missing_numbers)))

# Call the function
find_missing_numbers()