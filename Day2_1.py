import numpy as np

f = open("input2_2.txt", "r")
lines = f.readlines()

safe_count = 0

for i, l in enumerate(lines):
    a = l.strip()
    tmp_arr = list(map(int, a.split()))
    rev = sorted(tmp_arr, reverse=True)
    sort = sorted(tmp_arr)
    if rev == tmp_arr or sort == tmp_arr:
        tmp_arr_srtd = sorted(tmp_arr)

        differences = np.diff(tmp_arr_srtd)
        set_diffs = set(differences)
        if (1 <= len(set_diffs) <= 3) and 1 <= min(set_diffs) <= 3 and max(set_diffs) <= 3:
            safe_count = safe_count + 1
            print("Safe", tmp_arr)
    else:
        print("Unsafe", tmp_arr)
print(safe_count)