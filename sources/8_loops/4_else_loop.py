# Python supports `else` with a loops.
# When the loop condition of `for` or `while` statement fails then code part in `else` is executed.
# If `break` statement is executed then `else` block will be skipped.
# Even any `continue` statement within a loops, the `else` block will be executed.

count = 0

while count < 5:
    print(count)
    count += 1
    pass
else:
    print("Reach maximum counting (%d)" % count)
    pass

print()
for i in range(0,10):
    if i % 5 == 0:
        break
    print(i)
    pass
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    pass