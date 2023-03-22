def study_schedule(permanence_period, target_time):
    counter = 0
    for i in range(0, len(permanence_period)):
        entry = permanence_period[i][0]
        depart = permanence_period[i][1]
        if type(entry)!= int or type(depart) != int:
            return None
        if target_time is None:
            return None
        if entry <= target_time <= depart:
            counter += 1
    return counter
