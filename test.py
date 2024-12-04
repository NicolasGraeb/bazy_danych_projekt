import httpx

BASE_URL = "http://127.0.0.1:8080"

def test_create_wlasciciel():
    # Tworzenie nowego właściciela
    response = httpx.post(f"{BASE_URL}/wlasciciel/", json={"imie": "Jan", "nazwisko": "Kowalski"})
    assert response.status_code == 200, f"Failed: {response.text}"
    wlasciciel = response.json()
    assert wlasciciel["id"] is not None
    assert wlasciciel["imie"] == "Jan"
    assert wlasciciel["nazwisko"] == "Kowalski"
    print(f"Właściciel utworzony: {wlasciciel}")
    return wlasciciel["id"]

def test_get_all_wlasciciele():
    # Pobieranie wszystkich właścicieli
    response = httpx.get(f"{BASE_URL}/wlasciciel/")
    assert response.status_code == 200, f"Failed: {response.text}"
    wlasciciele = response.json()
    print(f"Wszyscy właściciele: {wlasciciele}")
    return wlasciciele

def test_create_nieruchomosc(wlasciciel_id):
    # Tworzenie nowej nieruchomości
    response = httpx.post(f"{BASE_URL}/nieruchomosc/", json={
        "wlasciciel_id": wlasciciel_id,
        "powierzchnia": 120,
        "adres": "Warszawa, ul. Przykladowa 123",
        "typ_nieruchomosci": "DOM"
    })
    assert response.status_code == 200, f"Failed: {response.text}"
    nieruchomosc = response.json()
    assert nieruchomosc["id"] is not None
    assert nieruchomosc["wlasciciel_id"] == wlasciciel_id
    assert nieruchomosc["powierzchnia"] == 120
    assert nieruchomosc["adres"] == "Warszawa, ul. Przykladowa 123"
    assert nieruchomosc["typ_nieruchomosci"] == "DOM"
    print(f"Nieruchomość utworzona: {nieruchomosc}")
    return nieruchomosc["id"]

def test_get_all_nieruchomosci():
    # Pobieranie wszystkich nieruchomości
    response = httpx.get(f"{BASE_URL}/nieruchomosc/")
    assert response.status_code == 200, f"Failed: {response.text}"
    nieruchomosci = response.json()
    print(f"Wszystkie nieruchomości: {nieruchomosci}")
    return nieruchomosci

def test_update_nieruchomosc(nieruchomosc_id):
    # Aktualizacja istniejącej nieruchomości
    response = httpx.put(f"{BASE_URL}/nieruchomosc/{nieruchomosc_id}", json={
        "wlasciciel_id": 1,
        "powierzchnia": 150,
        "adres": "Warszawa, ul. Przykladowa 321",
        "typ_nieruchomosci": "BIURO"
    })
    assert response.status_code == 200, f"Failed: {response.text}"
    updated_nieruchomosc = response.json()
    assert updated_nieruchomosc["id"] == nieruchomosc_id
    assert updated_nieruchomosc["powierzchnia"] == 150
    assert updated_nieruchomosc["adres"] == "Warszawa, ul. Przykladowa 321"
    assert updated_nieruchomosc["typ_nieruchomosci"] == "BIURO"
    print(f"Nieruchomość zaktualizowana: {updated_nieruchomosc}")

def test_delete_nieruchomosc(nieruchomosc_id):
    # Usunięcie nieruchomości
    response = httpx.delete(f"{BASE_URL}/nieruchomosc/{nieruchomosc_id}")
    assert response.status_code == 200, f"Failed: {response.text}"
    print(f"Nieruchomość o ID {nieruchomosc_id} została usunięta")

def test_delete_wlasciciel(wlasciciel_id):
    # Usunięcie właściciela
    response = httpx.delete(f"{BASE_URL}/wlasciciel/{wlasciciel_id}")
    assert response.status_code == 200, f"Failed: {response.text}"
    print(f"Właściciel o ID {wlasciciel_id} został usunięty")

if __name__ == "__main__":
    # Testy właścicieli
    wlasciciel_id = test_create_wlasciciel()
    test_get_all_wlasciciele()

    # Testy nieruchomości
    nieruchomosc_id = test_create_nieruchomosc(wlasciciel_id)
    test_get_all_nieruchomosci()
    test_update_nieruchomosc(nieruchomosc_id)
    test_delete_nieruchomosc(nieruchomosc_id)

    # Usuwanie właściciela po zakończeniu testów
    test_delete_wlasciciel(wlasciciel_id)
