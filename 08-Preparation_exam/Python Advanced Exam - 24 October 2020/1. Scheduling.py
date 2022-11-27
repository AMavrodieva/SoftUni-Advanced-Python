jobs = [int(x) for x in input().split(", ")]
index_of_job = int(input())
cycle = 0
line = jobs
while True:
    min_number = min(line)
    min_value_index = [ind for ind, value in enumerate(jobs) if value == min_number]
    if len(min_value_index) > 1 and index_of_job in min_value_index:
        match = min_value_index.index(index_of_job)
        cycle += (match+1) * min_number
        break
    elif len(min_value_index) > 1:
        cycle += (len(min_value_index) * min_number)
    else:
        ind_min_number = jobs.index(min_number)
        cycle += min_number
        if ind_min_number == index_of_job:
            break
    line = [el for el in line if el != min_number]

print(cycle)
