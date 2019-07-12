# coding: utf-8
# !/usr/bin/env python3
from reporterdb import pop_articles, pop_authors, days_with_errors


# format for answer to article question
article_ans_format = '''"%s" — %d views\n'''

# format for answer to author question
author_ans_format = '''%s — %d views\n'''

# format for answer to error question
error_ans_format = '''"%s" — %.1f%% errors\n'''


def main():
    """retrieves, formats, and prints the answers for the three
    reporter questions by calling pop_article(), pop_authors(),
    and days_with_errors()."""

    # Answer to"What are the most popular three articles of all time?"
    article_ans = "".join(
        article_ans_format % (title, numViews) for
        title, numViews in pop_articles())
    print("The most popular three articles of all time are:")
    print(article_ans)

    # Answer to "Who are the most popular article authors of all time?"
    author_ans = "".join(
        author_ans_format % (name, numViews) for
        name, numViews in pop_authors())
    print("The most popular authors of all time are:")
    print(author_ans)

    # Answer to "On which days did more than 1% of requests lead to errors?"
    error_ans = "".join(
        error_ans_format % (time, percentError) for
        time, percentError in days_with_errors())
    print("The day(s) where more than 1% of requests were errors were:")
    print(error_ans)


if __name__ == '__main__':
    main()
