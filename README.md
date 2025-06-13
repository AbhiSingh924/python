# Python Coding Questions - Strings and Arrays

This repository contains a comprehensive list of Python coding questions focused on **strings** and **arrays**. Each question is designed to help you practice and master fundamental programming concepts, algorithms, and problem-solving skills in Python.

## Contents

- **String Questions (50):**
- **Array Questions (50):**
  
## How to Use

1. **Browse the Questions:**  
   Open `questions.txt` to view all string and array questions.

2. **Solve the Problems:**  
   - Implement your solutions in Python.
   - Avoid using built-in functions if the question specifies so.
   - Save your solutions in appropriately named files (e.g., `reverseString.py`, `findFrequency.py`).

3. **Practice and Learn:**  
   These questions are ideal for coding interviews, exams, and self-study.

## Example

**Question:**  
7. Convert a string to uppercase without using upper().

**Sample Solution:**
```python
def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result
```

## Contribution

Feel free to contribute by:
- Adding new questions
- Improving solutions
- Fixing errors or typos

## License

This project is open-source and free to use for educational purposes.

---
Happy Coding!
