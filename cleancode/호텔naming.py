def run(the_list: list):
    for t in range(len(the_list)):
        if the_list[t] == 0:
            continue
        the_list[t] = the_list[t] - 1
