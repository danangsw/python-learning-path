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