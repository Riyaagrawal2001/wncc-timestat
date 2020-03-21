import numpy as np

f = open("timestat.txt", "r")
ll1 = (f.read()).split("\n\n")
f.close()
ll2 = [i.strip() for i in ll1]

real = [i.split("\n")[0].split(" ")[-1].strip() for i in ll2]
real = [int(i.split('m')[0]) * 60 + float(i.split('m')[1][:-1]) for i in real]
# print(len(real))

user = [i.split("\n")[1].split(" ")[-1].strip() for i in ll2]
user = [int(i.split('m')[0]) * 60 + float(i.split('m')[1][:-1]) for i in user]

sys = [i.split("\n")[2].split(" ")[-1].strip() for i in ll2]
sys = [int(i.split('m')[0]) * 60 + float(i.split('m')[1][:-1]) for i in sys]


real = np.array(real)
user = np.array(user)
sys = np.array(sys)

real_avg = np.mean(real)
user_avg = np.mean(user)
sys_avg = np.mean(sys)

real_std = np.std(real)
user_std = np.std(user)
sys_std = np.std(sys)


def within_func(x, s, e):
    label = 0
    if (x >= s and x <= e):
        label = 1
    
    return label

num_real = sum([within_func(i, real_avg - real_std, real_avg + real_std) for i in real])
# print(num_real)
num_user = sum([within_func(i, user_avg - user_std, user_avg + user_std) for i in user])
num_sys = sum([within_func(i, sys_avg - sys_std, sys_avg + sys_std) for i in sys])


print("Number of runs: ", len(real))
print("Average Time statistics")
print("real: ", str(round(real_avg, 4)) + "s", " user: ", str(round(user_avg, 4)) + "s", " sys: ", str(round(sys_avg, 4)) + "s")
print("Standard deviation of Time statistics")
print("real: ", str(round(real_std, 4)) + "s", " user: ", str(round(user_std, 4)) + "s", " sys: ", str(round(sys_std, 4)) + "s")
print("Number of runs within (average - standard deviation) to (average + standard deviation)")
print("real: ", num_real, " user: ", num_user, " sys: ", num_sys)