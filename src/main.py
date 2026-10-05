def add(a: int, b: int) -> int:
    return a + b


result = add(3, 5)
print(result)


def multyply(x: int, y: int) -> int:
    return x * y


value = multyply(4, 6)
print(value)


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = 0.0

    for number in numbers:
        total += number

    return total / len(numbers)


values = [10.0, 20.0, 30.0, 40.0]
average = calculate_average(values)
print(average)
