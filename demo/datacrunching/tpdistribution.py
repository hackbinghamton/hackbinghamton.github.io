import csv
from datetime import datetime
import matplotlib.pyplot as plt

#Open the file and set up CSV reader
f = open("tp.csv")
reader = csv.reader(f)
next(reader) #ignore the first row, has column headers

#Read datetimes and lengths (floats) out of the CSV
times = []
lengths = []
for line in reader:
  lengths.append(float(line[3]))
  times.append(datetime.strptime(line[2], "%m/%d/%Y %H:%M:%S"))

#Go through lengths and find where it dropped,
#calculate the gaps in datetime and hold on to them
deltas = []
prev_time = times[0]
prev_length = lengths[0]
for i in range(1, len(times)):
  if lengths[i] < prev_length: #Toilet paper got reloaded
    deltas.append(times[i] - prev_time)
    prev_time = times[i]
  prev_length = lengths[i]


#Now we have a list of timedeltas.
#Convert them into hours and plot a histogram
hours = [d.total_seconds() / 3600 for d in deltas]
plt.hist(hours, bins=15)
plt.show()
