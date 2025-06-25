import pandas as pd
from stage2_api.db import SessionLocal, engine
from stage2_api.models import Base, PromptResult

def load_data():
    df = pd.read_csv("stage1_scraper/results.csv")
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    for _, row in df.iterrows():
        result = PromptResult(
            prompt=row["prompt"],
            nike=int(row["Nike"]),
            adidas=int(row["Adidas"]),
            hoka=int(row["Hoka"]),
            new_balance=int(row["New Balance"]),
            jordan=int(row["Jordan"])
        )
        session.add(result)

    session.commit()
    session.close()