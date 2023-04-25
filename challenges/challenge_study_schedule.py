def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not type(target_time) == int:
        return None
    students = 0
    for start_time, end_time in permanence_period:
        if not (type(start_time) == int and type(end_time) == int):
            return None
        if target_time >= start_time and target_time <= end_time:
            students += 1

    return students
