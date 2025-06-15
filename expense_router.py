from fastapi import APIRouter, HTTPException
from models import Expense, UpdateExpense
from database import expenses_collection
from bson import ObjectId

router = APIRouter()

@router.get("/")
def get_all_expenses():
    expenses = []
    for expense in expenses_collection.find():
        expense["_id"] = str(expense["_id"])
        expenses.append(expense)
    return expenses

@router.post("/")
def create_expense(expense: Expense):
    result = expenses_collection.insert_one(expense.dict())
    return {"message": "Expense added", "id": str(result.inserted_id)}

@router.put("/{expense_id}")
def update_expense(expense_id: str, update_data: UpdateExpense):
    if not ObjectId.is_valid(expense_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    update_fields = {k: v for k, v in update_data.dict(exclude_unset=True).items() if v is not None}

    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = expenses_collection.update_one(
        {"_id": ObjectId(expense_id)},
        {"$set": update_fields}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense updated successfully"}

@router.delete("/{expense_id}")
def delete_expense(expense_id: str):
    if not ObjectId.is_valid(expense_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = expenses_collection.delete_one({"_id": ObjectId(expense_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense deleted"}

@router.get("/debug")
def debug():
    count = expenses_collection.count_documents({})
    return {"total_documents": count}
