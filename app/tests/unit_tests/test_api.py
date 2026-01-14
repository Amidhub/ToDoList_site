from fastapi.testclient import TestClient
import pytest

@pytest.mark.parametrize("name, password, code",
                         [
                            ('malina', 'zxc', 200),
                            ('leo', 'password123', 200), 
                            ('miki', '321123', 200),
                            (1, 'z', 200), 
                         ])
def test_register_user(name, password, code, ac : TestClient):
    response = ac.post("/auth/register", data = {
        "name" : name,
        "password" : password,
    })
    
    assert response.status_code == code
    
    
    
    
    
@pytest.mark.parametrize("name, password, code",
                         [
                            ('malina', 'zxc', 200),
                            ('leo', 'password123', 200), 
                            ('miki', '321123', 200),
                            ("luck", 'asdghj324', 401), 
                         ])
def test_login_user(name, password, code, ac : TestClient):
    response = ac.post("/auth/login", data = {
        "name" : name,
        "password" : password,
    })
    
    assert response.status_code == code