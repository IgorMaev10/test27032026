def operate_two_numbers(number_1: float | int, number_2: float | int, operation: str = "sum") -> float | int:
    if operation == "sum":
        result = number_1 + number_2
        return result
    elif operation == "sub":
        result = number_1 - number_2
        return result
    else:
        raise ValueError("Invalid operation")

def format_string(string: str, upper: bool = True) -> str:
    if upper:
        formatted_string = string.upper()
    else:
        formatted_string = string.lower()
    return formatted_string

def separate_numbers(row_of_numbers: str, separator: str = ",") -> int:
    numbers = row_of_numbers.split(separator)
    numbers = [int(number) for number in numbers]
    sum_of_numbers = sum(numbers)
    return sum_of_numbers
