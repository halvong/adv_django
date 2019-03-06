ADV Django
3/05/2019, Tues

https://gitlab.com/jeremytiki/MasterDjangoWebDev
https://docs.djangoproject.com/en/2.2/topics/auth/default/

#db
sudo service postgresql start

su - tom
psql -d advdjango

#settings
python manage.py shell --settings=adv_pycharm.settings.dev

#manage.py
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

#git
Display log graph
git log --graph --decorate --pretty=oneline --abbrev-commit

#checkout remote
1. git fetch
2. git checkout <branch>
3. git checkout -b <branch>

#Squashed
1. Put the to-be-squashed commits on a working branch (if they aren't already) -- use gitk for this
2. Check out the target branch (e.g. 'master')
3. git merge --squash (working branch name)
4. git commit