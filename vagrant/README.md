#View Declarations

logPathCount view:

create view logPathCount as select path, count(*) from log group by path;