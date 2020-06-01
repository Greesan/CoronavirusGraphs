# CoronavirusGraphs
Learning how to webscrape using BeautifulSoup and Selenium, and using google sheets api to provide data-logging and graphing capabilities. Hopefully going to completely automate this to update the graph on a common schedule. This gives me a bit more info into how services like IFTTT provides similar programs (https://ifttt.com/applets/NFRkZeJu-automatically-create-a-discover-weekly-archive)

StatUpdater: single run code, operates immediately

AutoStatUpdater: automated at 4:50, requires the python script to be running in background.

AutoStatUpdater: trying to automate with Windows Task Scheduler to remove the requirement of the python script running in background indefinitely.

This is how the current output looks like:

_Console Output:_

![Console Output](/corconsole.PNG)

_Google Sheets Output:_
![Data as of 5/31/2020](/corgraphs.PNG)
Steps to reimplement yourself:

1. Create a google apis project + service account, enable sheets and drive api.
1. Create the google sheet with headers, share with service account with edit access 
1. Change AutoStatUpdater.py line 22: creds=ServiceAccountCredentials.from_json_keyfile_name('YourJsonName.json', scope)
1. Change AutoStatUpdater.py line 25: self.sheet = client.open('YourGoogleSheetsName').sheet1
1. Run the AutoStatUpdater.py

Same instructionss for <StatUpdater,AutoStatUpdater,AutoStatUpdater2>, but change the file that you make edits to.

Resources Used:
https://www.youtube.com/watch?v=x2r_RmvfzRo -> LucidProgramming
https://www.youtube.com/watch?v=zF_DroDICaM -> JCharisTech & J-Secur1ty

