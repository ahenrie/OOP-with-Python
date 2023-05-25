# list of objects
from csv import reader
from app import App

apps = []

with open('code/advanced/apps.csv') as csv_file:
  csv_reader = reader(csv_file, delimiter=',')
  next(csv_reader)
  for name, description, category in csv_reader:
    apps.append(App(name, description, category))

##################################################
"""
for app in apps:
  app.display()

for i in range(len(apps)):
  apps[i].display()

i = 0
while i < len(apps):
  apps[i].display()
  i += 1
"""

for app in apps:
  if app.category == "social media":
    app.display()
