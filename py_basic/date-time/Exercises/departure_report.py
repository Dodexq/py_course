import os
from datetime import datetime

def get_departures():
    os.chdir(os.path.dirname(__file__))
    departures = []
    with open('../data/departure-data.txt') as f:
        for line in f.read().splitlines():
            departure = get_departure(line)
            if departure:
                departures.append(departure)
    return departures

def get_departure(line):
    
    if line[0] == "*":
        return None

    in_list = line.split("\t")
    date_planned = datetime.strptime(in_list[0], '%m/%d/%Y %I:%M %p')
    
    if in_list[1]:
        date_actual = datetime.strptime(in_list[1], '%m/%d/%Y %I:%M %p')
    else:
        date_actual = None
    return (date_planned, date_actual)

def left_ontime(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual == planned

# Write the following four functions. They should
# all return a boolean value
def left_early(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    if actual < planned:
        print('Early:', departure)
    return actual < planned

def left_late(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    if actual > planned:
        return actual > planned

def left_next_day(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual.day > planned.day

def did_not_run(departure):
    actual = departure[1]
    if actual == None:
        return True

def main():
    departures = get_departures()
    ontime_departures = [d for d in departures if left_ontime(d)]
    early_departures = [d for d in departures if left_early(d)]
    late_departures = [d for d in departures if left_late(d)]
    next_day_departures = [d for d in departures if left_next_day(d)]
    cancelled_trips = [d for d in departures if did_not_run(d)]

    print(f"""Total Departures: {len(departures)}
Ontime Departures: {len(ontime_departures)}
Early Departures: {len(early_departures)}
Late Departures: {len(late_departures)}
Next Day Departures: {len(next_day_departures)}
Cancelled Trips: {len(cancelled_trips)}""")

main()