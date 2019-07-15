# Database code for the news reporter project

import psycopg2

DBNAME = "news"


def pop_articles():
    """returns the three most popular articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select articles.title, numViews from articles, logPathCount
                 where logPathCount.path = '/article/' || articles.slug
                 order by numViews desc limit 3;""")
    return c.fetchall()
    db.close()


def pop_authors():
    """returns the three most popular authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select name, sum(numViews) as numViews from authorSlugs,
                 logPathCount where logPathCount.path = '/article/' ||
                 authorSlugs.slug group by name order by numViews desc;""")
    return c.fetchall()
    db.close()


def days_with_errors():
    """returns days where more than 1% of request lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select to_char(total.time, 'FMMonth dd, yyyy') as
                 time, (errors.requests * 100.0 / total.requests) as
                 percentError from total, errors where total.time = errors.time
                 and (errors.requests * 100.0 / total.requests) >= 1.0 order by
                 percentError desc;""")
    return c.fetchall()
    db.close()
