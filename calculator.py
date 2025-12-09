def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    return principal * rate * time / 100

def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    if n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    return principal * (1 + rate/(100*n))**(n*time)

def calculate_tax(amount: float, tax_rate: float) -> float:
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("tax_rate должно быть между 0 и 100")
    return amount * tax_rate / 100
  
print(calculate_simple_interest(1000, 10, 1))
print(calculate_simple_interest(100, 100, 10))
