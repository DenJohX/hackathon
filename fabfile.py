from fabric.api import *

import os
HOME = os.path.expanduser("~")

env.key_filename = os.path.join(HOME, '.ssh/id_rsa')
env.hosts = ['denjohx@udkkf97da965.denjohx.koding.io']


def deploy():
    app_dir = '/home/denjohx/www/worldofheroes/app/'
    with cd(app_dir):
        run('git reset --hard')
        run('git pull')

        with prefix('source /etc/bash_completion.d/virtualenvwrapper'):
            with prefix('workon hackathon'):
                run('pip install --upgrade -r requirements.txt')
                run('python manage.py migrate')
                run('python manage.py collectstatic --noinput')
                run('touch hackathon/local_settings.py')
                run('deactivate')