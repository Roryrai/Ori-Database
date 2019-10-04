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

# Test the connection
def testConnect():
    print(query("select version()"))

# Execute a query
def query(sql, params=None):
    try:
        conn = connect()
        cur = conn.cursor()
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        if "insert" in sql or "update" in sql:
            conn.commit()
        if "select" in sql or "returning" in sql:
            return cur.fetchall()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

"""
    sunstone = 1
    healthCells = 2
    learning = 3
    differently = 4
    categories = 5
    techniques = 6
    tricks = 7
"""

def insertQuestions(tournamentId, questionId, answer, participantId):
    questionId = """
        insert into question_responses(
            participant_id,
            question_id,
            response)
        values(%s, %s, %s)
    """
    pass


def insertParticipant(participantParams, runnerParams, volunteerParams):
    mainQuery = """
        insert into participants(display_name,
            discord_name,
            preferred_name,
            pronunciation,
            pronouns,
            interesting_facts,
            timestamp)
        values(%s, %s, %s, %s, %s, %s, %s) returning id
    """

    runnerQuery = """
        insert into runners(participant_id,
            srl_name,
            twitch_name,
            src_name,
            availability_weekday,
            availability_weekend,
            input_method,
            tricks,
            techniques,
            sunstone_method,
            health_cells,
            started_learning,
            unique_strats,
            other_games,
            timezone)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning id
    """

    volunteerQuery = """
        insert into volunteers(
            participant_id,
            restream,
            commentary,
            tracking,
            organizer)
        values(%s, %s, %s, %s, %s) returning id
    """

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(mainQuery, participantParams)
        participantId = cur.fetchone()[0]

        if runnerParams is not None:
            runnerParams = (participantId,) + runnerParams
            cur.execute(runnerQuery, runnerParams)

        if volunteerParams is not None:
            volunteerParams = (participantId,) + volunteerParams
            cur.execute(volunteerQuery, volunteerParams)

        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

if __name__ == "__main__":
    testConnect()