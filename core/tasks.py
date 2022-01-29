from turtle import position
from celery.task import periodic_task
from celery.schedules import crontab

from core.models import Post


@periodic_task(run_every=crontab(minute=59, hour='23'))
def reset_post_votes():
    print('my_task')
    posts = Post.objects.all()
    for post in posts:
        post.amount_of_votes=0
        post.voted_by.clear()
        post.save()