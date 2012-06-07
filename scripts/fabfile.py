#!/usr/bin/python
from fabric.api import *
import os

env.hosts=['xiaoftang@192.168.245.144']

user='xiaoftang'
package_name='shorturl.tar.gz'

def routes():
    deploy('routes.py')
    
def shorturl():
    deploy('applications/shorturl')

def deploy(path='*'):
    parent=os.path.dirname(os.path.dirname(env.real_fabfile))
    local_path=os.path.join(parent,'app_src')
    remote_path='/data/web2py'
    with lcd(local_path):
        local('rm %s -f'%(package_name))
        local('tar -czf %s %s'%(package_name,path))
        put(package_name,'/tmp/%s'%(package_name))
    with cd(remote_path):
        sudo('tar -xzf /tmp/%s'%(package_name))
        sudo('chown apache:apache %s -R -f'%(remote_path))

def restart_httpd():
    sudo('service httpd restart')

if __name__ == "__main__":
    deploy()