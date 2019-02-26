from django.contrib.auth.models import User
from django.views import generic
from polls.models import Question, Choice
import datetime, pytz

timezone = pytz.timezone("America/Los_Angeles")
