class ItineraryGenerator:
    def __init__(self, ai_client, maps_api_key, bigquery_client, firebase_client):
        self.ai_client = ai_client
        self.maps_api_key = maps_api_key
        self.bigquery_client = bigquery_client
        self.firebase_client = firebase_client
