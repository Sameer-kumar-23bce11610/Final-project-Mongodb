from pydantic import BaseModel
from typing import Optional

class Expense(BaseModel):
    title: str
    amount: float
    category: str

class UpdateExpense(BaseModel):
    title: Optional[str]
    amount: Optional[float]
    category: Optional[str]

class Budget(BaseModel):
    category: str
    limit: float
