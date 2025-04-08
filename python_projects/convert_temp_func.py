def convert_temperature(temp: float, from_scale: str, to_scale: str) -> float:
    from_scale = from_scale.replace('"', '')
    to_scale = to_scale.replace('"', '')
    key = from_scale + to_scale
    transform_dict = {'FC': '(temp - 32) * 5/9',
                      'CF': 'temp * 9/5 + 32'}
    return eval(transform_dict[key])


input_data = input().split(', ')
temp = float(input_data[0])
from_scale = input_data[1]
to_scale = input_data[2]
print(convert_temperature(temp, from_scale, to_scale))
