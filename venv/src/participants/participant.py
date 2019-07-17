class Participant:
    participantId = None
    displayName = None
    discordId = None
    preferredName = None
    pronunciation = None
    pronouns = None
    timezone = None
    facts = None
    timestamp = None

    def __init__(self, participantId, displayName, discordId, preferredName, pronunciation, pronouns, timezone, facts, timestamp):
        self.participantId = participantId
        self.displayName = displayName
        self.discordId = discordId
        self.preferredName = preferredName
        self.pronunciation = pronunciation
        self.pronouns = pronouns
        self.timezone = timezone
        self.facts = facts
        self.timestamp = timestamp

