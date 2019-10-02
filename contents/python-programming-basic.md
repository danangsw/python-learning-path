# Learn Python Programming Basic

## Python naming convention

Python filenames must have a `.py` extension and **must not** contain dashes (`-`).

Python supports making things private by using a leading double underscore `__` (aka. "dunder") prefix on a name, this is discouraged. Prefer the use of a single underscore `_`. 

Summarized from [PEP](https://www.python.org/dev/peps/pep-0008/#naming-conventions):

- Modules (filenames) should have **short**, `all_lowercase_names`, may **contain underscores**.
- Packages (directories) should have **short**, `all_lowercase_names`, preferably **without underscores**.
- Classes should use the `CapWords` convention.

A good overview when creating variable names, as well as apply to other names (for classes, packages, etc.):

- Variable name are not full description.
- Put details in the comments.
- Too specific name might mean to specific code.
- Keep short scope for read quickly.
- Spend time thinking about readability.

Another good overview of the naming conventions as given in the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations):


Type    | Public    | Internal  |
--------|-----------|-----------|
| Packages  | `lower_with_under`    |   |
| Modules   | `lower_with_under`    | `_lower_with_under` |
| Classes   | `CapWords`    | `_CapWords`   |
| Exceptions    | `CapWords`  |   |
| Functions    | `lower_with_under()`   | `_lower_with_under()` |
| Global/Class Constants    | `CAPS_WITH_UNDER`    | `_CAPS_WITH_UNDER` |
| Global/Class Variables    | `lower_with_under`    | `_lower_with_under`   |
| Instance Variables    | `lower_with_under`    | `_lower_with_under (protected)`   |
| Method Names    | `lower_with_under()`    | `_lower_with_under() (protected)` |
| Function/Method Parameters    | `lower_with_under`    |   |
| Local Variables    | `lower_with_under`    |  |

## Hello, World!
- Simple syntax. The simplest directive in Python is `print` directive.
- Two major Python versions, Python 2 and Python 3. We will use Python3.
- Python uses identation (four spaces) block, instead of curly braces.

## Variable and types

- Assignments can be done on more than one variable "simultaneously" on the same line.
- Mixing operators between numbers and strings is not supported.

**Numbers**

- Python is completely object-oriented, not "statically typed".
- Every variable in Python is an object.
- Python support two types of number - integer and floating - as well as support complex number.

**Strings**

- Strings are defined either with a single quote or a double quotes.
- The difference between the two is that using double quotes makes it easy to include apostrophes
- Simple operators can be executeed in number and string.
- Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`.
- Put several strings within parentheses `("..." )` to have them joined together.
- Strings can be indexed (subscripted), with the first character having index `0`. Slicing is also supported.
- Python string is `immutable`.
- The built-in function `len()` returns the length of a string.

## Lists

- Lists are very similar to arrays.

## Basic Operators

- Support arimatic operators `+ - * /`
- Support modulo operator `%`
- Support power operator `**`
- Supports multiplying strings to form a string with a repeating sequence `*`
- Lists can be joined with the addition operators `+`.
- Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator `*`.

## String Formatting

- The `%` operator is used to format a set of variables enclosed in "tuple", together with a format string, with contains normal text with "argument specifiers", like `%d` or `%s`.
- Any object which is not a string can be formatted using the `%s` operator as well. 
- Here are some basic argument specifiers you should know:
    - `%s` - String (or any object with a string representation, like numbers)
    - `%d` - Integers
    - `%f` - Floating point numbers
    - `%.<number of digits>f` - Floating point numbers with a fixed amount of digits to the right of the dot.
    - `%x` or `%X` - Integers in hex representation (lowercase/uppercase)

## Basic String Operations

- Strings are bits of text. 
- Python string is a array object, Python (and most other programming languages) start index at 0 instead of 1.
- Python string supports the extended slice syntax. The general form is `strings[start:stop:step]`.

## Conditions

- Python uses boolean variable to evaluate conditions.
- Variable assignment is a single equals operator `=`.
- Comparasion operators are using the double equals operator `==`. The "not equals" operator is marked as `!=`.
- The `and` and `or` boolean operators allow building complex boolean expressions.
- The `in` operator could to check if a specified object exist within an iterable object container, such as a list or a array.
- A statement is evaluated as true if one of the following is correct: 
    1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
    2. An object which is not considered "empty" is passed.
        - An empty string: `""` 
        - An empty list: `[]` 
        - The number zero: `0` 
        - The false boolean variable: `False`
- Unlike the double equals operators `==`, the `is` opererator does not match the values of variables, but the instances it themselves.
- Using "not" before a boolean expression inverts it.

# Loops

- There are two types of loops in Python, `for` and `while`.

**The `for` loop**

- For loops over a given sequence.
- For loops can iterate over a sequence of numbers using `range` and `xrange`.
- Python 3 uses the `range` function, which acts like `xrange`.

**The `while` loop**

- While loops repeat as long as a certain boolean condition is met.

**`break` and `continue` statements**

- `break` is used to exit a loop block.
- `continue` is used to skip the current block.

**`else` clause for loops**

- Python supports `else` with a loops.
- When the loop condition of `for` or `while` statement fails then code part in `else` is executed.
- If `break` statement is executed then `else` block will be skipped.
- Even any `continue` statement within a loops, the `else` block will be executed.

## Functions

- Functions in Python are defined by keyword `def`, following by the function name as the block name.
- Functions may also receive arguments.
- Function may return a value to the caller.