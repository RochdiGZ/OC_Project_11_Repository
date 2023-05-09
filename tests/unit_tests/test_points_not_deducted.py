import server

client = server.app.test_client()
competition = [
    {
        "name": "Test",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }
]

club = [
    {
        "name": "Test club",
        "email": "test_club@email.com",
        "points": "10"
    }
]


def test_deduct_points():
    places_booked = 5

    result = client.post(
        "/purchase_places",
        data={
            "places": places_booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert result.status_code == 200
    assert int(club[0]["points"]) - places_booked >= 0
