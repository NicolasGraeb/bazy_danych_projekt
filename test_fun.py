from db_utils import *
import requests
#create_wlasciciel("Jan", "Kowalski")
#delete_wlasciciel(1)
#create_nieruchomosc(2, 120, "Warszawa, ul. Przykladowa 123", "DOM")
#print(get_all_wlasciciele())

# #update_wlasciciel(1, "Jan", "Nowak")
result = add_nieruchomosc(
    typ_nieruchomosci="MIESZKANIE",
    wlasciciel_id=2,
    powierzchnia=75.0,
    adres="Kraków, ul. Mieszkaniowa 10",
    liczba_pokoi=3,
    pietro=2,
    cena=300000
)
print(result)
# import requests
#
# # Define the endpoint
url = "http://127.0.0.1:8080/add_nieruchomosc/"

payload = {
    "typ_nieruchomosci":"MIESZKANIE",
    "wlasciciel_id":2,
    "powierzchnia":75.0,
    "adres":"Kraków, ul. Mieszkaniowa 10",
    "liczba_pokoi":3,
    "pietro":2,
    "cena":300000
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
try:
    response = requests.post(url, json=payload, headers=headers)

    # Print the response status and body
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")



