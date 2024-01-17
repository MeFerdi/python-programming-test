from statistics import multimode

def find_modes(lst):
    modes = multimode(lst)
    return modes, lst.count(modes[0]) if modes else 0
