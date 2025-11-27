

def binary_search(array: list, target: int) -> int:
    '''
    Iterative Binay Search Implementation
    '''

    tail = 0
    head = len(array)-1

    while tail <= head:
        pointer = (tail+head)//2
        if array[pointer] == target:
            return pointer
        elif target > array[pointer]:
            tail = pointer+1
        else:
            head = pointer-1

    #is while loop didn't catch the target
    return None

def test(result):
    if result != None:
        print("Successful Run")
    else:
        print("Something went wrong. Debuggin team will deal with it later")

#=========================================================

test_array = [2,3,4,5,22,23,25,26,27,28,29,44,55,110,234,3353,5355]
target = 110

result = binary_search(test_array, target)
test(result)

     