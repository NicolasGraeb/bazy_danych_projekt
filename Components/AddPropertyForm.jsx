import React, { useState } from 'react';

const AddPropertyForm = ({ onAddProperty, owners }) => {
  const [formData, setFormData] = useState({
    wlasciciel_id: '',
    typ_nieruchomosci: '',
    powierzchnia: '',
    adres: '',
    cena: '',
    liczba_pokoi: '',
    pietro: '',
    powierzchnia_dzialki: '',
    liczba_czlonow: '',
    wspolna_sciana: false,
    stan_wykonczenia: '',
    basen: false,
    typ_budynku_biurowego: '',
  });

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? e.target.checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Ensure required fields are filled
    if (formData.typ_nieruchomosci && formData.powierzchnia && formData.adres && formData.cena && formData.wlasciciel_id) {
      onAddProperty({
        typ_nieruchomosci: formData.typ_nieruchomosci,
        wlasciciel_id: Number(formData.wlasciciel_id),
        powierzchnia: parseFloat(formData.powierzchnia),
        adres: formData.adres,
        cena: parseFloat(formData.cena),
        liczba_pokoi: formData.liczba_pokoi ? Number(formData.liczba_pokoi) : null,
        pietro: formData.pietro ? Number(formData.pietro) : null,
        powierzchnia_dzialki: formData.powierzchnia_dzialki ? parseFloat(formData.powierzchnia_dzialki) : null,
        liczba_czlonow: formData.liczba_czlonow ? Number(formData.liczba_czlonow) : null,
        wspolna_sciana: formData.wspolna_sciana,
        stan_wykonczenia: formData.stan_wykonczenia || null,
        basen: formData.basen,
        typ_budynku_biurowego: formData.typ_budynku_biurowego || null,
      });
      setFormData({
        wlasciciel_id: '',
        typ_nieruchomosci: '',
        powierzchnia: '',
        adres: '',
        cena: '',
        liczba_pokoi: '',
        pietro: '',
        powierzchnia_dzialki: '',
        liczba_czlonow: '',
        wspolna_sciana: false,
        stan_wykonczenia: '',
        basen: false,
        typ_budynku_biurowego: '',
      });
    } else {
      alert('Proszę wypełnić wszystkie wymagane pola.');
    }
  };

  return (
    <form className="add-property-form" onSubmit={handleSubmit}>
      <h2>Dodaj nową nieruchomość</h2>

      {/* Select Owner */}
      <select name="wlasciciel_id" value={formData.wlasciciel_id} onChange={handleChange} required>
        <option value="">Wybierz właściciela</option>
        {owners.map((owner) => (
          <option key={owner.id} value={owner.id}>
            {owner.imie} {owner.nazwisko}
          </option>
        ))}
      </select>

      {/* Select Property Type */}
      <select name="typ_nieruchomosci" value={formData.typ_nieruchomosci} onChange={handleChange} required>
        <option value="">Wybierz typ nieruchomości</option>
        <option value="MIESZKANIE">Mieszkanie</option>
        <option value="DOM">Dom</option>
        <option value="BIURO">Biuro</option>
      </select>

      {/* Common Fields */}
      <input
        type="number"
        name="powierzchnia"
        placeholder="Powierzchnia (m²)"
        value={formData.powierzchnia}
        onChange={handleChange}
        required
      />
      <input type="text" name="adres" placeholder="Adres" value={formData.adres} onChange={handleChange} required />
      <input
        type="number"
        name="cena"
        placeholder="Cena (zł)"
        value={formData.cena}
        onChange={handleChange}
        required
      />

      {/* Fields for "Mieszkanie" */}
      {formData.typ_nieruchomosci === 'MIESZKANIE' && (
        <>
          <input
            type="number"
            name="liczba_pokoi"
            placeholder="Liczba pokoi"
            value={formData.liczba_pokoi}
            onChange={handleChange}
          />
          <input
            type="number"
            name="pietro"
            placeholder="Piętro"
            value={formData.pietro}
            onChange={handleChange}
          />
        </>
      )}

      {/* Fields for "Dom" */}
      {formData.typ_nieruchomosci === 'DOM' && (
        <>
          <input
            type="number"
            name="powierzchnia_dzialki"
            placeholder="Powierzchnia działki (m²)"
            value={formData.powierzchnia_dzialki}
            onChange={handleChange}
          />
          <input
            type="number"
            name="liczba_czlonow"
            placeholder="Liczba członów"
            value={formData.liczba_czlonow}
            onChange={handleChange}
          />
          <label>
            <input
              type="checkbox"
              name="wspolna_sciana"
              checked={formData.wspolna_sciana}
              onChange={handleChange}
            />
            Wspólna ściana
          </label>
        </>
      )}

      {/* Fields for "Biuro" */}
      {formData.typ_nieruchomosci === 'BIURO' && (
        <>
          <input
            type="number"
            name="liczba_biur"
            placeholder="Liczba biur"
            value={formData.liczba_biur}
            onChange={handleChange}
          />
          <input
            type="text"
            name="typ_budynku_biurowego"
            placeholder="Typ budynku biurowego"
            value={formData.typ_budynku_biurowego}
            onChange={handleChange}
          />
        </>
      )}

      <button type="submit">Dodaj nieruchomość</button>
    </form>
  );
};

export default AddPropertyForm;
