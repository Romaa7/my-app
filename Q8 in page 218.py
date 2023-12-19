class Array:
    def find_combinations(self, input_array):
        input_array.sort()
        result = []

        for i in range(len(input_array) - 2):
            left, right = i + 1, len(input_array) - 1
            while left < right:
                total = input_array[i] + input_array[left] + input_array[right]
                if total == 0:
                    result.append([input_array[i], input_array[left], input_array[right]])
                left, right = left + (total < 0), right - (total > 0)

        return result


input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
output = Array().find_combinations(input_array)
print(output)  # Output should be [[-10, 2, 8], [-7, -3, 10]]

