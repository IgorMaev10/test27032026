from functions import operate_two_numbers, format_string, separate_numbers

params1 = {"number_1": 1.3, "number_2": 5, "operation": "sum"}
params2 = {"string": "hello world", "upper": True}
params3 = {"row_of_numbers": "30, -10, 15", "separator": ","}

result = operate_two_numbers(**params1)
text = format_string(**params2)
sum_of_numbers = separate_numbers(**params3)

