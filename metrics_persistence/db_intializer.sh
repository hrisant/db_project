#!/bin/bash
psql -h pg-1534cab-indarkwedwell39-82be.aivencloud.com -p 19267 -d defaultdb -U avnadmin -w -c "CREATE TABLE metrics (
	  url       text not null,
    logdate   timestamp not null,
    resp_code smallint not null,
    resp_time integer not null,
    has_regex boolean,
	  regex text ,
	PRIMARY KEY (logdate, url)
) PARTITION BY RANGE (logdate);"
