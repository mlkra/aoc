with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]

digits = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}
inv_digits = {v: k for k, v in digits.items()}

numbers = []
for number in input:
    number_len = len(number)
    converted_number = 0
    for i, digit in enumerate(number):
        converted_number += digits[digit] * 5 ** (number_len - i - 1)
    numbers.append(converted_number)

sum_decimal = sum(numbers)
result = []
b = sum_decimal
while True:
    r = b % 5
    b = b // 5
    if r > 2:
        b += 1
        r -= 5
    result.append(inv_digits[r])
    if b == 0:
        break
sum_5 = "".join(reversed(result))
print(sum_5)
