##Problem1.
# 'Introduction' exercises:
# Exercise 1: [Say "Hello, World!" With Python]
my_string = "Hello, World!"
print(my_string)

# Exercise 2: [Python If-Else]
import math
import os
import random
import re
import sys
n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Exercise 3: [Arithmetic Operators]
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Exercise 4: [Python: Division]
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# Exercise 5: [Loops]
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Exercise 6: [Write a function]
def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    return leap
year = int(input())
print(is_leap(year))

# Exercise 7: [Print Function]
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep='')


# ' Data types' exercises:
# Exercise 1: [List Comprehensions]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k]
           for i in range(x + 1)
           for j in range(y + 1)
           for k in range(z + 1)
           if i + j + k != n])

# Exercise 2: [Find the Runner-Up Score!]
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    print(max(x for x in arr if x != m))

# Exercise 3: [Nested Lists]
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted(set(score for name, score in records))[1]

    for name in sorted(name for name, score in records if score == second_lowest):
        print(name)

# Exercise 4: [Lists]
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))
        elif cmd[0] == "append":
            lst.append(int(cmd[1]))
        elif cmd[0] == "sort":
            lst.sort()
        elif cmd[0] == "pop":
            lst.pop()
        elif cmd[0] == "reverse":
            lst.reverse()

# Exercise 5: [Tuples]
if __name__ == '__main__':
    N=int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# Exercise 6: [Finding the percentage]
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    print(f"{avg:.2f}")

# 'Strings' exercises:
# Exercise 1: [Validating UID]
T = int(input())
for _ in range(T):
    uid = input().strip()
    upper = sum(c.isupper() for c in uid)
    digits = sum(c.isdigit() for c in uid)
    if (len(uid) == 10
            and uid.isalnum()
            and len(set(uid)) == 10
            and upper >= 2
            and digits >= 3):
        print("Valid")
    else:
        print("Invalid")

# Exercise 2: [Validating Credit Card Numbers]
import re
n = int(input())
for _ in range(n):
    card = input().strip()
    format_ok = re.fullmatch(r'[456]\d{15}|[456]\d{3}(-\d{4}){3}', card)
    digits = card.replace('-', '')
    if format_ok and not re.search(r'(\d)\1{3}', digits):
        print("Valid")
    else:
        print("Invalid")

# Exercise 3: [Validating Postal Codes]
regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Exercise 4: [Matrix Script]
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix.append(input())
# read column by column
decoded = "".join(matrix[r][c] for c in range(m) for r in range(n))
# symbol runs between alphanumerics -> one space
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))

# Exercise 5: [The Minion Game]
def minion_game(string):
    vowels = "AEIOU"
    n = len(string)
    kevin = 0
    stuart = 0
    for i, ch in enumerate(string):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)

# Exercise 6: [sWAP cASE]
def swap_case(s):
   swapped = []
   for char in s:
    if char.islower():
        swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)

    return ''.join(swapped)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Exercise 7: [String Split and Join]
def split_and_join(line):
    return "-".join(line.split(" "))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Exercise 8: [What's Your Name?]
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Exercise 9: [Mutations]
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Exercise 10: [Find a string]
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Exercise 11: [String Validators]
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# Exercise 12: [Text Alignment]
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Exercise 13: [Text Wrap]
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Exercise 14: [Designer Door Mat]
n, m = map(int, input().split())
# Top half
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))
# Center line
print("WELCOME".center(m, "-"))
# Bottom half (mirror of the top)
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))

# 'Sets' exercises:
# Exercise 1: [String Formatting]
def print_formatted(number):
    width = len(bin(number)) - 2   # strip the '0b' prefix
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Exercise 2: [Alphabet Rangoli]
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    for i in range(size):
        left = [alpha[size - 1 - j] for j in range(i + 1)]
        right = left[:-1][::-1]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))
    print("\n".join(lines + lines[-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Exercise 3: [Capitalize!]
def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

# Exercise 4: [Merge the Tools!]
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print("".join(dict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Exercise 5: [Introduction to Sets]
def average(array):
    distinct = set(array)
    return sum(distinct) / len(distinct)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Exercise 6: [Symmetric Difference]
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
for x in sorted(a ^ b):
    print(x)

# Exercise 7: [No Idea!]
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
print(happiness)

# Exercise 8: [Set .add()]
n = int(input())
stamps = set()
for _ in range(n):
    stamps.add(input())
print(len(stamps))

# Exercise 9: [Set .discard(), .remove() & .pop()]
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "pop":
        s.discard(min(s))
    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    else:
        s.discard(int(cmd[1]))
print(sum(s))

# Exercise 10: [Set .union() Operation]
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.union(french)))

# Exercise 11: [Set .intersection() Operation]
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.intersection(french)))

# Exercise 12: [Set .difference() Operation]
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.difference(french)))

# Exercise 13: [Set .symmetric_difference() Operation]
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.symmetric_difference(french)))

