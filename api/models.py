from django.db import models


class Info(models.Model):
    slack_name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    github_file_url = models.URLField()
    github_source_code_url = models.URLField()
