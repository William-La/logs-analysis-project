#View Declarations

logPathCount view:

create view logPathCount as select path, count(*) as numViews from log where status = '200 OK'  group by path;

authorSlugs view:

create view authorSlugs as select name, slug from authors, articles where authors.id = articles.author;

total view:

create view total as select time::date, count(*) as requests from log group by time::date;

errors view:

create view errors as select time::date, count(*) as requests from log where status = '404 NOT FOUND' group by time::date;