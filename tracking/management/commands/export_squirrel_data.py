from django.core.management.base import BaseCommand, CommandError
from tracking.models import Sighting
import pandas as pd


class Command(BaseCommand):
    help = 'Syntax: python manage.py export_squirrel_data path/to/file.csv'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):

        path = options['path'][0]
        sightings = Sighting.objects.all()

        row = {'X':[],
               'Y':[],
               'Unique Squirrel ID': [],
               'Shift':[],
               'Date':[],
               'Age':[],
               'Primary Fur Color': [],
               'Location': [],
               'Specific Location': [],
               'Running': [],
               'Chasing': [],
               'Climbing': [],
               'Eating': [],
               'Foraging': [],
               'Other Activities': [],
               'Kuks': [],
               'Quaas': [],
               'Moans': [],
               'Tail flags': [],
               'Tail twitches': [],
               'Approaches': [],
               'Indifferent': [],
               'Runs from': []
               }

        for s in sightings:
            row['X'].append(s.Latitude)
            row['Y'].append(s.Longitude)
            row['Unique Squirrel ID'].append(s.Unique_Squirrel_ID)
            row['Shift'].append(s.Shift)
            row['Date'].append(s.Date)
            row['Age'].append(s.Age.replace('nan',''))
            row['Primary Fur Color'].append(s.Primary_Fur_Color.replace('nan',''))
            row['Location'].append(s.Location.replace('nan',''))
            row['Specific Location'].append(s.Specific_Location.replace('nan',''))
            row['Running'].append(str(s.Running).upper())
            row['Chasing'].append(str(s.Chasing).upper())
            row['Climbing'].append(str(s.Climbing).upper())
            row['Eating'].append(str(s.Eating).upper())
            row['Foraging'].append(str(s.Foraging).upper())
            row['Other Activities'].append(s.Other_Activities.replace('nan',''))
            row['Kuks'].append(str(s.Kuks).upper())
            row['Quaas'].append(str(s.Quaas).upper())
            row['Moans'].append(str(s.Moans).upper())
            row['Tail flags'].append(str(s.Tail_flags).upper())
            row['Tail twitches'].append(str(s.Tail_twitches).upper())
            row['Approaches'].append(str(s.Approaches).upper())
            row['Indifferent'].append(str(s.Indifferent).upper())
            row['Runs from'].append(str(s.Runs_from).upper())

        df = pd.DataFrame.from_dict(row, orient='columns')
        df.to_csv(path,index=False)
