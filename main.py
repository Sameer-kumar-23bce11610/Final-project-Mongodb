from fastapi import FastAPI
from routers import expense_router
from database import expenses_collection, budgets_collection

app = FastAPI(title="Expense Tracker API")

@app.get("/")
def root():
    return {"message": "Expense Tracker is running"}

# Include expense routes
app.include_router(expense_router.router, tags=["Expenses"], prefix="/expenses")
