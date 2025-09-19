def binary_to_decimal_manual(binary_str):
    decimal_value = 0
    power = 0
    for digit in reversed(binary_str):
        decimal_value += int(digit) * (2 ** power)
        power += 1
    return decimal_value

binary_input = "10110"
decimal_output = binary_to_decimal_manual(binary_input)
print(f"The decimal equivalent of {binary_input} is: {decimal_output}")