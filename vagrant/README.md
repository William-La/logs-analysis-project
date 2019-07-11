#View Declarations

logPathCount view:

create view logPathCount as select path, count(*) from log where status = '200 OK'  group by path;