# Python File Handling Scripts

This repository contains two Python scripts, `file.py` and `append.py`, which demonstrate essential file handling operations such as reading, writing, and appending data in files.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Usage](#usage)
4. [Examples](#examples)
   - [file.py Examples](#filepy-examples)
   - [append.py Examples](#appendpy-examples)
5. [Requirements](#requirements)
6. [License](#license)

---

## Overview

### file.py
- Reads the contents of a file named `sample.txt`.
- Handles errors if the file does not exist.

### append.py
- Performs the following operations on a file named `output.txt`:
  - Writes user-provided text to the file.
  - Appends additional user-provided text.
  - Displays the updated file contents.

---

## Features

### file.py
1. Opens `sample.txt` in read mode.
2. Displays the file content if it exists.
3. Handles `FileNotFoundError` if the file is not present.

### append.py
1. Creates or opens `output.txt` and writes user input to it.
2. Appends additional text provided by the user.
3. Reads and displays the final content of `output.txt`.

---

## Usage

1. Clone this repository or download the scripts.
2. Place `sample.txt` in the same directory as `file.py` (if it exists).
3. Run the scripts as follows:
   - To run `file.py`:
     ```bash
     python file.py
     ```
   - To run `append.py`:
     ```bash
     python append.py
     ```

4. Follow the prompts for user input as needed.

---

## Examples

### file.py Examples

#### Case 1: `sample.txt` Exists
```bash
Reading File Content:
![image](https://github.com/user-attachments/assets/7f1cbdb9-b186-43cb-acb6-f58e335e9a31)

append.py Examples
Example Output
bash
Copy
Edit
![image](https://github.com/user-attachments/assets/b50cc23c-b33e-40c6-ab69-7f5edbd23bff)


#### Notes
For file.py, if sample.txt is not available, the script will only display an error and exit.

For append.py:

The file output.txt will be created if it does not already exist.

Writing operations overwrite existing content, while appending preserves it.
