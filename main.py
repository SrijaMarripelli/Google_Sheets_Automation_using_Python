import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "11-jWbgt8VojyPTxa0ibFWcRZAZRNwUujRdNqpKHI4-w"
sheet = client.open_by_key(sheet_id)

list_of_dicts = sheet.sheet1.get_all_values()

with open('output_file_1.txt', 'w') as file1, open('output_file_2.txt', 'w') as file2:
    for data in list_of_dicts:
        if '' in data:
            file1.write(data[0])
            file2.write(data[0])
        else:
            for i in range(len(data)):
                if i < 2:
                    file1.write(data[i])
                    file1.write("\t")
                else:
                    file2.write(data[i])
                    file2.write("\t")
        file1.write("\n")
        file2.write("\n")
