from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from math import trunc
from time import time
# Create your models here.

def gen_slug(place, ph):

	length_of_slug = 30

	rep_number = [ i for i in range(length_of_slug) ]
	j = 0
	for i in place:
		rep_number[j] += ord(i)
		j = (j + 1) % length_of_slug

	multiplier = trunc(ph) * int(time())
	delim = ord('z') - ord('A')

	for i in range(length_of_slug):
		rep_number[i] *= multiplier + 1
		rep_number[i] = chr(ord('A') + rep_number[i] % delim)

	rep_number = ''.join(rep_number)

	return slugify(rep_number, allow_unicode=True)

class Report(models.Model):

	date = models.DateField(auto_now_add=False)
	place = models.CharField(max_length=50, default='Altay Kray, Salt lake')
	ph = models.FloatField(default='0.0');
	comment = models.CharField(max_length=100, default='Your note')
	slug = models.SlugField(max_length=150, unique=True)


	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.place, self.ph)
			super().save(*args, **kwargs)

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse('report_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('edit_report', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('delete_report', kwargs={'slug': self.slug})
