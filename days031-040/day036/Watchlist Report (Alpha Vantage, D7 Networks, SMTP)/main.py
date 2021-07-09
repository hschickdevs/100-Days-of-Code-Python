from news_client import get_news
from stock_client import get_stock_data
from alerts_client import create_message, send_email, send_sms
from toplevels import Watchlist, GeneratedReport
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# NOTE: FREE ALPHA VANTAGE LICENSE ONLY ALLOWS 5 STOCKS TO BE CALLED AT ONE TIME!

email = "YOUR_EMAIL"
email_password = "YOUR_EMAIL_PASSWORD"
RECIPIENT_EMAIL = "RECIPIENT_EMAIL"

watchlist_df = pd.read_csv("watchlist_data/watchlist.csv")

WATCHLIST = watchlist_df.to_dict(orient="records")
print(WATCHLIST)


THEME_COLOR = "#FAF1E6"
FONT = ("Helvetica Neue", 18, "normal")
window = tk.Tk()
window.title("Watchlist Scanner")
window.minsize(width=250, height=150)
window.config(bg=THEME_COLOR, padx=25, pady=25)


def generate_report():
    report_list = []
    key_errors = []
    generate_report_button.config(state="disabled")
    for stock in WATCHLIST:
        ticker = stock['ticker']
        company_name = stock['name']
        try:
            stock_data = get_stock_data(ticker)
            movement = stock_data[0]
            percent_change = stock_data[1]
            get_headlines = stock_data[2]
            dates = [stock_data[3][0], stock_data[3][1]]
            report_list.append({'ticker': ticker, "change": percent_change, "movement": movement})
        except KeyError:
            get_headlines = False
            key_errors.append(ticker)

        if get_headlines:
            print(f"\nAttempting to get news for {ticker}...\n")
            # Get the top 5 headline news articles
            print(f"Article Posting Dates: {dates}\n")
            articles = get_news(company_name, dates)

            # Create the message
            message = create_message(ticker, articles, percent_change, movement)
            print(message)

            # Send alerts to sms/email (sms credits low)
            # send_sms(message)
            if emails_checked_state.get() > 0:
                encoded_message = message.encode("ascii", errors="ignore")
                decoded_message = encoded_message.decode("utf-8", "ignore")
                send_email(from_email=email, from_password=email_password, to_email=RECIPIENT_EMAIL,
                           message=decoded_message, ticker_symbol=ticker)
            else:
                print("Email notification checkbox unchecked. ")
        else:
            print(f"${ticker} has not had a significant move.")
    GeneratedReport(report_list, dates)
    generate_report_button.config(state="normal")
    if len(key_errors) > 0:
        system_status_label.config(text=f"Raised Key Errors for: {key_errors}")
    else:
        system_status_label.config(text=f"Successfully generated report ({dates[0]} to {dates[1]}).")


def open_watchlist():
    watchlist = Watchlist(WATCHLIST)
    watchlist.mainloop()


def update_watchlist():
    ticker_added = ticker_symbol_entry.get()
    company_name_added = company_name_entry.get()
    if messagebox.askokcancel("Is the information correct?",
                              f"Add to Watchlist:\n\nCompany: {company_name_added}\nTicker Symbol: ${ticker_added}"):

        # Add to watchlist and update CSV
        WATCHLIST.append({'ticker': ticker_added, 'name': company_name_added})
        watchlist_dataframe = pd.DataFrame(data=WATCHLIST)
        watchlist_dataframe.to_csv("watchlist_data/watchlist.csv", index=False)

        ticker_symbol_entry.delete(0, tk.END)
        company_name_entry.delete(0, tk.END)
        system_status_label.config(text=f"Successfully added ${ticker_added} to watchlist.")
    else:
        system_status_label.config(text=f"Successfully cancelled watchlist update.")


# Main menu buttons:
add_to_watchlist_image = tk.PhotoImage(file="image_assets/addtowatchlist.png")
generate_report_image = tk.PhotoImage(file="image_assets/generatereport.png")
view_watchlist_image = tk.PhotoImage(file="image_assets/viewwatchlist.png")

generate_report_button = tk.Button(image=generate_report_image, text="Search", command=generate_report, bg=THEME_COLOR,
                                   highlightthickness=0, bd=0, pady=0, padx=0)
generate_report_button.grid(row=4, column=0, columnspan=2, pady=5)
view_watchlist_button = tk.Button(text="Watchlist", command=open_watchlist, image=view_watchlist_image, bg=THEME_COLOR,
                                  highlightthickness=0, bd=0)
view_watchlist_button.grid(row=3, column=0, columnspan=2, pady=5)
add_to_watchlist_button = tk.Button(image=add_to_watchlist_image, bg=THEME_COLOR, highlightthickness=0, bd=0,
                                    command=update_watchlist)
add_to_watchlist_button.grid(row=2, column=0, columnspan=2, pady=5)

# Entries:
ticker_symbol_entry = tk.Entry(window, width=25, bg="#DEEDF0", highlightthickness=0, relief="groove")
ticker_symbol_entry.grid(row=0, column=0, pady=5, padx=2.5)
company_name_entry = tk.Entry(window, width=25, bg="#DEEDF0", highlightthickness=0, relief="groove")
company_name_entry.grid(row=0, column=1, pady=5, padx=2.5)

# Labels:
ticker_symbol_entry_label = tk.Label(text="Enter Ticker Symbol", font=FONT, bg=THEME_COLOR)
ticker_symbol_entry_label.grid(row=1, column=0, sticky="n")
company_name_entry_label = tk.Label(text="Enter Company Name", font=FONT, bg=THEME_COLOR)
company_name_entry_label.grid(row=1, column=1, sticky="n")
system_status_label = tk.Label(text="", font=FONT, bg=THEME_COLOR)
system_status_label.grid(row=5, column=0, columnspan=2, pady=5)

# Checkbuttons:
emails_checked_state = tk.IntVar()
email_checkbutton = tk.Checkbutton(master=window, text="Email Alerts", variable=emails_checked_state, font=FONT,
                                   bg=THEME_COLOR)
email_checkbutton.grid(row=6, column=0, pady=5)
sms_checked_state = tk.IntVar()
sms_checkbutton = tk.Checkbutton(master=window, text="SMS Alerts", variable=sms_checked_state, font=FONT,
                                 bg=THEME_COLOR)
sms_checkbutton.grid(row=6, column=1, pady=5)

window.mainloop()
