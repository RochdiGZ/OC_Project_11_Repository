import server

client = server.app.test_client()

competition = [
    {
        "name": "Winter Festival",
        "date": "2023-12-16 10:00:00",
        "numberOfPlaces": "20"
    }
]

club = [
    {
        "name": "Strength club",
        "email": "account@club.org",
        "points": "15"
    }
]


def test_available_points():
    client.post(
        "/purchase_places",
        data={
            "places": 5,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert int(competition[0]["numberOfPlaces"]) >= 5 and int(club[0]["points"]) >= 5


def test_not_available_points():
    client.post(
        "/purchase_places",
        data={
            "places": 30,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert not(int(competition[0]["numberOfPlaces"]) >= 30 and int(club[0]["points"]) >= 30)
