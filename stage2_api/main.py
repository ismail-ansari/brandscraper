from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from stage2_api.db import SessionLocal
from stage2_api.models import PromptResult

app = FastAPI()
def get_db(): #dependency to get DB session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/mentions")
def get_mentions():
    db = next(get_db())
    total = {
        "nike": 0,
        "adidas": 0,
        "hoka": 0,
        "new_balance": 0,
        "jordan": 0
    }

    results = db.query(PromptResult).all()
    for row in results:
        total["nike"] += row.nike
        total["adidas"] += row.adidas
        total["hoka"] += row.hoka
        total["new_balance"] += row.new_balance
        total["jordan"] += row.jordan
    return total

@app.get("/mentions/{brand}")
def get_brand_mentions(brand: str):
    db = next(get_db())
    valid_brands = ["nike", "adidas", "hoka", "new_balance", "jordan"]
    if brand not in valid_brands:
        raise HTTPException(status_code=404, detail="Brand not found")
    results = db.query(PromptResult).all()
    total = sum(getattr(row, brand) for row in results)

    return {brand: total}