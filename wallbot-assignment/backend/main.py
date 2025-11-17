from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Trajectory
from .schemas import WallInput, TrajectoryResponse
from .path_planner import generate_trajectory
import time, logging

Base.metadata.create_all(bind=engine)
app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/plan", response_model=TrajectoryResponse)
def plan_wall(data: WallInput, db: Session = Depends(get_db)):
    start = time.time()
    trajectory = generate_trajectory(data.width, data.height, data.obstacles)
    db_obj = Trajectory(width=data.width, height=data.height,
                        obstacles=str(data.obstacles), path=str(trajectory))
    db.add(db_obj); db.commit(); db.refresh(db_obj)
    logging.info(f"Generated in {time.time()-start:.4f}s")
    return TrajectoryResponse(id=db_obj.id, width=data.width,
                              height=data.height, obstacles=data.obstacles,
                              path=trajectory)

@app.get("/trajectories")
def all_traj(db: Session = Depends(get_db)):
    return db.query(Trajectory).all()

@app.get("/trajectory/{tid}")
def one_traj(tid: int, db: Session = Depends(get_db)):
    return db.query(Trajectory).filter(Trajectory.id == tid).first()