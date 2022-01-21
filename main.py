import numpy as np
import matplotlib.pyplot as plt

# Returns array of largest sum (Preffered Array
def get_max(arr1, arr2):
    return arr1 if np.sum(arr1) > np.sum(arr2) else arr2

# Holds solving algorithm
# Note - for all length 4 lists, 0,1 are bundles 1 and 2 for agent 1, while
# indecies 2,3 hold elements of bundles 1 and 2 for agent 2
# Index 0 and index 2 represent the same bundle for different agents
def solve(bundles):
    # Distributes bundles into
    a11, a12, a21, a22 = bundles[0],bundles[1],bundles[2],bundles[3]
    # Make copy before bundles is distributed
    copy = bundles
    # swapped_items list holds items that were swapped
    swapped_items = [[] for x in range(0,4)]
    # counts amount of swaps
    swaps = 0
    # lists store envy for agents 1 and 2 after every swap
    difs1 = []
    difs2 = []

    # this list stores the total bundle value of each bundle.
    total_bundle_val = [[] for x in range(0,4)]

    # lists store sums for agents 1 and 2 after every swap
    sums1 = []
    sums2 = []

    # while not every item in one bundle has been swapped
    while copy[0] and copy[1] and copy[2] and copy[3]:

        # This code moves swapped items to original bundles if original bundles are empty
        # This is no longer needed but I felt I should leave it in
        # for i in range(len(copy)):
        #     if not copy[i]:
        #         copy[i] = swapped_items[i]
        #         swapped_items[i] = []

        swaps = swaps + 1
        # created combines swapped items and copy items to recreate the entire bundle
        # for the purpose of taking sum and difference
        created = [[] for x in range(0,4)]
        for i in range(0, 4):
            created[i] = np.concatenate((copy[i], swapped_items[i])).tolist()
            total_bundle_val[i].append(np.sum(created[i]))

        # difference taken and stored
        dif1 = np.sum(created[0]) - np.sum(created[1])
        dif2 = np.sum(created[2]) - np.sum(created[3])
        difs1.append(dif1)
        difs2.append(dif2)
        # sum taken and stored
        sums1.append(np.sum(created[0]) + np.sum(created[1]))
        sums2.append(np.sum(created[2]) + np.sum(created[3]))

        # first - Check if entire system is SymEF1... if so, return true, and info to be graphed as needed
        # otherwise, swap goods
        if check_symef(created):
            return True, difs1, difs2, max(get_max(created[0],created[1])), max(get_max(created[2],created[3])), total_bundle_val
        else:
            # bin is true if swapping based on agent 1 and false if agent 2
            bin = True
            # if both systems are not symEF, use system of greatest difference
            # else, chose sym ef system
            if check_ef(created[0],created[1]) and check_ef(created[2],created[3]):
                bin = dif1 > dif2
            elif check_ef(created[0],created[1]):
                bin = False
            else:
                bin = True

            # If agent 1 is focus
            if bin:
                # check which bundle is to be swapped
                # if envy is positi, swap from A_1 to A_2
                # swapping will be outlined in this conditional
                # in the remaining 3, the process is the same, but with different bundles
                if dif1 > 0:
                    # get index of max good in A_1
                    max_idx = copy[0].index(max(copy[0]))
                    # append the good to swapped A_2
                    swapped_items[1].append(copy[0][max_idx])
                    # Remove the good from A_1
                    copy[0].pop(max_idx)
                    # do the same for Agent 2
                    swapped_items[3].append(copy[2][max_idx])
                    copy[2].pop(max_idx)
                else:
                    max_idx = copy[1].index(max(copy[1]))
                    swapped_items[0].append(copy[1][max_idx])
                    copy[1].pop(max_idx)
                    swapped_items[2].append(copy[3][max_idx])
                    copy[3].pop(max_idx)
            else:
                if dif2 > 0:
                    max_idx = copy[2].index(max(copy[2]))
                    swapped_items[3].append(copy[2][max_idx])
                    copy[2].pop(max_idx)
                    swapped_items[1].append(copy[0][max_idx])
                    copy[0].pop(max_idx)
                else:
                    max_idx = copy[3].index(max(copy[3]))
                    swapped_items[2].append(copy[3][max_idx])
                    copy[3].pop(max_idx)
                    swapped_items[0].append(copy[1][max_idx])
                    copy[1].pop(max_idx)
    # If solve fails, it outputs the bundles it failed on
    print(bundles)
    return False

