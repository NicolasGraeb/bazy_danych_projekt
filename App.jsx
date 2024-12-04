import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddPropertyForm from './components/AddPropertyForm';
import PropertyList from './components/PropertyList';
import Navbar from './components/Navbar';
import AgenciPage from './components/Agenci';
import WlascicielePage from './components/Wlasciciele';

const App = () => {
  const [properties, setProperties] = useState([]);
  const [owners, setOwners] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

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

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [ownersData, propertiesData] = await Promise.all([
          apiRequest('http://127.0.0.1:8080/wlasciciele'),
          apiRequest('http://127.0.0.1:8080/nieruchomosc/'),
        ]);
        setOwners(ownersData);
        setProperties(propertiesData);
      } catch (err) {
        console.error('Error fetching initial data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const addProperty = async (property) => {
    try {
      const response = await apiRequest('http://127.0.0.1:8080/add_nieruchomosc/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(property),
      });
      setProperties((prevProperties) => [...prevProperties, response]);
    } catch (err) {
      console.error('Error adding property:', err);
    }
  };
  const deleteProperty = async (id) => {
  try {
    const response = await fetch(`http://127.0.0.1:8080/nieruchomosc/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error || `Failed to delete property with id ${id}`);
    }

    // Remove the property from the local state
    setProperties((prevProperties) =>
      prevProperties.filter((property) => property.id !== id)
    );
  } catch (err) {
    console.error('Error deleting property:', err);
  }
};


  return (
    <Router>
      <Navbar />
      <div className="app">
        <Routes>
          <Route
            path="/"
            element={
              <>
                <h1>Zarządzanie Nieruchomościami</h1>
                {loading ? (
                  <p>Loading...</p>
                ) : error ? (
                  <p style={{ color: 'red' }}>{error}</p>
                ) : (
                  <>
                    <AddPropertyForm onAddProperty={addProperty} owners={owners} />
                    <PropertyList properties={properties} owners={owners} onDelete={deleteProperty} />;
                  </>
                )}
              </>
            }
          />
          <Route path="/agenci" element={<AgenciPage />} />
          <Route path="/wlasciciele" element={<WlascicielePage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
