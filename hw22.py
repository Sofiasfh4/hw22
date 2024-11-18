
result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError(f"ValueError: a ({a}) is less than b ({b})")
        if b > 100:
            raise IndexError(f"IndexError: b ({b}) is greater than 100")
        return a / b
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None  # Повертаємо None, щоб продовжити обробку

data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2, 3): 15, 8: 4, 106: 105}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)