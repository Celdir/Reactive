from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

CREATE_KEYSPACE = """
CREATE KEYSPACE reactive WITH REPLICATION = {'class' : 'SimpleStrategy',
'replication_factor' : 1};
"""

session.execute(CREATE_KEYSPACE)

CREATE_TABLE_USERS = """
CREATE TABLE reactive.users (
    name text PRIMARY KEY,
    id uuid,
    score int
);
"""

session.execute(CREATE_TABLE_USERS)

CREATE_TABLE_CLANS = """
CREATE TABLE reactive.clans (
    name text PRIMARY KEY,
    id uuid,
    score int
);
"""

session.execute(CREATE_TABLE_CLANS)
