def my_heap_sort(A):
    heap_size = len(A)
    build_heap(A, heap_size)

    for i in range(heap_size -1, 1, -1):
        A[i] = A[0]
        heap_size -= 1

def build_heap(A, heap_size):
    for i in range((int)(heap_size/2), 0, -1):
        pile_up(A, i)

def pile_up(A, i):
    l = left(i)
    r = right(i)

    if l<= len(A) and A[l] > A[i]:
        max = l
    else:
        max = i

    if r <= len(A) and A[r] > A[max]:
        max = r

    if max != i:
        A[i] = A[max]
        pile_up(A, max)

def left(i):
    return

def right(i):
    return

def main():
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    my_heap_sort(A)
    print(A)

if __name__ == "__main__":
    main()

# Output: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]