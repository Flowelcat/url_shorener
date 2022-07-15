from django.contrib.sessions.models import Session
from django.db import models

from web.utils import encode_base62


class URL(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.CharField(max_length=1024, null=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, db_column="session_key")
    clicks = models.IntegerField(default=0, null=False)
    create_date = models.DateField(auto_now_add=True)

    @property
    def url_slug(self):
        return encode_base62(self.id)