# Checks if one agent is SymEF
def check_ef(arr1, arr2):
    # if preferred bundle is bundle 1
    if max(np.sum(arr1), np.sum(arr2)) == np.sum(arr1):
        # checks if max item is less than difference
        return max(arr1) >= np.sum(arr1) - np.sum(arr2)
    else:
        return max(arr2) >= np.sum(arr2) - np.sum(arr1)

# generates n amount of bundles
def generate_bundles(amount):
    bundles = []
    for i in range(amount):
        # returns bundles as list of list of 4
        bund_x = []
        # declare size
        # size1 = np.random.randint(1, 1000)
        # size2 = np.random.randint(1, 1000)
        size1 = 1000
        size2 = 1000

        # append lists of random ints to  bund_x
        rand_x = np.random.randint(0,100, size1).tolist() # list 0
        rand_y = np.random.randint(0,100, size2).tolist() # list 1
        bund_x.append(rand_y)
        bund_x.append(rand_x)
        rand_x = np.random.randint(0, 100, size1).tolist() # list 2
        rand_y = np.random.randint(0, 100, size2).tolist() # list 3
        bund_x.append(rand_x)
        bund_x.append(rand_y)

        # this line checks that the each list is preferred differently
        #if np.sum(bund_x[0]) - np.sum(bund_x[1]) > 0 and np.sum(bund_x[2]) - np.sum(bund_x[3]) < 0 or np.sum(bund_x[0]) - np.sum(bund_x[1]) < 0 and np.sum(bund_x[2]) - np.sum(bund_x[3]) > 0:
        bundles.append(bund_x)

    return bundles





def check_symef(bundles):
    sums = []
    #get bundle sums
    for i in bundles:
        sums.append(np.sum(i))

    max_a1 = 0
    max_a2 = 0
    # Gets max item in max bundle
    if max(sums[0], sums[1]) == sums[0]:
        max_a1 = max(bundles[0])
    else:
        max_a1 = max(bundles[1])

    if max(sums[2], sums[3]) == sums[2]:
        max_a2 = max(bundles[2])
    else:
        max_a2 = max(bundles[3])

    # if return if both differences are less than both max items
    if abs(sums[0] - sums[1]) <= max_a1 and abs(sums[2] - sums[3]) <= max_a2:
        return True

    return False


# Bundles I tried Manually
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

# solves manual bundles
for i in all_bunds:
    print(solve(i))


# generates 10 bundles
all = generate_bundles(10)
# init outputs
difs11 = []
difs22 = []
count = 0
true_count = 0
false_count = 0

# solve bundles in all
for i in all:
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

    # generates graphs **** Comment out to reduce runtime if doing large amount of simulations
    len_list = list(range(0, len(difs11)))
    plt.plot(len_list, difs11)
    plt.plot(len_list, difs22)
    len_list = list(range(0, len(difs11)))
    # plt.plot(len_list, bundles[0])
    # plt.plot(len_list, bundles[1])
    # plt.plot(len_list, bundles[2])
    # plt.plot(len_list, bundles[3])
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axhline(y=max1, color='y', linestyle='-')
    plt.axhline(y=max2, color='b', linestyle='-')
    plt.axhline(y=-max1, color='y', linestyle='-')
    plt.axhline(y=-max2, color='b', linestyle='-')
    plt.show()

# prints outcome

print("length: " + str(len(all)))
print("Program Works: " + str(true_count))
print("Program Breaks: " + str(false_count))
