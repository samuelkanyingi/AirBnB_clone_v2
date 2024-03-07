#!/usr/bin/python3
"""Deploy archive to web servers"""
from fabric.api import env, put, run
import os

env.hosts = ['34.207.221.205', '54.145.241.21']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, "/tmp/")

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension> on the web servers
        archive_filename = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_filename)[0]
        releases_path = "/data/web_static/releases/"
        run("mkdir -p {}{}/".format(releases_path, archive_name_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(archive_filename, releases_path, archive_name_no_ext))

        # Delete the archive from the web servers
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web servers
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run("ln -s {}{}/ /data/web_static/current".format(releases_path, archive_name_no_ext))

        return True

    except Exception as e:
        print(e)
        return False
