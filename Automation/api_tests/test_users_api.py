import requests

BASE_URL = "https://automationexercise.com/api"


def test_get_all_products():

    response = requests.get(f"{BASE_URL}/productsList")

    assert response.status_code == 200

    response_text = response.text

    assert "Blue Top" in response_text

def test_products_api_json():

    response = requests.get(f"{BASE_URL}/productsList")

    json_data = response.json()

    assert json_data["responseCode"] == 200