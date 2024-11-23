import React, { useState } from 'react';
import '../styles/AddPropertyForm.css';

const AddPropertyForm = ({ onAddProperty }) => {
  const [formData, setFormData] = useState({
    name: '',
    type: 'Dom',
    price: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.name && formData.price) {
      onAddProperty({
        name: formData.name,
        type: formData.type,
        price: parseFloat(formData.price),
      });
      setFormData({ name: '', type: 'Dom', price: '' }); // Reset formularza
    } else {
      alert('Proszę wypełnić wszystkie pola.');
    }
  };

  return (
    <form className="add-property-form" onSubmit={handleSubmit}>
      <h2>Dodaj nową nieruchomość</h2>
      <input
        type="text"
        name="name"
        placeholder="Nazwa nieruchomości"
        value={formData.name}
        onChange={handleChange}
      />
      <select
        name="type"
        value={formData.type}
        onChange={handleChange}
      >
        <option value="Dom">Dom</option>
        <option value="Mieszkanie">Mieszkanie</option>
        <option value="Magazyn">Magazyn</option>
        <option value="Biuro">Biuro</option>
      </select>
      <input
        type="number"
        name="price"
        placeholder="Cena nieruchomości"
        value={formData.price}
        onChange={handleChange}
      />
      <button type="submit">Dodaj nieruchomość</button>
    </form>
  );
};

export default AddPropertyForm;
