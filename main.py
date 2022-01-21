import numpy as np
import matplotlib.pyplot as plt

# Returns array of largest sum (Preffered Array
def get_max(arr1, arr2):
    return arr1 if np.sum(arr1) > np.sum(arr2) else arr2

# Holds solving algorithm
def solve(bundles):
    # Distributes bundles into
    a11, a12, a21, a22 = bundles[0],bundles[1],bundles[2],bundles[3]
    # Make copy before bundles is distributed
    copy = bundles
    # shuffled list holds
    swapped_items = [[] for x in range(0,4)]
    swaps = 0
    difs1 = []
    difs2 = []

    total_bundle_val = [[] for x in range(0,4)]
    sums1 = []
    sums2 = []
    while copy[0] or copy[1] or copy[2] or copy[3]:
        for i in range(len(copy)):
            if not copy[i]:
                copy[i] = shuffled[i]
                shuffled[i] = []

        count = count + 1

        created = [[] for x in range(0,4)]
        for i in range(0, 4):
            created[i] = np.concatenate((copy[i], shuffled[i])).tolist()
            total_bundle_val[i].append(np.sum(created[i]))


        dif1 = np.sum(created[0]) - np.sum(created[1])
        dif2 = np.sum(created[2]) - np.sum(created[3])
        difs1.append(dif1)
        difs2.append(dif2)

        sums1.append(np.sum(created[0]) + np.sum(created[1]))
        sums2.append(np.sum(created[2]) + np.sum(created[3]))

        if check_symef(created):
            return True, difs1, difs2, max(get_max(created[0],created[1])), max(get_max(created[2],created[3])), total_bundle_val
        else:
            bin = True
            if not check_ef(created[0],created[1]) and not check_ef(created[2],created[3]):
                bin = dif1 > dif2
            elif not check_ef(created[0],created[1]):
                bin = False
            else:
                bin = True

            if bin:
                if dif1 > 0:
                    max_idx = copy[0].index(max(copy[0]))
                    shuffled[1].append(copy[0][max_idx])
                    copy[0].pop(max_idx)
                    shuffled[3].append(copy[2][max_idx])
                    copy[2].pop(max_idx)
                else:
                    max_idx = copy[1].index(max(copy[1]))
                    shuffled[0].append(copy[1][max_idx])
                    copy[1].pop(max_idx)
                    shuffled[2].append(copy[3][max_idx])
                    copy[3].pop(max_idx)
            else:
                if dif2 > 0:
                    max_idx = copy[2].index(max(copy[2]))
                    shuffled[3].append(copy[2][max_idx])
                    copy[2].pop(max_idx)
                    shuffled[1].append(copy[0][max_idx])
                    copy[0].pop(max_idx)
                else:
                    max_idx = copy[3].index(max(copy[3]))
                    shuffled[2].append(copy[3][max_idx])
                    copy[3].pop(max_idx)
                    shuffled[0].append(copy[1][max_idx])
                    copy[1].pop(max_idx)

    print(bundles)
    return False

def check_ef(arr1, arr2):
    if max(np.sum(arr1), np.sum(arr2)) == np.sum(arr1):
        return max(arr1) <= np.sum(arr1) - np.sum(arr2)
    else:
        return max(arr2) <= np.sum(arr2) - np.sum(arr1)


def generate_bundles(amount):
    bundles = []
    for i in range(amount):
        bund_x = []
        # size1 = np.random.randint(1, 1000)
        # size2 = np.random.randint(1, 1000)
        size1 = 1000
        size2 = 1000

        rand_x = np.random.randint(0,100, size1).tolist()
        rand_y = np.random.randint(0,100, size2).tolist()
        bund_x.append(rand_y)
        bund_x.append(rand_x)
        rand_x = np.random.randint(0, 100, size1).tolist()
        rand_y = np.random.randint(0, 100, size2).tolist()
        bund_x.append(rand_x)
        bund_x.append(rand_y)


        #if np.sum(bund_x[0]) - np.sum(bund_x[1]) > 0 and np.sum(bund_x[2]) - np.sum(bund_x[3]) < 0 or np.sum(bund_x[0]) - np.sum(bund_x[1]) < 0 and np.sum(bund_x[2]) - np.sum(bund_x[3]) > 0:
        bundles.append(bund_x)

    return bundles





def check_symef(bundles):
    sums = []
    for i in bundles:
        sums.append(np.sum(i))

    max_a1 = 0
    max_a2 = 0
    if max(sums[0], sums[1]) == sums[0]:
        max_a1 = max(bundles[0])
    else:
        max_a1 = max(bundles[1])

    if max(sums[2], sums[3]) == sums[2]:
        max_a2 = max(bundles[2])
    else:
        max_a2 = max(bundles[3])

    if abs(sums[0] - sums[1]) <= max_a1 and abs(sums[2] - sums[3]) <= max_a2:
        return True

    return False

a1_1 = [1, 2, 3]
a1_2 = [1,2,4]
a2_1 = [1, 1, 2]
a2_2 = [2, 2, 1]

bundles = [a1_1, a1_2, a2_1, a2_2]

print(check_symef(bundles))
print(solve(bundles))

all_bunds = []

a1_1 = [6,4,2]
a1_2 = [5,3,1]
a2_1 = [1, 1, 1]
a2_2 = [3, 3, 3]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [6,5]
a1_2 = [3,2,1]
a2_1 = [1, 3]
a2_2 = [3, 1, 2]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [6,5,4]
a1_2 = [3,2,1]
a2_1 = [1, 3, 1]
a2_2 = [3, 1, 2]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [6,4,3]
a1_2 = [5,2,1]
a2_1 = [1, 1, 3]
a2_2 = [3, 1, 3]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [6,5,4]
a1_2 = [3,2,1]
a2_1 = [1, 3, 1]
a2_2 = [3, 1, 3]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [50000,5,4]
a1_2 = [3,2,1]
a2_1 = [0, 3, 1]
a2_2 = [3, 1, 3]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

a1_1 = [50000]
a1_2 = [3,2,1]
a2_1 = [1]
a2_2 = [3, 1, 5000]
all_bunds.append([a1_1, a1_2, a2_1, a2_2])

for i in all_bunds:
    print(solve(i))

difs11 = []
difs22 = []
all = generate_bundles(10000)
count = 0
true_count = 0
false_count = 0
for i in all:
    count = count + 1
    print(count)
    works, difs1, difs2, max1, max2, bundles = solve(i)
        # if len(set(sums1)) != 1 or len(set(sums2)) != 1:
        #     print(i)
        #     print(sums1)
        #     print(sums2)
        #     break
    difs11 = difs1
    difs22 = difs2
    if works:
        true_count = true_count + 1
    else:
        print(i)
        false_count = false_count + 1
        break



        # len_list = list(range(0, len(difs11)))
        # plt.plot(len_list, difs11)
        # plt.plot(len_list, difs22)
        # len_list = list(range(0, len(difs11)))
        # # plt.plot(len_list, bundles[0])
        # # plt.plot(len_list, bundles[1])
        # # plt.plot(len_list, bundles[2])
        # # plt.plot(len_list, bundles[3])
        # plt.axhline(y=0, color='r', linestyle='-')
        # plt.axhline(y=max1, color='y', linestyle='-')
        # plt.axhline(y=max2, color='b', linestyle='-')
        # plt.axhline(y=-max1, color='y', linestyle='-')
        # plt.axhline(y=-max2, color='b', linestyle='-')
        # plt.show()

print("length: " + str(len(all)))
print("Program Works: " + str(true_count))
print("Program Breaks: " + str(false_count))


len_list = list(range(0, len(difs11)))