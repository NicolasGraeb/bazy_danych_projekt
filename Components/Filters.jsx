import React from 'react';
import '../styles/Filters.css';

const Filters = ({ onFilterChange }) => {
  const propertyTypes = ['Wszystkie', 'Dom', 'Mieszkanie', 'Magazyn', 'Biuro'];

  return (
    <div className="filters">
      <label htmlFor="filter">Filtruj według typu:</label>
      <select
        id="filter"
        onChange={(e) => onFilterChange(e.target.value)}
      >
        {propertyTypes.map((type) => (
          <option key={type} value={type}>
            {type}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Filters;
