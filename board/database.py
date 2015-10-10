from cassandra.cluster import Cluster
from uuid import uuid4

# Set up any necessary database stuff.
cluster = Cluster()
session = cluster.connect()

def db_add_user(username):
    maybe = db_get_user(username)
    if maybe != []:
        return maybe
    ADD_USER = """
        INSERT INTO reactive.users (name, id, score) VALUES ('%s', %s, 0);
    """
    result = session.execute(ADD_USER % (username, str(uuid4())))
    return db_get_user(username)

def db_get_user(username):
    GET_USER = """
        SELECT * FROM reactive.users WHERE name = '%s';
    """
    return session.execute(GET_USER % username)

def db_get_all_users():
    GET_ALL_USERS = """
        SELECT * FROM reactive.users;
    """
    return session.execute(GET_ALL_USERS)
