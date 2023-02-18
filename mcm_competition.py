# list_word = list(set)

# count = 0
# for i in range(len(list_word)):
#     word = sorted(list_word[i])
#     first_letter = word[0]
#     for j in range(1, len(word)):
#         if first_letter == word[j]:
#             count += 1
#             break
#         else:
#             first_letter = word[j]
# print(count)

list_word = ["acb", "ddcz", "apple", "dog", "aabbcc"]

count = 0
for i in range(len(list_word)):
    word = sorted(list_word[i])
    # first_letter = word[0]
    left = 0
    right = len(word) - 1
    while left <= right:
        if word[left] == word[left + 1]:
            count += 1
            break
        elif word[right] == word[right - 1]:
            count += 1
            break
        else:
            left += 1
            right -= 1
print(count)
