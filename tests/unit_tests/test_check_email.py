import server

client = server.app.test_client()


def test_known_email():
    result = client.post("/show_summary", data=dict(email="john@simplylift.co"))
    assert result.status_code == 302


def test_unknown_email():
    result = client.post("/show_summary", data=dict(email="account@domain.com"))
    assert result.status_code == 302
