import React from 'react';
import PropertyCard from './PropertyCard';
import '../styles/PropertyList.css';

const PropertyList = ({ properties, owners, onDelete }) => {
  const getOwnerById = (ownerId) => owners?.find((owner) => owner.id === ownerId);

  if (!properties || properties.length === 0) {
    return <p>No properties available.</p>;
  }

  return (
    <div className="property-list">
      <h2>Lista Nieruchomości</h2>
      <div className="property-items">
        {properties.map((property) => {
          const owner = getOwnerById(property.wlasciciel_id);
          return (
            <div key={property.id} className="property-item">
              <PropertyCard property={property} owner={owner} />
              <button
                className="delete-button"
                onClick={() => onDelete(property.id)}
              >
                Usuń
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PropertyList;
