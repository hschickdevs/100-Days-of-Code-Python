from datetime import datetime

now = datetime.now()


def generate_direct_report(flight_no, data: dict):
    from_city = data['cityFrom']
    from_airport = data['flyFrom']
    to_city = data['cityTo']
    to_airport = data['flyTo']
    price = data['price']
    url = data['deep_link']
    flight_availability = data['availability']['seats']
    flights_in_route = data['route']

    comp_a = f"Flight {flight_no} Report:"
    if len(flights_in_route) > 1:
        comp_b = "\n\nConnecting Flights Information: "
        for (index, flight) in enumerate(flights_in_route):
            comp_b += f"\nFlight {index + 1}: From {flight['flyFrom']} in {flight['cityFrom']} to {flight['flyTo']} in {flight['cityTo']} on {flight['local_departure'][:10]}"
    else:
        comp_b = f"\n\nDirect Flight Information:\nFlight from {from_airport} in {from_city} to {to_airport} in {to_city} on {data['local_departure'][:10]}."
    comp_c = f"\n\nTrip Ticket Cost: ${price}"
    comp_d = f"\nTrip Availability: {flight_availability} seats remaining."
    comp_e = f"\n\nBook this flight now:\n{url}\n\n\n "
    report = comp_a + comp_b + comp_c + comp_d + comp_e

    return report
