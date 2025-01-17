import os
import subprocess


def handle_cd_command(arg):
    """Handles a `cd` shell command by calling python's os.chdir."""
    CD_CMD = "cd"
    tokens = arg.split(CD_CMD + " ")
    directory = tokens[-1] if len(tokens) > 1 else None
    if not directory:
        return False, "No folder name was provided."
    try:
        os.chdir(directory)
        subprocess.call(["pwd"])
        return True, None
    except OSError as e:
        return False, e.strerror


def format_uptime(uptime_in_seconds):
    """Format number of seconds into human-readable string.

    :param uptime_in_seconds: The server uptime in seconds.
    :returns: A human-readable string representing the uptime.

    >>> uptime = format_uptime('56892')
    >>> print(uptime)
    15 hours 48 min 12 sec
    """

    m, s = divmod(int(uptime_in_seconds), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    uptime_values = []

    for value, unit in ((d, "days"), (h, "hours"), (m, "min"), (s, "sec")):
        if value == 0 and not uptime_values:
            # Don't include a value/unit if the unit isn't applicable to
            # the uptime. E.g. don't do 0 days 0 hours 1 min 30 sec.
            continue
        elif value == 1 and unit.endswith("s"):
            # Remove the "s" if the unit is singular.
            unit = unit[:-1]
        uptime_values.append("{0} {1}".format(value, unit))

    uptime = " ".join(uptime_values)
    return uptime


def check_if_sqlitedotcommand(command):
    """Does a check if the command supplied is in the list of SQLite dot commands.

    :param command: A command (str) supplied from the user
    :returns: True/False
    """

    sqlite3dotcommands = ['.archive','.auth','.backup','.bail','.binary','.cd','.changes','.check','.clone','.connection','.databases','.dbconfig','.dbinfo','.dump','.echo','.eqp','.excel','.exit','.expert','.explain','.filectrl','.fullschema','.headers','.help','.import','.imposter','.indexes','.limit','.lint','.load','.log','.mode','.nonce','.nullvalue','.once','.open','.output','.parameter','.print','.progress','.prompt','.quit','.read','.recover','.restore','.save','.scanstats','.schema','.selftest','.separator','.session','.sha3sum','.shell','.show','.stats','.system','.tables','.testcase','.testctrl','.timeout','.timer','.trace','.vfsinfo','.vfslist','.vfsname','.width']

    if isinstance(command, str):
        command = command.split(' ', 1)[0].lower()
        return (command in sqlite3dotcommands)
    else:
        return False