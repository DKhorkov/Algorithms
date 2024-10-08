"""
Use the following ideas to develop a non-recursive, linear-time O(n) algorithm for the maximum-subarray problem.
Start at the left end of the array, and progress toward the right, keeping track of the maximum subarray seen so far.
Knowing a maximum subarray A[1..j], extend the answer to find a maximum subarray ending at index j+1 by using
the following observation: a maximum subarray A[i..j+1], is either a maximum subarray of A[1..j] or
a subarray A[i..j+1], for some 1≤i≤j+1. Determine a maximum subarray of the form A[i..j+1] in constant
time based on knowing a maximum subarray ending at index j.
"""


from typing import List, Tuple, Union
from math import inf


def max_subarray_linear(array: List[int]) -> Tuple[int, int, Union[int, float]]:
    max_sum: float = -inf
    high_index: int = 0
    low_index: int = 0

    current_sum: float = -inf
    current_low_index: int = 0
    current_high_index: int

    """
    Итерируемся по массиву: Для каждого индекса будем считать, что он является верхним, чтобы наш подмассив мог 
    увеличиваться. 
    
    Если текущая сумма больше нуля - прибавляем к ней элемент массива, соответствующий текущему индексу. 
    
    Если же сумма меньше нуля (как в изначальном случае), возникают две ситуации - текущий подмассив не является 
    наибольшим (начинаем отсчитывать новый подмассив с текущего индекса), либо все элементы массива 
    являются отрицательными (вернется подмассив из одного наибольшего отрицательного элемента).
    Соответственно, считаем, что текущий индекс является нижним, с которого начинается подмассив, 
    а текущая сумма равна элементу массива, который соответствует текущему индексу.
    
    Если текущая сумма больше максимальной, то максимальная сумма и является текущей, а нижний и верхний индексы
    являются текущим нижним и текущим верхним индексами соответственно.
    """
    for i in range(len(array)):
        current_high_index = i
        if current_sum > 0:
            current_sum += array[i]
        else:
            current_sum = array[i]
            current_low_index = i

        if current_sum > max_sum:
            max_sum = current_sum
            low_index = current_low_index
            high_index = current_high_index

    return low_index, high_index, max_sum


if __name__ == '__main__':
    array: List[int] = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # array: List[int] = [-3, -25, -1]
    left_index, right_index, max_sum = max_subarray_linear(array=array)
    max_subarray: List[int] = array[left_index: right_index + 1]
    print(array, max_subarray, max_sum, sep='\t-\t')
