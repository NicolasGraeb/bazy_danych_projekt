import React, { useState, useEffect } from 'react';

const WlascicielePage = () => {
  const [owners, setOwners] = useState([]);
  const [newOwner, setNewOwner] = useState({ imie: '', nazwisko: '' });
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const apiRequest = async (url, options = {}) => {
    try {
      const response = await fetch(url, options);
      if (!response.ok) {
        throw new Error(`API request failed: ${response.statusText}`);
      }
      return await response.json();
    } catch (err) {
      setError(err.message);
      console.error('API request error:', err);
      throw err;
    }
  };

  // Fetch owners on page load
  useEffect(() => {
    const fetchOwners = async () => {
      try {
        setLoading(true);
        const data = await apiRequest('http://127.0.0.1:8080/wlasciciele');
        setOwners(data);
      } catch (err) {
        console.error('Error fetching owners:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchOwners();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewOwner((prevOwner) => ({
      ...prevOwner,
      [name]: value,
    }));
  };

  const handleAddOwner = async (e) => {
    e.preventDefault();

    if (!newOwner.imie || !newOwner.nazwisko) {
      alert('Proszę wypełnić wszystkie pola.');
      return;
    }

    try {
      const response = await apiRequest('http://127.0.0.1:8080/wlasciciele/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newOwner),
      });

      // Update the owner list with the new owner
      setOwners((prevOwners) => [...prevOwners, response]);
      setNewOwner({ imie: '', nazwisko: '' }); // Reset the form
    } catch (err) {
      console.error('Error adding owner:', err);
    }
  };

  return (
    <div className="wlasciciele-page">
      <h1>Właściciele</h1>

      <form onSubmit={handleAddOwner}>
        <h2>Dodaj nowego właściciela</h2>
        <input
          type="text"
          name="imie"
          placeholder="Imię"
          value={newOwner.imie}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="nazwisko"
          placeholder="Nazwisko"
          value={newOwner.nazwisko}
          onChange={handleInputChange}
          required
        />
        <button type="submit">Dodaj Właściciela</button>
      </form>

      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <ul>
          {owners.map((owner) => (
            <li key={owner.id}>
              {owner.imie} {owner.nazwisko}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default WlascicielePage;
