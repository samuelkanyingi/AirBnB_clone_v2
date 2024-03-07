#!/usr/bin/python3
"""Compress before sending"""
from datetime import datetime
from fabric.api import local, lcd

def do_pack():
    """Create a .tgz archive"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")
    #with lcd("AirBnB_clone_v2"):
    result = local("tar -czvf {} .".format(archive_path), capture=True)
    if result.failed:
        return None
    return archive_path
