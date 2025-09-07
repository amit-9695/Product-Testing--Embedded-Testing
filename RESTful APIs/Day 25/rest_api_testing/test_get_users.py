import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data['page'] == 2
    assert len(data['data']) == 6
    assert any(user['first_name'] == "Michael" for user in data['data'])
    
    
# Test post request
def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    
    # It is vey important to  define the header
    header ={
        "x-api-key" : "reqres-free-v1",
        "Content-Type" : "application/json"
    }

    response = requests.post(url, json=payload,headers=header)
    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    
#Testing put(update) request
def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {"name": "neo", "job": "zion leader"}
    
    # defining the header
    header ={
        "x-api-key" : "reqres-free-v1",
        "Content-Type" : "application/json"
    }

    response = requests.put(url, json=payload, headers=header)
    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "neo"
    assert data["job"] == "zion leader"
