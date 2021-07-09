from tkinter import *


class GeneratedReport(Tk):
    def __init__(self, report, dates):
        super().__init__()
        self.title("Watchlist Report")
        self.report_label = Label(self, text=self.create_report(report, dates))
        self.report_label.grid(row=0,column=0, padx=20, pady=20)
        self.close_button = Button(self, text="Close", command=self.close_window)
        self.close_button.grid(row=1, column=0)

    def close_window(self):
        self.destroy()

    def create_report(self, report: list, dates: list):
        report_string = f"Generated Report from {dates[0]} to {dates[1]}:\n\n"
        for stock in report:
            report_string += f"${stock['ticker']} {stock['movement']} {str(stock['change'])}%.\n"
        return report_string


class Watchlist(Tk):
    def __init__(self, watchlist):
        super().__init__()
        self.title("Watchlist")
        self.close_button = Button(self, text="Close", command=self.close_window)
        self.close_button.grid(row=1, column=1)
        self.watchlist = Label(self, text=self.get_watchlist(watchlist))
        self.watchlist.grid(row=0, column=1)

    def close_window(self):
        self.destroy()

    def get_watchlist(self, watchlist: list):
        watchlist_string = ""
        for stock in watchlist:
            watchlist_string += f"\n{stock['name']} (${stock['ticker']})\n"
        return watchlist_string
