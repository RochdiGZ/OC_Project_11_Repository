import server

client = server.app.test_client()
competition = [
    {
        "name": "Winter Festival",
        "date": "2023-12-16 14:00:00",
        "numberOfPlaces": "36"
    }
]

club = [
    {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    }
]


def test_points_update():
    places_booked = 1

    client.post(
        "/purchase_places",
        data={
            "places": places_booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    result = client.get("/points-clubs")

    assert result.status_code == 404
