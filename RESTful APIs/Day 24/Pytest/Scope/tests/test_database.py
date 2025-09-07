def test_database_connection_1(database_connection):
    assert database_connection["db"] == "connected"

def test_database_connection_2(database_connection):
    assert database_connection["db"] == "connected"