# Exercise 14: [Set Mutations]
input()
A = set(map(int, input().split()))
for _ in range(int(input())):
    op = input().split()[0]
    B = set(map(int, input().split()))
    getattr(A, op)(B)
print(sum(A))

# Exercise 15: [The Captain's Room]
k = int(input())
rooms = list(map(int, input().split()))
unique = set(rooms)
print((k * sum(unique) - sum(rooms)) // (k - 1))

# Exercise 16: [Check Subset]
for _ in range(int(input())):
    input()
    A = set(input().split())
    input()
    B = set(input().split())
    print(A.issubset(B))

# Exercise 17: [Check Strict Superset]
A = set(input().split())
n = int(input())
print(all(A > set(input().split()) for _ in range(n)))

# 'Collections' exercises:
# Exercise 1: [collections.Counter()]
from collections import Counter
input()
sizes = Counter(map(int, input().split()))
earned = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        earned += price
        sizes[size] -= 1
print(earned)

# Exercise 2: [DefaultDict Tutorial]
from collections import defaultdict
n, m = map(int, input().split())
positions = defaultdict(list)
for i in range(1, n + 1):
    positions[input()].append(i)
for _ in range(m):
    print(*positions.get(input(), [-1]))

# Exercise 3: [Collections.namedtuple()]
from collections import namedtuple
n = int(input())
Student = namedtuple("Student", input().split())
total = sum(int(Student(*input().split()).MARKS) for _ in range(n))
print(f"{total / n:.2f}")

# Exercise 4: [Collections.OrderedDict()]
from collections import OrderedDict
items = OrderedDict()
for _ in range(int(input())):
    *name, price = input().split()
    name = " ".join(name)
    items[name] = items.get(name, 0) + int(price)
for name, total in items.items():
    print(name, total)

# Exercise 5: [Word Order]
from collections import OrderedDict
counts = OrderedDict()
for _ in range(int(input())):
    word = input()
    counts[word] = counts.get(word, 0) + 1
print(len(counts))
print(*counts.values())

# Exercise 6: [Collections.deque()]
from collections import deque
d = deque()
for _ in range(int(input())):
    command, *args = input().split()
    getattr(d, command)(*args)
print(*d)

# Exercise 7: [Piling Up!]
from collections import deque
for _ in range(int(input())):
    input()
    cubes = deque(map(int, input().split()))
    top = float("inf")
    possible = True
    while cubes:
        biggest = cubes.popleft() if cubes[0] >= cubes[-1] else cubes.pop()
        if biggest > top:
            possible = False
            break
        top = biggest
    print("Yes" if possible else "No")

# Exercise 8: [Company Logo]
from collections import Counter
if __name__ == '__main__':
    s = input()
    ranked = sorted(Counter(s).items(), key=lambda pair: (-pair[1], pair[0]))
    for char, count in ranked[:3]:
        print(char, count)

# 'Date and Time' exercises:
# Exercise 1: [Calendar Module]
import calendar
month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())

# Exercise 2: [Time Delta]
from datetime import datetime
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)
    return str(int(abs((d1 - d2).total_seconds())))
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))

# 'Exceptions' exercises:
# Exercise 1: [Exceptions]
t = int(input())
for _ in range(t):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# 'Built-ins' exercises:
# Exercise 1: [Zipped!]
n, x = map(int, input().split())
marks = [map(float, input().split()) for _ in range(x)]
for student in zip(*marks):
    print(f"{sum(student) / x:.1f}")

# Exercise 2: [Athlete Sort]
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())

# Exercise 3: [ginortS]
s = input()
print(''.join(sorted(s, key=lambda c: (
    c.isdigit(),        # letters before digits
    c.isupper(),        # lowercase before uppercase (among letters)
    c in '02468',       # odd digits before even digits (among digits)
    c,                  # then alphabetical / numeric order
))))

# 'Python Functionals' exercises:
# Exercise 1: [Map and Lambda Function]
cube = lambda x: x ** 3
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# 'Regex and Parsing challenges ' exercises:
# Exercise 1: [Detect Floating Point Number]
import re
for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*\.\d+$', input())))

# Exercise 2: [Re.split()]
import re
print("\n".join(filter(None, re.split(r'[,.]', input()))))

# Exercise 3: [Group(), Groups() & Groupdict()]
import re
m = re.search(r'([a-zA-Z0-9])\1', input())
print(m.group(1) if m else -1)

# Exercise 4: [Re.findall() & Re.finditer()]
import re
cons = 'qwrtypsdfghjklzxcvbnm'
found = re.findall(rf'(?<=[{cons}])([aeiou]{{2,}})(?=[{cons}])', input(), re.I)
print("\n".join(found) if found else -1)

# Exercise 5: [Re.start() & Re.end()]
import re
s, k = input(), input()
matches = list(re.finditer(rf'(?=({re.escape(k)}))', s))
if matches:
    for m in matches:
        print((m.start(1), m.end(1) - 1))
else:
    print((-1, -1))

# Exercise 6: [Regex Substitution]
import re
for _ in range(int(input())):
    line = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',
                 lambda m: 'and' if m.group() == '&&' else 'or', line))

