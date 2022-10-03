# def my_cron_job():
#     print("this is my first cron")

# from django_cron import CronJobBase, Schedule

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1
#     RETRY_AFTER_FAILURE_MINS = 1
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
#     code='ns_app.my_cron_job'
#     def do(self):
#         print("cron new")