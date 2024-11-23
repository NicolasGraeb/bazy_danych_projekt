import React from 'react';
import '../styles/PropertyCard.css';

const PropertyCard = ({ property }) => {
  return (
    <div className="property-card">
      <h3>{property.name}</h3>
      <p>Typ: {property.type}</p>
      <p>Cena: {property.price} zł</p>
    </div>
  );
};

export default PropertyCard;
