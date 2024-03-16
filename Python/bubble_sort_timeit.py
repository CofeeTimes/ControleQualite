import timeit

mysetup='''
def my_bubble_sort(A):
    for i in range(0, len(A) - 1, 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

def main():
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # for 100 elements, 1000 elements, 10000 elements, 100000 elements
    B = [i for i in range(100, 0, -1)]
    C = [i for i in range(1000, 0, -1)]
    D = [i for i in range(10000, 0, -1)]
    # E = [i for i in range(100000, 0, -1)]

    my_bubble_sort(A)
    print(A)
    my_bubble_sort(B)
    print(B)
    my_bubble_sort(C)
    print(C)
    my_bubble_sort(D)
    print(D)
    # my_bubble_sort(E)
    # print(E)

if __name__ == "__main__":
    main()

# Output: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
'''

mycode = "main()"
print(timeit.timeit(setup = mysetup, stmt = mycode, number = 10))