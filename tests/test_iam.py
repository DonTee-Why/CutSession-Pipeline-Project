from fastapi.testclient import TestClient
import pytest
from src.config import AppSettings
from src import main
from .base import BaseTestClass


client = TestClient(main.app)


class TestIAM(BaseTestClass):
    def test_register_users_returns_ok(self):
        self.set_up()

        payload = {
            "name": "Timilehin",
            "email": "timi@email.com",
            "username": "timiddon",
            "phoneNumber": "09798823411",
            "dob": "1993-12-09",
            "cityOfResidence": "Lagos",
            "password": "password"
        }
        response = client.post("/register/users", json=payload)

        assert response.status_code == 200

        self.tear_down()

    def test_register_users_returns_422_when_invalid_data_is_sent(self):
        self.set_up()

        payload = {
            "name": "Timilehin",
            "email": "timi@email.com",
            "username": "timiddon",
            "phoneNumber": "09798823411",
            "password": "password"
        }
        response = client.post("/register/users", json=payload)

        assert response.status_code == 422

        self.tear_down()

    def test_register_merchant_returns_ok(self):
        self.set_up()

        payload = {
            "name": "Joshua Bamidele",
            "email": "josh@email.com",
            "username": "joshbam",
            "phoneNumber": "09818876345",
            "cityOfOperation": "Lagos",
            "password": "password"
        }
        response = client.post("/register/merchants", json=payload)

        assert response.status_code == 200

        self.tear_down()

    def test_register_merchant_returns_422_when_invalid_data_is_sent(self):
        self.set_up()

        payload = {
            "name": "Joshua Bamidele",
            "username": "joshbam",
            "phoneNumber": "09818876345",
            "cityOfOperation": "Lagos",
            "password": "password"
        }
        response = client.post("/register/merchants", json=payload)

        assert response.status_code == 422

        self.tear_down()

    def test_sign_in_returns_ok(self):
        self.set_up()

        self.db.session.add(self.user)

        payload = {
            "username": "string",
            "password": "string",
            "accessType": "USER"
        }
        response = client.post("/sign-in", json=payload)

        assert response.status_code == 200

        self.tear_down()
