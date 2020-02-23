hash_table = [[] for _ in range(10)]
print(hash_table)

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)

    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')

print(search(hash_table, 10))  # Output: Nepal
print(search(hash_table, 20))  # Output: India
print(search(hash_table, 30))  # Output: None

delete(hash_table, 100)
print(hash_table)
# Output:
# Key 100 not found
# [[(10, 'Nepal'), (20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]

delete(hash_table, 10)
print(hash_table)
# Output:
# Key 10 deleted
# [[(20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]
