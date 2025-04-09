from djongo import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()

    def __str__(self):
        return self.name
