 

View Declarations
------------------
####logPathCount view:

Counts the number of successful requests to a specific paths.
```sql
create view logPathCount as select path, count(*) as numViews from log where status = '200 OK'  group by path;
```

####authorSlugs view:

Pairs the authors' names with the slugs of their articles. 
```sql
create view authorSlugs as select name, slug from authors, articles where authors.id = articles.author;
```

####total view:

Counts the number of requests made on a specific date.
```sql
create view total as select time::date, count(*) as requests from log group by time::date;
```

####errors view:

Counts the number of error requests on a specific date.
```sql
create view errors as select time::date, count(*) as requests from log where status = '404 NOT FOUND' group by time::date;
```