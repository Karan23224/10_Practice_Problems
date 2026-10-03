# Q1.Count Digits and Sum
# Given an integer n, write a program to:
# Count the number of digits.
# Calculate the sum of all its digits.

# Example:
# Input: 5832
# Output:
# Number of digits: 4
# Sum of digits: 18

n=23340
digits=0
total=0

for i in str(n):
    total=total+int(i)
    digits+=1
print("Number: ",n)
print("Number of digits: ",digits)
print("Sum of digits: ",total)


# Q2. Second Largest Element
# Given a list of integers, find the second largest unique element without using sort() or sorted().

# Example:
# Input: [10, 5, 8, 10, 3, 7]
# Output: 8

l=[1,4,2,3,8,1,9,9]
unique_elem=list(set(l))
temp_list=unique_elem.copy()

if len(temp_list)==0:
    print("List is empty")
elif len(temp_list)==1:
    print("There is only 1 element")
elif len(temp_list)==2:
    print("Second smallest element is ",min(temp_list))
else:
    while len(temp_list)>2:
        minimun=min(temp_list)
        temp_list.remove(minimun)

    print("Second smallest element in the list is ",min(temp_list))


# Q3. Character Frequency
# Given a string, count how many times each character appears.

# Example:
# Input: "banana"
# Output:
# b: 1
# a: 3
# n: 2

strg="naman"
dict1={}

for i in strg:
    ct=strg.count(i)

    dict1[i]=ct

print("String: ",strg)
print(dict1)


# 4. Remove Duplicates Without Changing Order
# Given a list, remove duplicate elements while maintaining their original order.

# Example:
# Input: [4, 2, 4, 5, 2, 7, 5]
# Output: [4, 2, 5, 7]
# Constraint: Don't use set().

l=[12,3,2,5,5,4,2,12]
l1=l.copy()

for i in l1:
    if l1.count(i)!=1:
        l1.remove(i)
print(l)
print(l1)


# 5. Find the Missing Number
# You are given n-1 numbers from 1 to n. Exactly one number is missing.
# Find the missing number.

# Example:
# Input: [1, 2, 3, 5, 6]
# Output: 4

l=[1,2,3,4,5,6,8,9,10]
actual_total=0
total=sum(list(range(min(l),max(l)+1)))

for i in l:
    actual_total+=i

print(l)
print("Number missing: ",total-actual_total)


# 6. Longest Word in a Sentence
# Given a sentence, find the longest word.

# Example:
# Input:
# "Python is powerful for data science"
# Output:
# powerful

strg="Weelcoome to the corporate world"
l=strg.split()
longest=l[0]

for i in l:
    if len(i)>len(longest):
        longest=i
print("Longest word: ",longest)


# 7. Two Sum
# Given a list of integers and a target value, find two numbers whose sum equals the target.

# Example:
# Input:
# numbers = [2, 7, 11, 15]
# target = 9
# Output:
# 2, 7

numbers = [2, 7, 11, 15]
target = 9

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print(complement, num)
        break
    seen[num] = True


# 8. Longest Consecutive Sequence
# Given an unsorted list of integers, find the length of the longest sequence of consecutive numbers.
# Example:
# Input:
# [100, 4, 200, 1, 3, 2]
# Output:
# 4
# Because:
# 1, 2, 3, 4
# is the longest consecutive sequence.

numbers = [100, 4, 200, 1, 3, 2]

num_set = set(numbers)
longest = 0

for num in num_set:
    if num - 1 not in num_set:
        current = num
        length = 1

        while current + 1 in num_set:
            current += 1
            length += 1

        if length > longest:
            longest = length

print("Longest consecutive sequence:", longest)


# 9. First Non-Repeating Character
# Given a string, find the first character that occurs only once.

# Example:
# Input:
# "swiss"
# Output:
# w
text = "swiss"

frequency = {}

# Count frequency of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Find the first character with frequency 1
for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break


# 10. Maximum Subarray Sum
# Given a list containing positive and negative integers, find the maximum possible sum of a contiguous subarray.

# Example:
# Input:
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output:
# 6
# Because:
# [4, -1, 2, 1]
# has sum:
# 4 + (-1) + 2 + 1 = 6

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
maximum_sum = numbers[0]

for num in numbers[1:]:
    current_sum = max(num, current_sum + num)
    maximum_sum = max(maximum_sum, current_sum)

print("Maximum subarray sum:", maximum_sum)