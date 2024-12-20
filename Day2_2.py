import numpy as np

f = open("input2_2.txt", "r")
lines = f.readlines()

safe_count = 0


def isSafe(set_diffs):
    result = False
    if (1 <= len(set_diffs) <= 3 and
            1 <= min(abs(x) for x in set_diffs) <= 3 and
            max(abs(x) for x in set_diffs) <= 3 and
            (all(x < 0 for x in set_diffs) or all(x > 0 for x in set_diffs))):
        result = True
    return result


def get_corrupted_level_index(differences):
    print('Diffs', differences)

    all_neg = all(x < 0 for x in differences)
    all_pos = all(x > 0 for x in differences)
    if all_neg:
        for ind, lv in enumerate(differences):
            if lv < -3:
                return ind
    if all_pos:
        for ind, lv in enumerate(differences):
            if lv > 3:
                return ind
    else:
        if differences[0] < 0:
            cur_el = differences[0]
            for ind, lv in enumerate(differences, start=1):
                if lv > cur_el:
                    return ind
        if differences[0] > 0:
            cur_el = differences[0]
            for ind, lv in enumerate(differences, start=1):
                if lv < cur_el:
                    return ind
        else:
            return 0

for i, l in enumerate(lines):
    a = l.strip()
    tmp_arr = list(map(int, a.split()))
    print('Input', tmp_arr)
    differences = np.diff(tmp_arr)
    set_diffs = set(differences)
    if isSafe(set_diffs):
        safe_count = safe_count + 1
        print('Safe', tmp_arr)
    else:
        t_tmp_arr = tmp_arr.copy()
        index = get_corrupted_level_index(differences)
        print('Wrong lv index: ', index)
        differences_list = list(differences)
        t_tmp_arr.pop(index)
        new_differences = np.diff(t_tmp_arr)
        try:
            tmp_arr.pop(index+1)
        except IndexError:
            tmp_arr.pop(len(tmp_arr)-1)
        new_differences_two = np.diff(tmp_arr)
        set_diffs = set(new_differences)
        set_diffs_two = set(new_differences_two)
        if isSafe(set_diffs) or isSafe(new_differences_two):
            safe_count = safe_count + 1
            print('Safe', tmp_arr)
        else:
            print("Unsafe", tmp_arr)
    print('++++++++++++++++++++++++++++++')
print(safe_count)
