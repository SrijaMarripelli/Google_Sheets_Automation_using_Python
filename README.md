# Google_Sheets_Automation_using_Python
This project automates tasks that could be done in Google Sheets using Python and Google Sheets API. It also integrates efficient data management and writing the data into text files in the desired format.


### Prerequisites for this Project
1) Latest version of Python (version > 3.8)
2) Google Cloud Account to enable Google Sheets API to the project
3) Google Sheet Data
4) A Code Editor

### Step-1: Google Cloud Setup
1) Go to https://console.cloud.google.com
2) Make sure you are on the right google account, if not click on top right corner to change the account
3) Click on "NEW PROJECT" beside the Google Cloud logo on the top
4) Create a new project and click on the new project
5) Go to "APIs and Services" in the navigation menu and click on "ENABLE APIS AND SERVICES"
6) Enable "Google Sheets API"

### Step-2: Generating a Service Account
1) In the Google Sheets API page, click on "CREATE CREDENTIALS"
2) Select "Google Sheets API" in the dropdown for "Select an API" query
3) Select "Application data" for "What data will you be accessing?"
4) For creating a service account, enter any service account name and grant "Editor" role. Click on "DONE"
5) Copy the service account mail address from the service account details
6) In the keys section, click on "ADD KEY" and then create a private key for the service account by clicking an "JSON" key. Click on "CREATE"
7) Download the JSON file to the same folder that we are going to use to create the scripts for automation

### Step-3: Python Setup
1) Rename the JSON file to "credentials.json"
2) Go to Google Sheets to create a new file and share it with the email address you have copied earlier
3) For connecting the google sheets, use the terminal in the VS Code Editor
4) Create a virtual environment by typing the following command:

   `python -m venv sheets`
5) Set the execution policy to "Unrestricted" by typing the following command:

   `Set-ExecutionPolicy -Scope CurrentUser`
7) Enter the ExecutionPolicy as "Unrestricted" when prompted:

   `cmdlet Set-ExecutionPolicy at command pipeline position 1
    Supply values for the following parameters:
    ExecutionPolicy: Unrestricted`
   
**_IMPORTANT!!!_ Do not forget to change the execution policy back to "Restricted" when there are no more scripts**
9) For Windows type:
   `sheets\Scripts\Activate.ps1`
   For Mac/Linux type:
   `./sheets/bin/activate`
10) Install the necessary modules:

    pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthib gspread
11) Write python automation script as mentioned in 'main.py'
