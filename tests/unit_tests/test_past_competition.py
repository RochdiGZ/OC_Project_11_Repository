import server


client = server.app.test_client()
competitions = [
    {
        "name": "Test_closed",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "20"
    },
    {
        "name": "Test_open",
        "date": "2024-03-27 10:00:00",
        "numberOfPlaces": "20"
    }
]

club = [
    {
        "name": "Test club",
        "email": "test_club@email.com",
        "points": "15"
    }
]


def test_book_closed_competition():
    result = client.get(
        f"/book/{competitions[0]['name']}/{club[0]['name']}"
    )
    assert result.status_code == 500


def test_book_open_competition():
    result = client.get(
        f"/book/{competitions[1]['name']}/{club[0]['name']}"
    )
    assert result.status_code == 500
