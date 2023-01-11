from datetime import timedelta, date
from metrics_persistence import configs
import subprocess

query_string = "CREATE TABLE metrics_{} PARTITION OF metrics FOR VALUES FROM (DATE '{}') TO (DATE '2023-01-09');".format(
	date.today().strftime('%Y%m%d'),
	date.today().strftime('%Y-%m-%d'),
	(date.today() + timedelta(days=1)).strftime('%Y-%m-%d'))

psql_command = "psql -h {} -p {} -d {} -U {} -w -c '{}'".format(
	configs.db["host"],
	configs.db["port"],
	configs.db["database"],
	configs.db["user"],
	query_string
)

shell_command = 'crontab -l | {{ cat; echo "50 23 * * * {}";}}| crontab -'.format(psql_command)

p = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)

print(p.communicate())