# Exercise 7: [Validating Roman Numerals]
import re
pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(bool(re.match(pattern, input())))

# Exercise 8: [Validating Phone Numbers]
import re
for _ in range(int(input())):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")

# Exercise 9: [Validating and Parsing Email Addresses]
import re, email.utils
for _ in range(int(input())):
    name, addr = email.utils.parseaddr(input())
    if re.match(r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
        print(email.utils.formataddr((name, addr)))

# Exercise 10: [Hex Color Code]
import re
n = int(input())
css = "\n".join(input() for _ in range(n))
for block in re.findall(r'\{([^}]*)\}', css):
    for color in re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', block):
        print(color)

# Exercise 11: [HTML Parser - Part 1]
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for name, value in attrs:
            print('->', name, '>', value)
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for name, value in attrs:
            print('->', name, '>', value)
n = int(input())
MyParser().feed('\n'.join(input() for _ in range(n)))

# Exercise 12: [HTML Parser - Part 2]
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_comment(self, data):
        print('>>> Multi-line Comment' if '\n' in data else '>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)
n = int(input())
MyParser().feed('\n'.join(input() for _ in range(n)))

# Exercise 13: [Detect HTML Tags, Attributes and Attribute Values]
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print('->', name, '>', value)
n = int(input())
MyParser().feed('\n'.join(input() for _ in range(n)))

# Exercise 14: [Validating UID]
import re
for _ in range(int(input())):
    uid = input()
    ok = re.fullmatch(r'(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[A-Za-z0-9]{10}', uid)
    print('Valid' if ok else 'Invalid')

# Exercise 15: [Validating Credit Card Numbers]
import re
for _ in range(int(input())):
    card = input()
    ok = (re.fullmatch(r'[456]\d{3}(-?\d{4}){3}', card)
          and not re.search(r'(\d)\1{3}', card.replace('-', '')))
    print('Valid' if ok else 'Invalid')

# Exercise 16: [Validating Postal Codes]
import re
regex_integer_in_range = r'^[1-9]\d{5}$'
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'
P = input()
print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Exercise 17: [Matrix Script]
import re
n, m = map(int, input().split())
rows = [input() for _ in range(n)]
decoded = ''.join(rows[r][c] for c in range(m) for r in range(n))
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))

# 'XML' exercises:
# Exercise 1: [XML 1 - Find the Score]
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    return sum(len(e.attrib) for e in node.iter())
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# Exercise 2: [XML2 - Find the Maximum Depth]
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# 'Closures and Decorations' exercises:
# Exercise 1: [Standardize Mobile Number Using Decorators]
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# Exercise 2: [Decorators 2 - Name Directory]
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# 'Numpy' exercises:
# Exercise 1: [Arrays]
import numpy
def arrays(arr):
    return numpy.array(arr[::-1], float)
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Exercise 2: [Shape and Reshape]
import numpy
print(numpy.array(input().split(), int).reshape(3, 3))

# Exercise 3: [Transpose and Flatten]
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(a.T)
print(a.flatten())

# Exercise 4: [Concatenate]
import numpy
n, m, p = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((a, b), axis=0))

# Exercise 5: [Zeros and Ones]
import numpy
shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))

# Exercise 6: [Eye and Identity]
import numpy
numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(numpy.eye(n, m, k=0))

# Exercise 7: [Array Mathematics]
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

# Exercise 8: [Floor, Ceil and Rint]
import numpy
numpy.set_printoptions(legacy='1.13')
a = numpy.array(input().split(), float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

# Exercise 9:[Sum and Prod]
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(a, axis=0)))

# Exercise 10: [Min and Max]
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(a, axis=1)))

# Exercise 11: [Mean, Var, and Std]
import numpy
numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(float(numpy.std(a)), 11))

# Exercise 12: [Dot and Cross]
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))

# Exercise 13: [Inner and Outer]
import numpy
a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b))
print(numpy.outer(a, b))

# Exercise 14: [Polynomials]
import numpy
p = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(p, x))

# Exercise 15: [Linear Algebra]
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(float(numpy.linalg.det(a)), 2))

##Problem2.
# Exercise 1: [Birthday Cake Candles]
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Exercise 2: [Number Line Jumps]
import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    diff = x2 - x1
    speed = v1 - v2
    return "YES" if diff % speed == 0 and diff // speed >= 0 else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Exercise 3: [Viral Advertising]
import math
import os
import random
import re
import sys
def viralAdvertising(n):
    shared = 5
    total_liked = 0
    for _ in range(n):
        liked = shared // 2
        total_liked += liked
        shared = liked * 3
    return total_liked
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Exercise 4: [Recursive Digit Sum]
import math
import os
import random
import re
import sys
def superDigit(n, k):
    total = sum(int(d) for d in n) * k
    while total >= 10:
        total = sum(int(d) for d in str(total))
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Exercise 5: [Insertion Sort - Part 1]
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = value
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Exercise 6: [Insertion Sort - Part 2]
import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)











