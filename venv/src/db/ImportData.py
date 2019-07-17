import csv
import db



def readFile(file):
    reader = csv.reader(file)
    for row in reader:

        participantParams = None
        runnerParams = None
        volunteerParams = None

        if row[0] == "Timestamp":
            continue
        timestamp = row[0]
        discordName = row[1]
        preferredName = row[2]
        pronunciation = row[3]
        pronouns = row[4]
        displayName = discordName.split("#")[0]
        facts = row[23]

        # Volunteer-specific stuff
        restream = True if row[6] == "Yes" else False
        commentary = True if row[7] == "Yes" else False
        tracking = True if row[8] == "Yes" else False
        organizer = False
        volunteer = restream or commentary or tracking or organizer

        # Runner-specific stuff
        runner = True if row[5] == "Yes" else False
        if runner:
            timezone = row[9]
            weekdayAvailability = row[10]
            weekendAvailability = row[11]
            srcName = row[12]
            twitchName = row[13]
            srlName = row[14]
            inputMethod = row[15]
            tricks = row[16]
            techniques = row[17]
            sunstoneMethod = row[18]
            healthCells = row[19]
            startedLearning = row[20]
            uniqueStrats = row[21]
            otherGames = row[22]

        participantParams = (displayName, discordName, preferredName, pronunciation,
                             pronouns, facts, timestamp,)
        if runner:
            runnerParams = (srlName, twitchName, srcName, weekdayAvailability,
                            weekendAvailability, inputMethod, tricks, techniques,
                            sunstoneMethod, healthCells, startedLearning, uniqueStrats,
                            otherGames, timezone,)
            # runnerParams = (2,) + runnerParams
        if volunteer:
            volunteerParams = (restream, commentary, tracking, organizer,)

        db.insertParticipant(participantParams, runnerParams, volunteerParams)

if __name__ == "__main__":
    file = open("venv/resources/signups.csv", "r", encoding="utf8")
    # print(file.read())
    readFile(file)