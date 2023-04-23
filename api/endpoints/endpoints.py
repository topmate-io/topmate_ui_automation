def get_booking_status_endpoint(booking_type: str, booking_id: str):
    if booking_type == 'video call' or booking_type == 'webinar':
        return f'/booking-detail/{booking_id}'
    elif booking_type == 'package':
        return f'/package-booking-detail/{booking_id}'
