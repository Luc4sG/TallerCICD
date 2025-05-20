from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)
def test_hola_mundo():
    response = cliente.get("/")
    assert response.status_code == 200  
    assert response.json() == {"message": "Hola mundo"}



