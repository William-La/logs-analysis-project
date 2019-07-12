# coding: utf-8
from reporterdb import pop_articles, pop_authors, days_with_errors

DBNAME = "news"
# format for answer to article question
article_ans_format = '''"%s" — %d views\n'''

# format for answer to author question
author_ans_format = '''%s — %d views\n'''

# format for answer to error question
error_ans_format = '''"%s" — %d errors\n'''



def main():
    """retrieves, formats, and prints the answers for the three reporter 
    questions by calling popArticle(), popAuthors(), and daysWithErrors()."""

    # Answer to the question "What are the most popular three articles of all time?"
    article_ans = "".join(article_ans_format % (title, numViews) for title, numViews in pop_articles())
    print("The most popular three articles of all time are:")
    print(article_ans)

    # Answer to the question "Who are the most popular article authors of all time?"
    author_ans = "".join(author_ans_format % (name, numViews) for name, numViews in pop_authors())
    print("The most popular authors of all time are:")
    print(author_ans)

    # Answer to the question "On which days did more than 1% of requests lead to errors?"

       

if __name__ == '__main__':
    main()