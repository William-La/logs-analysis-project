# news reporter log analysis project

news reporter logs analysis project analyzes the data in the "news" PostgreSQL database, which is a mock database modeled for a news website, provided by Udacity as part of the Full Stack Web Developer nanodegree course. The reporter then provides answers to the following questions:

1. "What are the most popular three articles of all time?"
2. "Who are the most popular article authors of all time?"
3. "On which days did more than 1% of requests lead to errors?"

Set up
------

This project requires a linux server to be able to analyze the "news" SQL database. Using VirtualBox and Vagrant will allow us to run that linux server on a virtual machine. For more information on the required set up, software, and files for this project, please visit [this Udacity github page](https://github.com/udacity/fullstack-nanodegree-vm). 

[The "news" database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from Udacity's Full Stack Web Developer nanodegree is also required. Once the data is downloaded, unzip the file and then place the `.sql` file in the vagrant directory. To load the data, you must have the virtual machine online and be logged in with the commands:

```terminal
vagrant up
vagrant ssh
```

Next, run the following terminal command while in the /vagrant directory.

```terminal
psql -d news -f newsdata.sql
```

After the required software and files have been set up, you can then create the views used in this project. Please view the "View Declarations" section below.

View Declarations
------------------

To create these views, you must be in the psql news envinroment before using the create commands. To enter the environment enter the following command into your virtual machine while in the /vagrant directory.

```terminal
psql news
```

#### logPathCount view:

Counts the number of successful requests to a specific paths.
```sql
CREATE VIEW logPathCount AS
SELECT path, count(*) AS numViews
FROM log
WHERE status = '200 OK'
GROUP BY path;
```

#### authorSlugs view:

Pairs the authors' names with the slugs of their articles. 
```sql
CREATE VIEW authorSlugs AS
SELECT name, slug
FROM authors, articles
WHERE authors.id = articles.author;
```

#### total view:

Counts the number of requests made on a specific date.
```sql
CREATE VIEW total AS
SELECT time::date, count(*) AS requests
FROM log
GROUP BY time::date;
```

#### errors view:

Counts the number of error requests on a specific date.
```sql
CREATE VIEW errors AS
SELECT time::date, count(*) AS requests
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY time::date;
```

Usage
------

To use the news reporter tool, run the following command in the /vagrant directory of your virtual machine.

```terminal
python reporter.py
```

The news reporter will then print out the top three articles, the top authors, and the days where atleast 1% of requests were errors into your terminal. To see the expected output, please view the output.txt file.

Program Design
---------------

When the reporter.py file is run, it retrieves information from the three reporterdb.py methods, formats the answers, and then prints the answers. The methods in the reporterdb.py file obtain the information required to answer the reporter's questions by connecting to the "news" database, creating a cursor, running a sql query specific to each question, and returning the output to the queries. 