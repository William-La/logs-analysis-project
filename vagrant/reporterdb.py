# coding: utf-8
# Database code for the news reporter project

import psycopg2

DBNAME = "news"
# format for answer to article question
artAnsFormat = '''"%s" — %d views\n'''

# format for answer to author question
autAnsFormat = '''%s — %d views\n'''

# format for answer to error question
errAnsFormat = '''"%s" — %d errors\n'''




def main():
    """retrieves, formats, and prints the answers for the three reporter questions by 
    calling popArticle(), popAuthors(), and daysWithErrors()."""

    # Answer to the question "What are the most popular three articles of all time?"
    artAns = "".join(artAnsFormat % (title, numViews) for title, numViews in popArticles())
    print("The most popular three articles of all time are:")
    print(artAns)

    # Answer to the question "Who are the most popular article authors of all time?"
    autAns = "".join(autAnsFormat % (name, numViews) for name, numViews in popAuthors())
    print("The most popular authors of all time are:")
    print(autAns)

    # Answer to the question "On which days did more than 1% of requests lead to errors?"

def popArticles():
    """returns the three most popular articles of all time"""
    db = psycopg2.connect(database= DBNAME)
    c = db.cursor()
    c.execute("select articles.title, numViews from articles, logPathCount where logPathCount.path = '/article/' || articles.slug order by numViews desc limit 3;")
    return c.fetchall()
    db.close()
    
def popAuthors():
    """returns the three most popular authors of all time"""
    db = psycopg2.connect(database= DBNAME)
    c = db.cursor()
    c.execute("select name, sum(numViews) as numViews from authorSlugs, logPathCount where logPathCount.path = '/article/' || authorSlugs.slug group by name order by numViews desc;")
    return c.fetchall()
    db.close()
    
def daysWithErrors():
    """returns the days where more than one percent of request lead to errors"""
    db = psycopg2.connect(database= DBNAME)
    c = db.cursor()

if __name__ == '__main__':
    main()