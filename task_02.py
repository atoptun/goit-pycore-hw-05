from typing import Callable, Generator
import re


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Extracts and yields numbers from a text, one by one """
    reg = re.compile(r"\b\d+\.\d+\b")
    for match in re.finditer(reg, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Returns the sum of numbers in a text"""
    return sum(x for x in func(text))



text = """Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
