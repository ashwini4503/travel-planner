class BookingPaymentService:
    def __init__(self, emt_client, firebase_client, payment_client):
        self.emt_client = emt_client
        self.firebase_client = firebase_client
        self.payment_client = payment_client

    def book(self, itinerary_id, payment_info):
        booking_confirmation = self.emt_client.book(itinerary_id, payment_info)
        payment_status = self.payment_client.process(payment_info)
        self.firebase_client.save_booking_confirmation(itinerary_id, booking_confirmation)
        return booking_confirmation, payment_status
