from Participant import Participant

class Runner(Participant):
    runnerId = None
    srlName = None
    twitchName = None
    srcName = None
    availabilityWeekday = None
    availabilityWeekend = None
    inputMethod = None
    tricks = None
    techniques = None
    sunstoneMethod = None
    healthCells = None
    startedLearning = None
    uniqueStrats = None
    otherGames = None

    def __init__(self, dict):
        self.runnerId = dict["runner_id"] if "runner_id" in dict else None
        self.srlName = dict["srl_name"]
        self.twitchName = dict["twitch_name"]
        self.srcName = dict["src_name"]
        self.availabilityWeekday = dict["availability_weekday"]
        self.availabilityWeekend = dict["availability_weekend"]
        self.inputMethod = dict["input_method"]
        self.tricks = dict["tricks"]
        self.techniques = dict["techniques"]
        self.sunstoneMethod["sunstone_method"]
        self.healthCells = dict["health_cells"]
        self.startedLearning = dict["started_learning"]
        self.uniqueStrats = dict["unique_strats"]
        self.otherGames = dict["other_games"]
        super(Runner, self).__init__(dict["participant_id"] if "participant_id" in dict else None,
                                     dict["display_name"],
                                     dict["discord_name"],
                                     dict["preferred_name"],
                                     dict["pronunciation"],
                                     dict["timezone"],
                                     dict["interesting_facts"],
                                     dict["timestamp"])

