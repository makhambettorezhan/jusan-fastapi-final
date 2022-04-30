from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_sum_to_n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {
        "result": 55
    }

def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {
        "result": 3
}

def test_reverse():
    response = client.post(
        "/reverse",
        headers={"string": "hello"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "result": "olleh"
    }
    
def test_put_list():
    client.put(
        "/list",
        json={"element":"Apple"}
    )
    client.put(
        "/list",
        json={"element":"Microsoft"}
    )
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Apple", "Microsoft"]
    }

def test_put_list():
    client.put(
        "/list",
        json={"element":"Apple"}
    )
    client.put(
        "/list",
        json={"element":"Microsoft"}
    )
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Apple", "Microsoft"]
    }

def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Apple", "Microsoft"]
    }

def test_calc():
    resp_plus = client.post(
        "/calculator",
        json={
            "expr": "1,+,1"
        }
    )
    assert resp_plus.status_code == 200
    assert resp_plus.json() == {
        "result": 2
    }

def test_calc_div_zero():
    resp_zero_div = client.post(
        "/calculator",
        json={
            "expr": "1,/,0"
        }
    )
    assert resp_zero_div.status_code == 403

def test_calc_invalid_op():
    resp_invalid_op = client.post(
        "/calculator",
        json={
            "expr": "1,x,1"
        }
    )
    assert resp_invalid_op.status_code == 400
    
