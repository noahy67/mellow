import uuid


class UserInfo:
    # userID = 'random_users'
    # loggedIn = 'false'
    # tempID = 'random_users/' + str(uuid.uuid4())
    # tempFileLocs = []
    def __init__(self):
        self.userID = 'random_users'
        self.loggedIn = 'false'
        self.tempID = 'random_users/' + str(uuid.uuid4())
        self.email = 'unknown'
        self.name = 'not logged in'
        self.questions = []
        self.type = 'patient'


    def set_user(self, newuserID):
        self.userID = newuserID

    def set_email(self, email):
        self.email = email

    def set_log_status(self, status):
        self.loggedIn = status

    def get_user(self):
        return self.userID

    def get_log_status(self):
        return self.loggedIn

    def get_temp_id(self):
        return self.tempID

    def set_default(self):
        self.userID = 'random_users'
        self.loggedIn = 'false'
        self.tempID = 'random_users/' + str(uuid.uuid4())
        self.email = 'unknown'
        self.name = 'not logged in'
        self.questions = []
        self.type = 'patient'
