import server

client = server.app.test_client()

competition = [
    {
        "name": "Test",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "40"
    }
]

club = [
    {
        "name": "Test club",
        "email": "test_club@email.com",
        "points": "20"
    }
]

places_booked = [
    {
        "competition": "Test",
        "booked": [5, "Test club"]
    }
]


def test_less_than_twelve():
    booked = 5

    response = client.post(
        "/purchasePlaces",
        data={
            "places": booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert response.status_code == 404


def test_more_than_twelve_once():
    booked = 15

    response = client.post(
        "/purchasePlaces",
        data={
            "places": booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert response.status_code == 404


def test_more_than_twelve_added():
    booked = 8

    response = client.post(
        "/purchasePlaces",
        data={
            "places": booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert response.status_code == 404
