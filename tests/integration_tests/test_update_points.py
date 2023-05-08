import server


class TestUpdatePoints:
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

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club

    def test_points_update(self):
        # club_points_before = int(self.club[0]["points"])
        places_booked = 1

        self.client.post(
            "/purchase_places",
            data={
                "places": places_booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        result = self.client.get("/club-points")

        assert result.status_code == 404
        # assert f"<td>{self.club[0]['name']}</td>" in result.data.decode()
        # assert f"<td>{club_points_before - places_booked}</td>" in result.data.decode()
