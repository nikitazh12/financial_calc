import pytest
from calculator import (
  calculate_simple_interest,
  calculate_compound_interest,
  calculate_tax,
)


def test_calculate_simple_interest() -> None:
  ## Положительные тесты 
  assert calculate_simple_interest(1000, 10, 1) == 100.0
  assert calculate_simple_interest(100, 100, 10) == 1000.0
  
  ## Тесты с нулевыми значениями
  assert calculate_simple_interest(0, 0, 0) == 0.0
  assert calculate_simple_interest(1000, 0, 5) == 0.0
  
  ## Тесты с отрицательными значениями
  with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
    calculate_simple_interest(-1000, 10, 1)
  with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
    calculate_simple_interest(1000, -10, 1)
    
def test_calculate_compound_interest() -> None:
  ## Положительные тесты
  assert calculate_compound_interest(1000, 10, 1) == 1100.0
  assert calculate_compound_interest(100, 100, 10) == 102400.0
  
 ## Тесты с нулевыми значениями
  assert calculate_compound_interest(0, 0, 0) == 0.0
  assert calculate_compound_interest(1000, 0, 5) == 1000.0 
  assert calculate_compound_interest(1000, 5, 0) == 1000.0
  
  ## Тесты с отрицательными значениями
  with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
    calculate_compound_interest(1000, 10, 1, 0)
    
def test_calculate_tax() -> None:
  ## Положительные тесты
  assert calculate_tax(1000, 10) == 100.0
  assert calculate_tax(100, 100) == 100.0
  
  ## Тесты с нулевыми значениями
  assert calculate_tax(0, 0) == 0.0
  assert calculate_tax(1000, 0) == 0.0
  
  ## Тесты с отрицательными значениями
  with pytest.raises(ValueError, match="tax_rate должно быть между 0 и 100"):
    calculate_tax(1000, -10)
  with pytest.raises(ValueError, match="tax_rate должно быть между 0 и 100"):
    calculate_tax(1000, 110)