def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    raise NotImplementedError


def search(numbers, start, end):
    min_element = numbers[start]
    min_element_index = start

    for i in range(start + 1, end):
        if numbers[i] < min_element:
            min_element = numbers[i]
            min_element_index = i

    return min_element_index


def selection_sort(numbers):
    n = len(numbers)

    for i in range(n - 1): 
        min_i = search(numbers, i, n)
        numbers[i], numbers[min_i] = numbers[min_i], numbers[i] 
