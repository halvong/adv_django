ADV Django
2/25/2019, mon.


su - tom
psql -d advdjango

#----
0. exec(open('script.py').read())
1. python manage.py startapp polls
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate

----
d = datetime.datetime.now()
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)
d_aware.tzinfo
> <DstTzInfo 'America/Los_Angeles' PST-1 day, 16:00:00 STD>

----
#sample 
>>> pub = datetime.datetime.now()
>>> timezone = pytz.timezone("America/Los_Angeles")
>>> d_aware = timezone.localize(pub)
>>> pub
datetime.datetime(2019, 2, 25, 22, 52, 34, 249900)
>>> q1 = Question(question_text='What is your favorite employer?', pub_date=pub)
>>> c1 = Choice(question=q1, choice_text="Networkofone.com", votes=5)
