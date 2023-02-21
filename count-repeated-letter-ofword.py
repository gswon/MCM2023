from english_words import get_english_words_set
lst = get_english_words_set(['web2'], lower=True)
lst = list(lst)

count = 0
num = 0
for i in lst:
    i = list(i)
    i = sorted(i)
    if len(i) == 5:
        if i[-1] == i[-2]:
            count += 1
        else:
            count += 0

    else:
        count += 0

for j in lst:
    if len(j) == 5:
        num += 1
    else:
        num += 0


print(count)
print(num)
print(f" The number of repeated letter of words{count/num * 100}")



lst2 = get_english_words_set(['web2'], lower=True)
lst2 = list(lst2)
count = 0
for i in lst2:
    if "a" in i:
        count += 1
print(f"Calculating word with a certain letter: {count/len(lst2) * 100}")
