from locust import HttpUser, task, between

competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Winter Festival",
            "date": "2023-12-16 14:00:00",
            "numberOfPlaces": "36"
        }
]

clubs = [
    {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    },
    {
        "name": "Iron Temple",
        "email": "admin@irontemple.com",
        "points": "4"
    },
    {
        "name": "She Lifts",
        "email": "kate@shelifts.co.uk",
        "points": "12"
    }
]


class TestServer(HttpUser):
    wait_time = between(1, 5)
    competition = competitions[2]
    club = clubs[2]

    def on_start(self):
        self.client.get("/", name="Home")
        self.client.post("/show_summary", data={'email': self.club["email"]}, name="Summary")

    @task
    def get_booking(self):
        self.client.get(
            f"/book/{self.competition['name']}/{self.club['name']}",
            name="booking places"
        )

    @task
    def post_booking(self):
        self.client.post(
            "/purchase_places",
            data={
                "places": 0,
                "club": self.club["name"],
                "competition": self.competition["name"]
            },
            name="Purchase places"
        )

    @task
    def get_board(self):
        self.client.get("/clubs-points", name="Available points of clubs")

    def on_stop(self):
        self.client.get("/logout", name="Logout")
