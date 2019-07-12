# coding: utf-8
from reporterdb import popArticles, popAuthors, daysWithErrors

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

       

if __name__ == '__main__':
    main()