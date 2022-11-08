import json
import os

basePath = "Hazen Robotics Slack export Apr 1 2020 - Nov 7 2022"
search = "ok"
channels = os.scandir(basePath)
for channel in channels:
    if not".json" in channel.name:
        days = os.scandir(basePath+"/"+channel.name)
            for day in days:/""
                print(basePath + "/" + channel.name + "/" + day.name)
                file = open(basePath + "/" + channel.name + "/" + day.name)
                jsonDay = json.load(file)
                file.close()
                for line in jsonDay:
                    if search in line:
                        print(line['text'])
