import firebirdsql
def get_connection():
    con = firebirdsql.connect(
        host='localhost',
        database='nieruchomosci.fdb',
        port=3050,
        user='SYSDBA',
        password='masterkey',
        charset='UTF8'
    )
    return con

def get_agenci():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ID, IMIE, NAZWISKO, NRLICENCJI FROM AGENT")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def create_wlasciciel(imie: str, nazwisko: str) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO WLASCICIEL (IMIE, NAZWISKO)
        VALUES (?, ?) RETURNING ID;
        """
        cursor.execute(query, (imie, nazwisko))
        wlasciciel_id = cursor.fetchone()[0]
        conn.commit()
        return wlasciciel_id
    finally:
        cursor.close()
        conn.close()

def get_all_wlasciciele():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ID, IMIE, NAZWISKO FROM WLASCICIEL")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_wlasciciel_by_id(wlasciciel_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT ID, IMIE, NAZWISKO FROM WLASCICIEL WHERE ID = ?;"
        cursor.execute(query, (wlasciciel_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_wlasciciel(wlasciciel_id: int, imie: str, nazwisko: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = """
        UPDATE WLASCICIEL
        SET IMIE = ?, NAZWISKO = ?
        WHERE ID = ?;
        """
        cursor.execute(query, (imie, nazwisko, wlasciciel_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

def delete_wlasciciel(wlasciciel_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM WLASCICIEL WHERE ID = ?;"
        cursor.execute(query, (wlasciciel_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

# Operacje na nieruchomości
def create_nieruchomosc(wlasciciel_id: int, powierzchnia: int, adres: str, typ_nieruchomosci: str) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO NIERUCHOMOSC (WLASCICIELID, POWIERZCHNIA, ADRES, TYP_NIERUCHOMOSCI)
        VALUES (?, ?, ?, ?) RETURNING ID;
        """
        cursor.execute(query, (wlasciciel_id, powierzchnia, adres, typ_nieruchomosci))
        nieruchomosc_id = cursor.fetchone()[0]
        conn.commit()
        return nieruchomosc_id
    finally:
        cursor.close()
        conn.close()


def add_nieruchomosc(
    typ_nieruchomosci: str,
    wlasciciel_id: int,
    powierzchnia: float,
    adres: str,
    cena: float,
    typ_domu: str = None,
    powierzchnia_dzialki: float = None,
    liczba_pokoi: int = None,
    pietro: int = None,
    liczba_biur: int = None,
    liczba_czlonow: int = None,
    wspolna_sciana: bool = None,
    stan_wykonczenia: str = None,
    basen: bool = None,
    typ_budynku_biurowego: str = None
):
    """
    Calls the stored procedure to add a new property.
    """
    conn = get_connection()  # Function to get the DB connection
    try:
        cursor = conn.cursor()
        query = """
        EXECUTE PROCEDURE AddNieruchomosc (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """
        cursor.execute(query, (
            typ_nieruchomosci,
            wlasciciel_id,
            powierzchnia,
            adres,
            cena,
            typ_domu,
            powierzchnia_dzialki,
            liczba_pokoi,
            pietro,
            liczba_biur,
            liczba_czlonow,
            wspolna_sciana,
            stan_wykonczenia,
            basen,
            typ_budynku_biurowego
        ))
        result = cursor.fetchone()
        conn.commit()
        return {"nieruchomosc_id": result[0], "dom_id": result[1]} if result else None
    except Exception as e:
        print(f"Error executing AddNieruchomosc: {e}")
        raise
    finally:
        cursor.close()
        conn.close()



def get_all_nieruchomosci():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT ID, WLASCICIELID, POWIERZCHNIA, ADRES, TYP_NIERUCHOMOSCI, Cena FROM NIERUCHOMOSC;"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_nieruchomosc_by_id(nieruchomosc_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT ID, WLASCICIELID, POWIERZCHNIA, ADRES, TYP_NIERUCHOMOSCI FROM NIERUCHOMOSC WHERE ID = ?;"
        cursor.execute(query, (nieruchomosc_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_nieruchomosc(nieruchomosc_id: int, wlasciciel_id: int, powierzchnia: int, adres: str, typ_nieruchomosci: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = """
        UPDATE NIERUCHOMOSC
        SET WLASCICIELID = ?, POWIERZCHNIA = ?, ADRES = ?, TYP_NIERUCHOMOSCI = ?
        WHERE ID = ?;
        """
        cursor.execute(query, (wlasciciel_id, powierzchnia, adres, typ_nieruchomosci, nieruchomosc_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

def delete_nieruchomosc(nieruchomosc_id: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM NIERUCHOMOSC WHERE ID = ?;"
        cursor.execute(query, (nieruchomosc_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()