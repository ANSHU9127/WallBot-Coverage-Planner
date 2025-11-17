from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_plan():
    r = client.post("/plan", json={"width":5,"height":5,"obstacles":[]})
    assert r.status_code==200
    assert len(r.json()["path"])>0

def test_all():
    r = client.get("/trajectories")
    assert r.status_code==200