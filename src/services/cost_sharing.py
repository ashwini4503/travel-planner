class CostSharingService:
    def __init__(self, firebase_client):
        self.firebase_client = firebase_client

    def get_cost_breakdown(self, itinerary_id):
        return self.firebase_client.get_cost_breakdown(itinerary_id)
