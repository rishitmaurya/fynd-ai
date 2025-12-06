# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine, Base
from app.models import Submission
from app.schemas import SubmitRequest, SubmissionOut
from app.llm import generate_user_reply, generate_summary, generate_recommended_actions
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feedback Backend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/submit", response_model=SubmissionOut)
def submit(req: SubmitRequest, db: Session = Depends(get_db)):
    if req.rating < 1 or req.rating > 5:
        raise HTTPException(status_code=400, detail="rating must be 1..5")
    # Generate AI outputs
    ai_reply = generate_user_reply(req.rating, req.review)
    ai_summary = generate_summary(req.review)
    ai_actions = generate_recommended_actions(req.rating, req.review)
    # Save to DB
    sub = Submission(rating=req.rating, review=req.review, ai_reply=ai_reply, ai_summary=ai_summary, ai_actions=ai_actions)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return SubmissionOut(
        id=sub.id,
        timestamp=sub.timestamp.isoformat(),
        rating=sub.rating,
        review=sub.review,
        ai_reply=sub.ai_reply,
        ai_summary=sub.ai_summary,
        ai_actions=sub.ai_actions
    )

@app.get("/submissions", response_model=List[SubmissionOut])
def list_submissions(limit: int = 200, db: Session = Depends(get_db)):
    items = db.query(Submission).order_by(Submission.timestamp.desc()).limit(limit).all()
    out = []
    for s in items:
        out.append(SubmissionOut(
            id=s.id,
            timestamp=s.timestamp.isoformat(),
            rating=s.rating,
            review=s.review,
            ai_reply=s.ai_reply,
            ai_summary=s.ai_summary,
            ai_actions=s.ai_actions
        ))
    return out
