# HackerRank AI
# Statistics and Machine Learning
# Day 5: Computing the Correlation
# Problem code: https://www.hackerrank.com/challenges/computing-the-correlation/problem


# Reading in data
Maths = []
Phys = []
Chem = []

for _ in range(int(input())):
    m, p, c = [int(i) for i in input().split()]
    Maths.append(m)
    Phys.append(p)
    Chem.append(c)


def calc_pearsonr(array1, array2):
    '''
    Calculating the pearson r correlation between arr1 and arr2

    *Args:
    arr1 (array)
    arr2 (array)

    return:
    float: correlation coefficient

    '''
    mean_1 = sum(array1) / len(array1)
    mean_2 = sum(array2) / len(array2)
    # get the numerator
    num = sum([(x - mean_1) * (y - mean_2) for x, y in zip(array1, array2)])
    # calculate the standard deviation of the two arrays
    s1 = (sum([(x - mean_1)**2 for x in array1]))**(1 / 2)
    s2 = (sum([(x - mean_2)**2 for x in array2]))**(1 / 2)
    r = num / (s1 * s2)
    return round(r, 2)


print(calc_pearsonr(Maths, Phys))
print(calc_pearsonr(Phys, Chem))
print(calc_pearsonr(Maths, Chem))
