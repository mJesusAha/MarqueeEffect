from django.test import TestCase
from unittest import skipIf
from .models import *
import requests


def for_test():
    try:
        requests.get("http://127.0.0.1:8000/")
        return 1
    except:
        return 0


class Test(TestCase):
    @skipIf(for_test() != 1, "No")
    def test_run(self):
        self.assertEqual(requests.get("http://127.0.0.1:8000/").status_code, 200)
        print("@@@@ Сервер подключен")
        self.assertEqual(
            requests.get(
                "http://127.0.0.1:8000/runtext/?color=%23ffc677&background=%23000000&text=text"
            ).status_code,
            200,
        )
        self.assertEqual(
            requests.get("http://127.0.0.1:8000/runtext/?color=%23ffc677").status_code,
            200,
        )
        self.assertEqual(
            requests.get(
                "http://127.0.0.1:8000/runtext/?background=%23000000"
            ).status_code,
            200,
        )
        self.assertEqual(
            requests.get("http://127.0.0.1:8000/runtext/?text=text").status_code, 200
        )
        self.assertEqual(
            requests.get(
                "http://127.0.0.1:8000/runtext/?color=%jk&background=%23000000&text=text"
            ).status_code,
            200,
        )


if __name__ == "__main__":
    unittest.main()
