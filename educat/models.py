from django.db import models


class Type(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name


class Module(models.Model):
	name = models.CharField(max_length=200, unique=True)
	activity = models.CharField(max_length=200)
	level1 = models.CharField(max_length=200)
	level2 = models.CharField(max_length=200)
	image = models.FileField(upload_to='images/')
	categorie = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name


class Visiteurs(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	ipAdresse = models.CharField(max_length=200)
	temps = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
