import server


class TestApp:
    client = server.app.test_client()

    competitions = server.load_competitions()

    clubs = server.load_clubs()

    def test_get_home(self):
        assert self.client.get('/').status_code == 200

        response = self.client.get('/')
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data

    def test_email(self):
        assert self.client.get('/').status_code == 200

        for club in self.clubs:
            assert self.client.get('/', data=club["email"]).status_code == 200

    def test_display_board(self):
        assert self.client.get('/').status_code == 200

        assert self.client.get('/clubs-points').status_code == 200

    def test_points_update(self):
        places_booked = 5

        self.client.post(
            "/purchase_places",
            data={
                "places": places_booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        response = self.client.get("/clubs-points")
        assert response.status_code == 200
        assert str(int(self.clubs[0]["points"]) - places_booked) in response.data.decode()

    def test_logout(self):
        response = self.client.get('/logout')
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
