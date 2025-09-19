class TestingFeedbackService:
    def __init__(self, firebase_client, bigquery_client):
        self.firebase_client = firebase_client
        self.bigquery_client = bigquery_client

    def collect_feedback(self, user_id, feedback):
        self.firebase_client.save_feedback(user_id, feedback)
