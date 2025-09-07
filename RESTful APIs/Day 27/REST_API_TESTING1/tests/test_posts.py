import pytest
from api import client

def test_get_all_posts():
    response=client.get_posts()
    assert response.status_code==200
    posts=response.json()
    assert isinstance(posts,list)
    assert len(posts)>0

def test_get_posts_by_id():
    response=client.get_post_by_id(1)
    assert response.status_code==200
    post=response.json()
    assert post["id"]==1
    print(post)
    assert 'title' in post