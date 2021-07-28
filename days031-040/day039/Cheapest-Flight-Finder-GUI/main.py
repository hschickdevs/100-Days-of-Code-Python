import os
# from data_manager import
from flight_search import FlightSearch
from notification_manager import NotificationManager
from windows import MainMenu, DirectReportToplevel, MulticityReportToplevel
from report_generator import generate_direct_report

flight_search_handler = FlightSearch()
notification_handler = NotificationManager(email=os.environ.get("BOT_EMAIL"), password=os.environ.get("BOT_EMAIL_PASSWORD"))


def search_pressed():
    print("searching...")
    tk_data = tkinter_menu.get_tk_entries()

    flight_datasets = []
    search_reports = []
    for (index, flight) in enumerate(tk_data['flights_information']['departure_cities']):
        cheapest_flight_data = flight_search_handler.get_direct_deals(tk_data=tk_data)
        flight_datasets.append(cheapest_flight_data)

        search_report = generate_direct_report(flight_no=index + 1, data=cheapest_flight_data)
        search_reports.append(search_report)

    final_report = ""
    for flight_report in search_reports:
        final_report += flight_report

    with open("search_logs.txt", mode="a") as file:
        file.write(f"\n{final_report}")

    if tk_data['emails']:
        notification_handler.send_mail(to_email=tk_data['to_email'],
                                       message=final_report,
                                       from_city="TEST",
                                       to_city="TEST")

    if len(flight_datasets) == 1:
        # if len(flight_datasets['routes']) > 1 (IT IS A ROUND TRIP)
        print(flight_datasets)
        generated_direct_report_window = DirectReportToplevel(flight_datasets[0])
        generated_direct_report_window.mainloop()
    elif len(flight_datasets) > 1:
        generated_multicity_report_window = MulticityReportToplevel(flight_datasets)
        generated_multicity_report_window.mainloop()
        pass


tkinter_menu = MainMenu(search_func=search_pressed)

tkinter_menu.mainloop()

