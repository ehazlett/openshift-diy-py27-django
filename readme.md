Runtime Configuration
======================
This will easily create an Openshift diy-0.1 app with Python 2.7.3 & Django 1.4+ & uWSGI in only 5 commands.

````shell
rhc-create-app -a <app_name> -t diy-0.1
cd app_name
git remote add upstream -m master git://github.com/iepathos/openshift-diy-py27-django.git
git pull -s recursive -X theirs upstream master
git push
````

And watch the scripts do their thing.
