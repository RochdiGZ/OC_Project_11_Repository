from locust import HttpUser, task, between

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


class TestRetrieveCompetitions(HttpUser):
    wait_time = between(1, 5)

    club = clubs[2]

    def on_start(self):
        self.client.get("/", name="Home")

    @task
    def get_board(self):
        self.client.get("/clubs-points", name="Available points of clubs")

    def on_stop(self):
        self.client.get("/logout", name="Logout")
