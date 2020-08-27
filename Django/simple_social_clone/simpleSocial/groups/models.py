from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template

User = get_user_model()
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slugify = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = '')
    description_html = models.TextField(editble = False, default = '', blank = True)
    members = models.ManyToManyField(User, through = 'GroupMember', on_delete = 'CASCADE')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return rever('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name = 'memberships', on_delete = 'CASCADE')
    user = models.ForeignKey(User, related_name = 'user_groups', on_delete = 'CASCADE')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
