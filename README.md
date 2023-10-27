# EMSI-data-retrieval
Retrieving skill ids and names using EMSI API provided by lightcast.io

Small, simple program to retrieve skills data from a data source made available by Lightcast via an API
auth.py - reads the emsi_creds.txt and uses the credentials provided by EMSI to access the API/data
sample_emsi_creds.txt - is the file containing the credentials that Lightcast/EMSI provided you when you registered at their site for API access. Note that you will have to rename this file as "emsi_creds.txt"
retrieve.py - is the code that will execute the API and then place all the data in a CSV file that can be opened by EXCEL.
skills-database-json-layout.xlsx - is the file that EMSI provides as a guide to the fields that are available. However, only a handlful (half a dozen as of 10/27/2023) are truly available.
The code however accounts for all the fields and so when EMSI makes the fields available, one can modify the code easily to obtain the added fields.
