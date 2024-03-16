def my_bubble_sort(A):
    for i in range(0, len(A) - 1, 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

def main():
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    my_bubble_sort(A)
    print(A)

if __name__ == "__main__":
    main()

# Output: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]