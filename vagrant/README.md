#View Declarations

logPathCount view:

create view logPathCount as select path, count(*) from log where status = '200 OK'  group by path;

authorSlugs view:

create view authorSlugs as select name, slug from authors, articles where authors.id = articles.author;