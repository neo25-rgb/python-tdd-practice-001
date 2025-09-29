Here’s a clear README for your activity:

---

# String and List Utility Functions

This repository contains a set of Python functions that manipulate strings and lists in various ways. Your task is to **implement and thoroughly test** each function, including edge cases.

## Functions to Implement

### 1. `increment_string(strng)`

* **Description:** Increment the numeric suffix of a string.

  * If the string ends with a number, increment that number by 1.
  * If the string does not end with a number, append `1`.
* **Examples:**

  ```python
  "foo" -> "foo1"
  "foobar23" -> "foobar24"
  "foo0042" -> "foo0043"
  "foo9" -> "foo10"
  "foo099" -> "foo100"
  ```

---

### 2. `count_letters(string)`

* **Description:** Count the occurrences of each letter in a string.
* **Example:**

  ```python
  "aba" -> {"a": 2, "b": 1}
  ```

---

### 3. `sum_consecutives(s)`

* **Description:** Return a list of sums of each consecutive pair in a list.
* **Example:**

  ```python
  [1, 2, 3] -> [3, 5]  # 1+2=3, 2+3=5
  ```

---

### 4. `count_unique(string)`

* **Description:** Count the number of unique words in a string.
* Should raise a `ValueError` if the input is not a string.
* **Example:**

  ```python
  "no example ;)"
  ```

---

## Instructions

1. Implement all functions in the main Python file (e.g., `main.py`).

2. Write comprehensive tests for **all functions**, including **edge cases**, such as:

   * Empty strings
   * Strings without numbers
   * Lists with a single element
   * Non-string inputs for `count_unique`

3. Place all test cases in a separate file:

   ```
   tests/test.py
   ```

4. Use Python's built-in `unittest` framework for testing. Example:

   ```python
   import unittest
   from main import increment_string

   class TestIncrementString(unittest.TestCase):
       def test_increment_no_number(self):
           self.assertEqual(increment_string("foo"), "foo1")

       def test_increment_with_number(self):
           self.assertEqual(increment_string("foo009"), "foo010")

   if __name__ == "__main__":
       unittest.main()
   ```

5. Ensure all tests pass before submission.

---
