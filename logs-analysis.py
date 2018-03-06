#!/usr/bin/python3

import psycopg2

db = psycopg2.connect("dbname=news")

# Cursor to execute SQL statements
cursor = db.cursor()


# Most popular three articles
cursor.execute("""select title, count(*) as views
               from articles, log
               where path like '%' || slug
               group by title
               order by views desc
               limit 3""")
popular_articles = cursor.fetchall()
print("Query 1 executed...")


# Most popular article authors
cursor.execute("""select name, count(*) as views
               from articles inner join log
               on path like '%' || slug
               inner join authors
               on articles.author = authors.id
               group by name
               order by views desc""")
popular_authors = cursor.fetchall()
print("Query 2 executed...")


# Days when > 1% of requests were errors
cursor.execute("""select errors.date, (errorRequests/requests::float)*100 as errorPercent
               from (select time::date as date, count(*) as errorRequests
                    from log
                    where status != '200 OK'
                    group by date) as errors,
                    (select time::date as date, count(*) as requests
                    from log
                    group by date) as totals
               where errors.date = totals.date
               group by errors.date, errorPercent
               having (errorRequests/requests::float)*100 > 1""")
error_request_days = cursor.fetchall()
print("Query 3 executed...\n\n")


db.close()


# Output
print("QUERY RESULTS")
print("\nPopular articles:")
for title, views in popular_articles:
    print("{0} -- {1} views".format(title, views))

print("\nPopular authors:")
for name, views in popular_authors:
    print("{0:22} -- {1:<6} views".format(name, views))

print("\nDays when more than 1% of requests were errors:")
for date, error_percent in error_request_days:
    # Format date: month day, year
    print(date.strftime("%B %d, %Y"), "--",
          "{0:0.2f}% errors\n".format(error_percent))
