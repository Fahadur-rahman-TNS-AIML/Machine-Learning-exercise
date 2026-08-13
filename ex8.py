batch_a = {"Python", "Java", "C", "SQL"}
batch_b = {"Java", "Python", "SQL", "C++"}
batch_c = {"Python", "Java", "SQL", "JavaScript"}

common = batch_a & batch_b & batch_c

print("Languages known by every batch:", common)

only_a = batch_a - batch_b - batch_c

print("Languages only in Batch A:", only_a)

a_and_b = batch_a & batch_b

a_b_not_c = a_and_b - batch_c

print("Languages in A and B but not C:", a_b_not_c)

all_languages = batch_a | batch_b | batch_c

print("Total distinct languages:", len(all_languages))
