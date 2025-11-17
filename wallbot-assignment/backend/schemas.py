from pydantic import BaseModel

class Obstacle(BaseModel):
    x: float; y: float; width: float; height: float

class WallInput(BaseModel):
    width: float; height: float
    obstacles: list[Obstacle]

class TrajectoryResponse(BaseModel):
    id: int; width: float; height: float
    obstacles: list[Obstacle]
    path: list[tuple]