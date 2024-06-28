from __future__ import annotations

class Money:
    _value: float

    def __init__(self, value: float):
        if value < 0:
            raise Exception("Invalid amount")
        
        self._value = value

    def __lt__(self, other):
        return self._value < other._value
    
    def __le__(self, other):
        return self._value <= other._value

    def __eq__(self, other):
        return self._value == other._value

    def __gt__ (self, other):
        self._value > other._value
    
    def __ge__ (self, other):
        self._value >= other._value

    def __add__(self, other):
        return Money(self._value + other._value)
    
    def __sub__(self, other):
        return Money(self._value - other._value)
    
    def __repr__(self) -> str:
        return f"<Money: {self._value}>"
    
    @property
    def value(self) -> float:
        return self._value