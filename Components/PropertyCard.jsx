import React from 'react';
import '../styles/PropertyCard.css';

const PropertyCard = ({ property, owner }) => {
  return (
    <div className="property-card">
      <h3>{property.name || 'Nieruchomość'}</h3>
      <p>Typ: {property.typ_nieruchomosci || 'Nieznany'}</p>
      <p>Właściciel: {owner ? `${owner.imie} ${owner.nazwisko}` : 'Nieznany'}</p>
      <p>Adres: {property.adres}</p>
      <p>Powierzchnia: {property.powierzchnia} m²</p>
      <p>Cena: {property.cena ? `${property.cena} zł` : 'Cena nieznana'}</p>
    </div>
  );
};

export default PropertyCard;
