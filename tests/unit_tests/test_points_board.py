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


def test_update_points():
    places_booked = 5

    client.post(
        "/purchase_places",
        data={
            "places": places_booked,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    response = client.get("/clubs-points")
    assert response.status_code == 200
    assert str(int(club[0]["points"]) - places_booked) in response.data.decode()
