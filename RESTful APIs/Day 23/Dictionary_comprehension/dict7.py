# Nested dictionary comprehension
# Nested loop (2D dictionary)

tabel={i:{j:i*j for j in range(1,11)} for i in range(1,11)}
print(tabel)