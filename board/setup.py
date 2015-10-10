from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

def create_keyspace():
    CREATE_KEYSPACE = """
    CREATE KEYSPACE reactive WITH REPLICATION = {'class' : 'SimpleStrategy',
    'replication_factor' : 2};
    """
    session.execute(CREATE_KEYSPACE)

def create_table_users():
    CREATE_TABLE_USERS = """
    CREATE TABLE reactive.users (
        name text PRIMARY KEY,
        id uuid,
        score int
    );
    """
    session.execute(CREATE_TABLE_USERS)

def create_table_clans():
    CREATE_TABLE_CLANS = """
    CREATE TABLE reactive.clans (
        name text PRIMARY KEY,
        id uuid,
        score int
    );
    """
    session.execute(CREATE_TABLE_CLANS)

#create_keyspace()
#create_table_users()
#create_table_clans()
