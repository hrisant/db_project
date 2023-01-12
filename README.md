# db_project

Consists of a: 
- metrics_producer module that is basically a website monitor that periodically queries a set of urls(configurable) and sends 
the metrics to a kafka queue
- metrics_persitence module that reads from the queue and persists the mtrics to a database

### Database considerations:
It was designed as a multi - partion table, one partition per day.
It is thus easy to remove old data and maybe with some query magic to optimize reads.
For space efficiency the url and regex fields could have been extracted in a different table,
and leave only the metrics in the metrics table, but it would have a cost at reading.

It is initialized by running db_initializer.sh and then partitions_crontab.py

### Tests:
- are intended to be run with pytest


### Credits:
https://towardsdatascience.com/how-to-build-a-simple-kafka-producer-and-consumer-with-python-a967769c4742
