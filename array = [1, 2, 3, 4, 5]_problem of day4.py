"""array = [1, 2, 3, 4, 5]
left_rotation_t = 2
n = len(array)
left_rotation_t = left_rotation_t % n
array[:n] = array[:n][::-1]
array[:n-left_rotation_t] = array[:n-left_rotation_t][::-1]
array[n-left_rotation_t:] = array[n-left_rotation_t:][::-1]
print(array)"""

array = [1, 2, 3, 4, 5]
left_rotation_t = 2

n = len(array)
rotation_count = left_rotation_t

while rotation_count > 0:
    first_element = array[0]
    for i in range(n - 1):
        array[i] = array[i + 1]
    array[n - 1] = first_element
    rotation_count -= 1

print("The array after rotation:")
print(array)