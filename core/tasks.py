from celery.task import periodic_task
from celery.schedules import crontab

from core.models import Post


@periodic_task(run_every=crontab(minute=59, hour='23'))
def reset_post_votes():
    print('my_task')
    Post.objects.all().update(amount_of_votes=0)
