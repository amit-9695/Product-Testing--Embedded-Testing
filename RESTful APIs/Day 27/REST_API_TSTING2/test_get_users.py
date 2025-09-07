import requests
def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data['page'] == 2
    assert len(data['data']) == 6
    print(data['data'[0]])
    assert any(user['first_name'] == "Michael" for user in data['data'])
    
    
def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    
    #creating the header
    headers = {
        "Content-Type": "application/json",
        "x-api-key" : "reqres-free-v1",
    }

    response = requests.post(url, json=payload,headers=headers)
    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    
    
    
    
    # Appliying put(update) request
def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {"name": "neo", "job": "zion leader"}
    
    #creating the header
    headers = {
        "Content-Type": "application/json",
        "x-api-key" : "reqres-free-v1",
    }

    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "neo"
    assert data["job"] == "zion leader"
