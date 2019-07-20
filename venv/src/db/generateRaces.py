import db
import random
import copy

minMinutes = 28
maxMinutes = 45
minSeconds = 0
maxSeconds = 59
numQualifiers = 21
minParticipants = 6
maxParticipants = 22

participantIds = []

def getRunners():
    sql = """select participant_id from runners order by participant_id"""
    result = db.query(sql)
    for id in result:
        participantIds.append(id[0])
    print(participantIds)


def generateQualifiers():
    for raceNumber in range(0, numQualifiers):
        numParticipants = random.randint(minParticipants, maxParticipants)
        entrants = copy.copy(participantIds)
        random.shuffle(entrants)
        entrants = entrants[:numParticipants]
        print(entrants)
        raceSql = """insert into races(number_entrants) values (%s) returning id"""
        raceParams = (numParticipants,)
        raceId = db.query(raceSql, raceParams)[0][0]
        for id in entrants:
            minutes = random.randint(minMinutes, maxMinutes)
            seconds = random.randint(minSeconds, maxSeconds)
            time = "0:" + str(minutes) + ":" + str(seconds)
            runnerSql = """insert into race_participants(race_id, participant_id, time)
                            values(%s, %s, %s)"""
            runnerParams = (raceId, id, time,)
            db.query(runnerSql, runnerParams)

getRunners()
generateQualifiers()

