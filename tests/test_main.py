from app.main import app


def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert r.json["status"] == "running"


def test_hello():
    r = app.test_client().get("/hello/Amine")
    assert r.status_code == 200
    assert r.json["message"] == "Bonjour Amine !"