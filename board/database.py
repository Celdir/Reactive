from cassandra.cluster import Cluster
from uuid import uuid4

# Set up any necessary database stuff.
cluster = Cluster()
session = cluster.connect()

# User-Oriented Database Interactions

def add_user(username):
    # verify that the user doesn't exist already
    user = get_user(username)
    if user != []:
        return []
    # otherwise, go ahead and add the user
    ADD_USER = """
        INSERT INTO reactive.users (name, id, score) VALUES ('%s', %s, 0);
    """
    session.execute(ADD_USER % (username, str(uuid4())))
    # return the user because yes
    return get_user(username)

def get_user(username):
    GET_USER = """
        SELECT * FROM reactive.users WHERE name = '%s';
    """
    result = session.execute(GET_USER % username)
    if result == []:
        return []
    else:
        # we just want the first user result - there should only be one
        return result[0]

def get_all_users():
    GET_ALL_USERS = """
        SELECT * FROM reactive.users;
    """
    return session.execute(GET_ALL_USERS)

# Clan-Oriented Database Interactions

def add_clan(clanname):
    # verify that the clan doesn't exist already
    clan = get_clan(clanname)
    if clan != []:
        return []
    # otherwise, go ahead and add the clan
    ADD_CLAN = """
        INSERT INTO reactive.clans (name, id, score) VALUES ('%s', %s, 0);
    """
    session.execute(ADD_CLAN % (clanname, str(uuid4())))
    # return the clan because yes
    return get_clan(clanname)

def get_clan(clanname):
    GET_CLAN = """
        SELECT * FROM reactive.clans WHERE name = '%s';
    """
    result = session.execute(GET_CLAN % clanname)
    if result == []:
        return []
    else:
        # we just want the first clan result - there should only be one
        return result[0]

def get_all_clans():
    GET_ALL_CLANS = """
        SELECT * FROM reactive.clans;
    """
    return session.execute(GET_ALL_CLANS)

# Awarding Points

def award_user_points(username, points):
    user = get_user(username)
    if user == []:
        return []
    AWARD_USER_POINTS = """
        INSERT INTO reactive.users (name, id, score) VALUES ('%s', %s, %d);
    """
    session.execute(AWARD_USER_POINTS % (user.name, user.id, user.score + points))
    return get_user(username)

def award_clan_points(clanname, points):
    clan = get_clan(clanname)
    if clan == []:
        return []
    AWARD_clan_POINTS = """
        INSERT INTO reactive.clans (name, id, score) VALUES ('%s', %s, %d);
    """
    session.execute(AWARD_clan_POINTS % (clan.name, clan.id, clan.score + points))
    return get_clan(clanname)

# Utility Methods

def clear_all_records():
    CLEAR_ALL_RECORDS = """
        TRUNCATE reactive.users;
    """
    return session.execute(CLEAR_ALL_RECORDS)
