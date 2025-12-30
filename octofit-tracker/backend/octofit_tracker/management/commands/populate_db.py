from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_leader=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc', is_leader=True),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='easy'),
            Workout(name='Running', description='Cardio endurance', difficulty='medium'),
            Workout(name='Deadlift', description='Full body strength', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='pushups', duration=15, calories=100, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='deadlift', duration=45, calories=400, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='run', duration=25, calories=250, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=1000, rank=1)
        Leaderboard.objects.create(team=dc, points=900, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
