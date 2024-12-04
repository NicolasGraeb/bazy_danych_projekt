import axios from 'axios';

// Lista endpointów do sprawdzenia
const endpoints = [
  'http://127.0.0.1:8080/wlasciciele',
  'http://127.0.0.1:8080/nieruchomosc',
  'http://127.0.0.1:8080/nieruchomosc/9'
];

// Funkcja do sprawdzenia połączenia z endpointem
async function checkEndpoints() {
  for (const endpoint of endpoints) {
    try {
      console.log(`Sprawdzanie: ${endpoint}`);
      const response = await axios.get(endpoint);
      console.log(`✅ ${endpoint} - Status: ${response.status}`);
    } catch (error) {
      if (error.response) {
        console.error(`❌ ${endpoint} - Błąd: ${error.response.status}`);
      } else if (error.request) {
        console.error(`❌ ${endpoint} - Brak odpowiedzi serwera.`);
      } else {
        console.error(`❌ ${endpoint} - Nieoczekiwany błąd: ${error.message}`);
      }
    }
  }
}

// Uruchomienie funkcji
checkEndpoints();
