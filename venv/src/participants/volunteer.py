from particpant import Participant

class Volunteer(Participant):
    volunteerId = None
    restream = False
    commentary = False
    tracking = False
    organizer = False

    def __init__(self, dict):
        self.volunteerId = dict["volunteer_id"] if "volunteer_id" in dict else None
        self.restream = dict["restream"]
        self.commentary = dict["commentary"]
        self.tracking = dict["tracking"]
        self.organizer = dict["organizer"]
        super(Volunteer, self).__init__(dict["participant_id"] if "participant_id" in dict else None,
                                        dict["display_name"],
                                        dict["discord_name"],
                                        dict["preferred_name"],
                                        dict["pronunciation"],
                                        dict["timezone"],
                                        dict["interesting_facts"],
                                        dict["timestamp"])