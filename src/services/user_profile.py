from ..interfaces.user_interaction import UserInteractionInterface

class UserProfileService(UserInteractionInterface):
    def __init__(self, firebase_client):
        self.firebase_client = firebase_client

    def update_name(self, user_id, name):
        # In a real implementation, you would save this to a database
        pass

    def update_age(self, user_id, age):
        # In a real implementation, you would save this to a database
        pass
