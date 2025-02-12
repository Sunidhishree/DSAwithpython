lst=[]

def sep(l):
    rain = {}
    states=[]
    for state, value in l:
        if state in rain:
            rain[state] += float(value)
        else:
            rain[state] = float(value)
            states.append(state)
    return rain,states


def rainaverage(l):
    rain,states = sep(l)

    state_counts = {}
    for state in [x[0] for x in l]:
        if state in state_counts:
            state_counts[state] += 1
        else:
            state_counts[state] = 1

    for state in rain:
        rain[state] /= state_counts[state]
    lst = [(states[i], rain[states[i]]) for i in range(len(states))]

    lst.sort()
    return lst


