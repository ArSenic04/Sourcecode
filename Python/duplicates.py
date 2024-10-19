# Function to find duplicates using a set
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example
arr = [1, 2, 3, 4, 5, 3, 2, 6, 7, 2]
duplicates = find_duplicates(arr)
print("Duplicates in the array:", duplicates)
