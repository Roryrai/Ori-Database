import psycopg2 as pg

from configparser import ConfigParser
from psycopg2.extras import RealDictCursor

# Config settings for the database connection
def config(filename='venv/resources/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    file = open(filename, "r")
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

# Get a connection to the database
def connect():
    conn = None
    try:
        params = config()
        conn = pg.connect(**params)
        return conn
    except (Exception, pg.DatabaseError) as error:
        print(error)


def insertParticipant(params):
    query = """
        insert into participants(display_name,
        discord_name,
        preferred_name,
        pronunciation,
        pronouns,
        timezone,
        interesting_facts,
        timestamp)
        values (%s, %s, %s, %s, %s, %s, %s, %s) returning id
    """
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(query, params)
        participantId = cur.fetchone()[0]
        conn.commit()
        return participant_id
    except (Exception, pg.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

def insertRunner(params):
    insertParticipant(params)


def insertVolunteer(params):
    insertParticipant()