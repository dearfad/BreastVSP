import gspread
from typing import List

def save_to_gspread(data: List[str]) -> None:
    google_credentials = gspread.service_account_from_dict(st.secrets.gspread_credentials)
    spreadsheet = google_credentials.open("breastvsp")
    worksheet = spreadsheet.worksheet("data")
    worksheet.append_row(data)
    return