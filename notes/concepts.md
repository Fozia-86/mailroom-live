# Concepts Recap

Everything I've learned so far, with examples I can re-read anytime.

---

## 1. Variables and Types (Lesson 13.3)

A variable is a name that holds a value. Every value has a type.

```python
name: str = "Ayesha"       # text
age: int = 25              # whole number
price: float = 9.99        # decimal number
active: bool = True        # yes or no
```

**Rule:** Money is stored in whole cents (integers), not floats.

```python
price_cents: int = 999     # Rs 9.99 stored as 999 cents
```

---

## 2. Decisions: if / elif / else (Lesson 13.4)

Run different code depending on a condition.

```python
score: int = 85

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")       # this runs because 85 >= 80
else:
    print("Try again")
```

---

## 3. Loops: for and while (Lesson 13.4 / 13.5)

**for** — repeat for each item in a list:

```python
names: list[str] = ["Ayesha", "Tom", "Priya"]
for name in names:
    print(name)
# prints: Ayesha, Tom, Priya (one per line)
```

**while** — repeat as long as a condition is true:

```python
count: int = 3
while count > 0:
    print(count)
    count -= 1
# prints: 3, 2, 1
```

---

## 4. and / or / None (Lesson 13.5)

```python
x: int = 5
if x > 0 and x < 10:
    print("between 1 and 9")    # both must be true

if x == 5 or x == 10:
    print("five or ten")        # at least one must be true
```

**None** means "no value":

```python
result: str | None = None
if result is None:
    print("nothing here yet")
```

---

## 5. Functions (Lesson 13.6)

A function does one job. The signature is the contract — it says what goes in and what comes out.

```python
def add(a: int, b: int) -> int:
    return a + b

assert add(2, 3) == 5    # test with one hand-checkable assertion
```

**Rule:** Every number comes from a tested function.

---

## 6. Lists and Dictionaries (Lesson 13.7)

**List** — ordered items, accessed by index (starting at 0):

```python
fruits: list[str] = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[2])    # cherry
```

**Dictionary** — key-value pairs:

```python
person: dict[str, str] = {"name": "Ayesha", "city": "Lahore"}
print(person["name"])    # Ayesha
```

**Missing key handling:**

```python
if "email" in person:
    print(person["email"])
else:
    print("no email found")
```

---

## 7. Reading a File (Lesson 13.8)

Open a file and read all its text into a string.

```python
with open("data/subscribers.csv", encoding="utf-8") as f:
    text: str = f.read()
```

- `encoding="utf-8"` — tells Python how to turn bytes into text. Without it, Windows might guess wrong and garble names like "Müller".
- `with` — automatically closes the file when done.
- `splitlines()` — splits text into a list of lines (safely ignores trailing newlines).

```python
"a\nb\nc\n".splitlines()   # ['a', 'b', 'c']  — clean, no empty string
"a\nb\nc\n".split("\n")    # ['a', 'b', 'c', '']  — extra empty string!
```

**Rule:** Use `splitlines()` not `split("\n")` for file content.

---

## 8. sys.argv — Reading the Command Line (Lesson 13.8)

When you type `uv run python demo.py subscribers`, Python collects the words into a list called `sys.argv`.

```python
import sys

print(sys.argv)       # ['demo.py', 'subscribers']
print(sys.argv[0])    # 'demo.py'       — the file name (index 0)
print(sys.argv[1])    # 'subscribers'   — the first argument (index 1)
```

Remember: list indexes start at **0**, not 1.

---

## 9. if \_\_name\_\_ == "\_\_main\_\_" — The Front Door Guard (Lesson 13.8)

Python gives every file a hidden name tag called `__name__`.

- You **run** the file directly → `__name__` is `"__main__"` (front door)
- Another file **imports** it → `__name__` is the file's own name like `"shop"` (back door)

**Analogy:** A shop's "open" sign only lights up when the owner walks in the front door. A supplier entering the back door to borrow a tool doesn't trigger the sign.

```python
# shop.py
def shout(word: str) -> str:
    return word + "!"

print("hello from", __name__)       # doorbell — always rings

if __name__ == "__main__":           # open sign — front door only
    print(shout("open"))
```

```python
# visitor.py
from shop import shout              # back door — imports shop
print(shout("borrowed"))
```

| Run command | `__name__` is | Doorbell says | Open sign? |
|---|---|---|---|
| `python shop.py` | `"__main__"` | `hello from __main__` | Yes: `open!` |
| `python visitor.py` | `"shop"` | `hello from shop` | No |

**Why we need it:** Without the guard, when `check.py` imports from `mailroom.py`, the printing code would run too — giving unwanted output.
