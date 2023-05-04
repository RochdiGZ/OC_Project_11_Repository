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

"""
def test_points_update():
    club_points_before = int(club[0]["points"])
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
    assert f"<td>{club[0]['name']}</td>" in result.data.decode()
    assert f"<td>{club_points_before - places_booked}</td>" in result.data.decode()
"""