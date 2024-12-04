from flask import Flask, jsonify, request
from flask_cors import CORS
from db_utils import *

app = Flask(__name__)

# Enable CORS
CORS(app)

@app.route('/agenci/', methods=['GET'])
def fetch_agents():
    try:
        agenci = get_agenci()
        return jsonify([{"id": row[0], "imie": row[1], "nazwisko": row[2], "nr_licencji": row[3]} for row in agenci])
    except Exception as e:
        return jsonify({"error": f"Failed to fetch agents: {str(e)}"}), 500

@app.route('/wlasciciele/', methods=['GET'])
def get_wlasciciele():
    """
    Endpoint to fetch all owners.
    """
    try:
        wlasciciele = get_all_wlasciciele()
        return jsonify([{"id": row[0], "imie": row[1], "nazwisko": row[2]} for row in wlasciciele])
    except Exception as e:
        return jsonify({"error": f"Failed to fetch owners: {str(e)}"}), 500

@app.route('/wlasciciele/', methods=['POST'])
def add_wlasciciel():
    try:
        data = request.json
        new_id = create_wlasciciel(data['imie'], data['nazwisko'])
        return jsonify({"id": new_id, "imie": data['imie'], "nazwisko": data['nazwisko']})
    except Exception as e:
        return jsonify({"error": f"Failed to add owner: {str(e)}"}), 500

@app.route('/add_nieruchomosc/', methods=['POST'])
def add_nieruchomosc_endpoint():
    try:
        data = request.json

        required_fields = ['wlasciciel_id', 'typ_nieruchomosci', 'powierzchnia', 'adres', 'cena']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if data['powierzchnia'] <= 0:
            raise ValueError("Field 'powierzchnia' must be greater than 0.")
        if data['cena'] < 0:
            raise ValueError("Field 'cena' must be non-negative.")

        result = add_nieruchomosc(
            typ_nieruchomosci=data['typ_nieruchomosci'],
            wlasciciel_id=int(data['wlasciciel_id']),
            powierzchnia=float(data['powierzchnia']),
            adres=data['adres'],
            cena=float(data['cena']),
            typ_domu=data.get('typ_domu'),
            powierzchnia_dzialki=float(data['powierzchnia_dzialki']) if data.get('powierzchnia_dzialki') else None,
            liczba_pokoi=int(data['liczba_pokoi']) if data.get('liczba_pokoi') else None,
            pietro=int(data['pietro']) if data.get('pietro') else None,
            liczba_biur=int(data['liczba_biur']) if data.get('liczba_biur') else None,
            liczba_czlonow=int(data['liczba_czlonow']) if data.get('liczba_czlonow') else None,
            wspolna_sciana=bool(data.get('wspolna_sciana', False)),
            stan_wykonczenia=data.get('stan_wykonczenia'),
            basen=bool(data.get('basen', False)),
            typ_budynku_biurowego=data.get('typ_budynku_biurowego')
        )

        return jsonify(result), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

@app.route('/nieruchomosc/', methods=['GET'])
def get_all_nieruchomosci_endpoint():

    try:
        nieruchomosci = get_all_nieruchomosci()
        result = [
            {
                "id": row[0],
                "wlasciciel_id": row[1],
                "powierzchnia": row[2],
                "adres": row[3].strip(),
                "typ_nieruchomosci": row[4].strip(),
                "cena": row[5]
            }
            for row in nieruchomosci
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch properties: {str(e)}"}), 500

@app.route('/nieruchomosc/<int:nieruchomosc_id>', methods=['GET'])
def get_nieruchomosc_endpoint(nieruchomosc_id):
    """
    Endpoint to fetch a property by ID.
    """
    try:
        row = get_nieruchomosc_by_id(nieruchomosc_id)
        if row:
            return jsonify({
                "id": row[0],
                "wlasciciel_id": row[1],
                "powierzchnia": row[2],
                "adres": row[3].strip(),
                "typ_nieruchomosci": row[4].strip()
            })
        return jsonify({"error": "Property not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to fetch property: {str(e)}"}), 500

@app.route('/nieruchomosc/<int:nieruchomosc_id>', methods=['PUT'])
def update_nieruchomosc_endpoint(nieruchomosc_id):
    """
    Endpoint to update a property.
    """
    try:
        data = request.json
        success = update_nieruchomosc(
            nieruchomosc_id,
            data['wlasciciel_id'],
            data['powierzchnia'],
            data['adres'],
            data['typ_nieruchomosci']
        )
        if not success:
            return jsonify({"error": "Property not found"}), 404
        data['id'] = nieruchomosc_id
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Failed to update property: {str(e)}"}), 500

@app.route('/nieruchomosc/<int:nieruchomosc_id>', methods=['DELETE'])
def delete_nieruchomosc_endpoint(nieruchomosc_id):
    """
    Endpoint to delete a property.
    """
    try:
        success = delete_nieruchomosc(nieruchomosc_id)
        if not success:
            return jsonify({"error": "Property not found"}), 404
        return jsonify({"message": "Property deleted successfully"})
    except Exception as e:
        return jsonify({"error": f"Failed to delete property: {str(e)}"}), 500


@app.route('/nieruchomosc/<int:nieruchomosc_id>', methods=['DELETE'])
def delete_nieruchomosc(nieruchomosc_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT typ_nieruchomosci FROM NIERUCHOMOSC WHERE id = ?", (nieruchomosc_id,))
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": "Nieruchomość not found"}), 404

        typ_nieruchomosci = result[0]

        if typ_nieruchomosci == 'DOM':
            # Delete from DOM_SZEREGOWY and DOM_WOLNOSTOJACY
            cursor.execute("DELETE FROM DOM_SZEREGOWY WHERE DOMID IN (SELECT id FROM DOM WHERE NIERUCHOMOSCID = ?)", (nieruchomosc_id,))
            cursor.execute("DELETE FROM DOM_WOLNOSTOJACY WHERE DOMID IN (SELECT id FROM DOM WHERE NIERUCHOMOSCID = ?)", (nieruchomosc_id,))
            # Delete from DOM
            cursor.execute("DELETE FROM DOM WHERE NIERUCHOMOSCID = ?", (nieruchomosc_id,))

        elif typ_nieruchomosci == 'MIESZKANIE':
            # Delete from MIESZKANIE
            cursor.execute("DELETE FROM MIESZKANIE WHERE NIERUCHOMOSCID = ?", (nieruchomosc_id,))

        elif typ_nieruchomosci == 'BIURO':
            # Delete from BIURO
            cursor.execute("DELETE FROM BIURO WHERE NIERUCHOMOSCID = ?", (nieruchomosc_id,))

        # Step 3: Delete the main property record
        cursor.execute("DELETE FROM NIERUCHOMOSC WHERE id = ?", (nieruchomosc_id,))

        # Check if the property was deleted
        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({"error": "Failed to delete property"}), 500

        conn.commit()
        return jsonify({"message": "Nieruchomość and related records deleted successfully"}), 200
    except Exception as e:
        conn.rollback()
        print(f"Error deleting nieruchomosc: {e}")
        return jsonify({"error": f"Failed to delete nieruchomość: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()




if __name__ == '__main__':
    app.run(debug=True, port=8080)
