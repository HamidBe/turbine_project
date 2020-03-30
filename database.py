import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import  NamedTupleCursor

def create_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",
                                dbname="carto_db",
                                user="carto",
                                password="carto_pwd",
                                port=5432)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    except Exception as inst:
        print("I am unable to connect to the database")
        print(inst)

    return conn

def create_tables(conn) -> None:
    requete = """CREATE TABLE IF NOT EXISTS nom_des_voies (
        voie_id serial, 
        voie_complet varchar(250), 
        voie_fantoir varchar(10), 
        voie_date_cre  varchar(10),
        voie_real varchar(15),
        voie_officiel varchar(15),
        tenant varchar(250),
        aboutissant varchar(250),
        denom_annee varchar(15),
        dm_seance varchar(10),
        delib_num varchar(15),
        cote_archives varchar(20),
        denom_origine varchar(350), 
        lien_externe varchar(350),
        observation varchar(300),
        geojson varchar(5000),
        genre varchar(5));"""

    query_create_select(conn, requete)

def query_create_select(conn, requete):
    cur = conn.cursor()
    print(requete)
    cur.execute(requete)
    return cur

def query_dict(conn, requete, data_dict):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(requete, data_dict)
    return cur

if __name__ == "__main__":
    with create_connection() as conn:
        try:
            create_tables(conn)
        except Exception as e:
            print(e)
        finally:
            conn.commit()