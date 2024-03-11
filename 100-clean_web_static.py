#!/usr/bin/python3

#Fabric script that deletes out-of-date archives
from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['<34.207.221.205>', '<54.145.241.21']
env.user = 'ubuntu' 



def do_clean(number=0):
    """
    Deletes all unnecessary archives on both web servers
    """
    try:
        number = int(number)
    except ValueError:
        return
    if number < 0:
        return

    number = number if number > 1 else 1

    with cd('/data/web_static/releases'):
        archives = run('ls -1tr').split('\n')

        archives_to_keep = archives[-number:]

        for archive in archives:
            if archive not in archives_to_keep:
                run('rm -f {}'.format(archive))

    with cd('/versions'):
        archives = run('ls -1tr').split('\n')

        archives_to_keep = archives[-number:]

        for archive in archives:
            if archive not in archives_to_keep:
                run('rm -f {}'.format(archive))

