ADV Django
2/25/2019, mon.


su - tom
psql -d advdjango

#----
1. python manage.py startapp polls
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate