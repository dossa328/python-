# max-heapify sudo
'''
MAX-Heapify(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= heap-size[A] and A[l] > A[i]
        then largest <- l
        else largest <- i
    if r<= heap-size[A] and A[r] > A[largest]
        then largest <- r
    if largest != i
        then exchange A[i] <-> A[largest]
            MAX-HEAPIFY(A, largest)

BUILD-MAX-HEAP(A)
    heap-size[A] <- length[A]
    for i <- [length[A]/2] downto 1     [ ] -> floor function, I couldn't find replace symbol

        do MAX-HEAPIFY(A,i)
'''


def heapify(input_list, index, heap_size):
    left_node_idx = index * 2 + 1
    right_node_idx = index * 2 + 2
    if left_node_idx < heap_size and input_list[left_node_idx] > input_list[index]:
        largest = left_node_idx
    else:
        largest = index
    if right_node_idx < heap_size and input_list[right_node_idx] > input_list[largest]:
        largest = right_node_idx
    if largest != index:
        input_list[index], input_list[largest] = input_list[largest], input_list[index]
        heapify(input_list, largest, heap_size)


def build_max_heap(input_list, heap_size):
    for i in range(len(input_list)/2-1, -1, -1):
        heapify(input_list, i, heap_size)


def heap_sort(input_list):
    n = len(input_list)
    build_max_heap(input_list, n)
    for i in range(n-1, -1, -1):
        input_list[0], input_list[i] = input_list[i], input_list[0]
        n = n - 1
        heapify(input_list, 0, n)
    return input_list


input_lists = [1, 16, 4, 10, 14, 7, 9, 3, 2, 8]
# input_lists = [1, 16, 4]
print (heap_sort(input_lists))
