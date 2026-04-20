# Secure Password Generator

A robust Python command-line tool that generates secure, randomized passwords based on custom distribution logic and strict user input validation.

## 🚀 Overview

This project was developed to demonstrate core programming principles in Python:
- **Logical Distribution**: Implements a specific character ratio (25% numbers, 10% symbols, 30% uppercase) to ensure high-entropy passwords.
- **Input Sanitization**: Features a custom validation engine to prevent crashes from invalid user inputs.
- **Security-First Approach**: Uses Python's `random` module combined with `shuffle` operations to eliminate predictable character patterns.

## ✨ Features

- **Customizable Length**: Define the exact length of your password (minimum 7 characters).
- **Optional Character Sets**: Choose whether to include uppercase letters, numbers, or special symbols.
- **"Bulletproof" Input Handling**: 
  - Prevents `ValueError` when entering non-integer lengths.
  - Forces strict `y/n` (yes/no) confirmation for character set choices.
- **Zero Dependencies**: Runs on standard Python 3.x libraries without needing external packages like `pip`.

## 🛠️ Technical Logic

Unlike basic generators, this tool follows a **weighted repartition** to guarantee password complexity:
1. **Initial Allocation**: Fills the first portions of the password based on selected categories (e.g., 25% numbers).
2. **Padding**: Automatically fills the remaining length with lowercase letters.
3. **Randomization**: Converts the string into a list and performs a complete shuffle to ensure character types are not clustered.

## 💻 Installation & Usage

### Prerequisites
- Python 3.6 or higher installed on your machine.

### Setup
1. **Clone the repository**:
```bash
git clone https://github.com/kilian-gthb/password_generator.git
```
   
2. **Navigate to the directory:**
```bash
cd password_generator
```

### Execution
```bash
python generator.py
```
---
*Developed by [Kilian](https://github.com/kilian-gthb)*
