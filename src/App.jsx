import React, { useState } from 'react';
import PropertyList from './components/PropertyList';
import Filters from './components/Filters';
import AddPropertyForm from './components/AddPropertyForm';
import './styles/App.css';

const App = () => {
  const [properties, setProperties] = useState([
    { id: 1, type: 'Dom', name: 'Piękny Dom', price: 500000 },
    { id: 2, type: 'Mieszkanie', name: 'Mieszkanie w centrum', price: 300000 },
    { id: 3, type: 'Magazyn', name: 'Duży Magazyn', price: 700000 },
    { id: 4, type: 'Biuro', name: 'Biuro z widokiem', price: 450000 },
  ]);

  const [filter, setFilter] = useState('Wszystkie');

  const handleFilterChange = (selectedType) => {
    setFilter(selectedType);
  };

  const handleAddProperty = (newProperty) => {
    setProperties((prevProperties) => [
      ...prevProperties,
      { id: Date.now(), ...newProperty },
    ]);
  };

  const filteredProperties =
    filter === 'Wszystkie'
      ? properties
      : properties.filter((property) => property.type === filter);

  return (
    <div className="app">
      <h1>Sprzedaż Nieruchomości</h1>
      <Filters onFilterChange={handleFilterChange} />
      <AddPropertyForm onAddProperty={handleAddProperty} />
      <PropertyList properties={filteredProperties} />
    </div>
  );
};

export default App;
