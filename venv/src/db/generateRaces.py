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

groupSize = 4

def getRunners():
    sql = """select participant_id from runners order by participant_id"""
    result = db.query(sql)
    for id in result:
        participantIds.append(id[0])


def generateQualifiers():
    for raceNumber in range(0, numQualifiers):
        numParticipants = random.randint(minParticipants, maxParticipants)
        entrants = copy.copy(participantIds)
        random.shuffle(entrants)
        entrants = entrants[:numParticipants]
        raceSql = """insert into races(number_entrants) values (%s) returning id"""
        raceParams = (numParticipants,)
        raceId = db.query(raceSql, raceParams)[0][0]
        for id in entrants:
            time = generateTime()
            runnerSql = """insert into race_participants(race_id, participant_id, time)
                            values(%s, %s, %s)"""
            runnerParams = (raceId, id, time,)
            db.query(runnerSql, runnerParams)

def generateTime():
    minutes = random.randint(minMinutes, maxMinutes)
    seconds = random.randint(minSeconds, maxSeconds)
    time = "0:" + str(minutes) + ":" + str(seconds)
    return time

def generateGroupMatches():
    groupIdsQuery = """select distinct group_id from runners order by group_id"""
    groupIds = db.query(groupIdsQuery)

    raceParticipantsQuery = """insert into group_race_participants(race_id, participant_id, time)
                    values(%s, %s, %s)"""
    raceQuery = """insert into races(number_entrants) values(%s) returning id"""

    for groupId in groupIds:
        groupMembers = getRunnersInGroup(groupId[0])
        for i in range(0, len(groupMembers)):
            runner1 = groupMembers[i][0]
            for j in range(i+1, len(groupMembers)):
                runner2 = groupMembers[j][0]
                raceParams = (2,)
                raceId = db.query(raceQuery, raceParams)

                raceParticipantsParams1 = (raceId[0], runner1, generateTime(),)
                raceParticipantsParams2 = (raceId[0], runner2, generateTime(),)
                db.query(raceParticipantsQuery, raceParticipantsParams1)
                db.query(raceParticipantsQuery, raceParticipantsParams2)


def getRunnersInGroup(groupId):
    query = """select participant_id from runners where group_id = %s"""
    params = (groupId,)
    result = db.query(query, params)
    return result


def assignGroups():
    sql = """update runners set group_id = %s where participant_id = %s"""
    numGroups = int(len(participantIds)/groupSize)
    i = 0
    for id in participantIds:
        groupId = i % numGroups + 1
        params = (groupId, id,)
        db.query(sql, params)
        i = i+1

getRunners()
generateGroupMatches()
