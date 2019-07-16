# Database code for the news reporter project

import psycopg2

DBNAME = "news"


def pop_articles():
    """return the three most popular articles of all time."""
    query = """SELECT articles.title, numViews
                FROM articles, logPathCount
                WHERE logPathCount.path = '/article/' || articles.slug
                ORDER BY numViews DESC
                LIMIT 3;"""
    return database_helper(query)


def pop_authors():
    """return the three most popular authors of all time."""
    query = """SELECT name, sum(numViews) AS numViews
                FROM authorSlugs, logPathCount
                WHERE logPathCount.path = '/article/' || authorSlugs.slug
                GROUP BY name
                ORDER BY numViews DESC;"""
    return database_helper(query)


def days_with_errors():
    """return days where more than 1% of request lead to errors."""
    query = """SELECT to_char(total.time, 'FMMonth dd, yyyy') AS time,
                    (errors.requests * 100.0 / total.requests) as percentError
                FROM total, errors
                WHERE total.time = errors.time
                AND (errors.requests * 100.0 / total.requests) >= 1.0
                ORDER BY percentError DESC;"""
    return database_helper(query)


def database_helper(query):
    """take in a SQL query, establishe a connection to the news
    database, execute the query, and return the results
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results
