# `break` is used to exit a loop block.
# `continue` is used to skip the current block.

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    pass
print()
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    pass