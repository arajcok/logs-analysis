# Logs Analysis
This program runs from the command line. It does not take any input from the user. Instead, it connects to a database, uses SQL queries to analyze the log data, and prints out the answers to some questions.

## Run
#### Download the data
To successfully run this program, the user must have access to a PostgreSQL database in order to load the data and run the database queries. Additionally, a file provided by Udacity called `newsdata.sql` must also be downloaded and executed to create the `news` database and tables. Unfortunately, that file is too large to add to this repository, otherwise I would have done so.

#### Execute the queries
In order to run the program, simply execute `./logs-analysis.py`.

## Output
The query results are displayed in the console when the program is run. An example of the program's output is in `query-results.txt`. 
NOTE: `query-results.txt` is not formatted correctly in Notepad (Notepad has known formatting issues).

## Files
#### logs-analysis.py
This file connects to the `news` database and executes queries to answer three questions: 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
A single query is used, along with joins (both implicit and explicit), to successfully answer each question. The answer to the third question involves two subqueries. Each query result is stored in a variable, which is later looped over to extract the results.

#### query-results.txt
A plain text file that is an example of the program's output.
