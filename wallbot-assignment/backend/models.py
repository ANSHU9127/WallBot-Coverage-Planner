from sqlalchemy import Column, Integer, String
from .database import Base

class Trajectory(Base):
    __tablename__ = "trajectories"
    id = Column(Integer, primary_key=True, index=True)
    width = Column(Integer)
    height = Column(Integer)
    obstacles = Column(String)
    path = Column(String)