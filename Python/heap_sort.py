def my_heap_sort(A):
    heap_size = len(A)
    build_heap(A, heap_size)

    for i in range(heap_size -1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        pile_up(A, 1, heap_size)

def build_heap(A, heap_size):
    for i in range((int)(heap_size/2), 0, -1):
        pile_up(A, i, heap_size)

def pile_up(A, i, heap_size):
    l = left(i)
    r = right(i)

    if l<= heap_size and A[l-1] > A[i-1]:
        max = l
    else:
        max = i

    if r <= heap_size and A[r-1] > A[max-1]:
        max = r

    if max != i:
        A[i-1], A[max-1] = A[max-1], A[i-1]
        pile_up(A, max, heap_size)

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def main():
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # for 100 elements, 1000 elements, 10000 elements, 100000 elements
    B = [i for i in range(100, 0, -1)]
    C = [i for i in range(1000, 0, -1)]
    D = [i for i in range(10000, 0, -1)]
    # E = [i for i in range(100000, 0, -1)]

    my_heap_sort(A)
    print(A)
    my_heap_sort(B)
    print(B)
    my_heap_sort(C)
    print(C)
    my_heap_sort(D)
    print(D)
    my_heap_sort(E)
    print(E)

if __name__ == "__main__":
    main()

# Output: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]