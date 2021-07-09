# Loan qualifier app for Predator Loans

The loan qualifier is a simple application that uses CLI to filter a list of loans based on an applicant's qualifying criteria (credit score, debt outstanding, monthly income, loan amount, and home value)

---

## Technologies

This projects uses Python 3.7 and imports the following packages:

[sys](https://docs.python.org/3/library/sys.html) - For exiting the app when an error occurs.

[fire](https://github.com/google/python-fire) - For the command line interface and entry-point.

[questionary](https://pypi.org/project/questionary/) - For interactive user prompts and dialogs.

[csv](https://docs.python.org/3/library/csv.html) - For CSV file reading and writing

[pathlib](https://docs.python.org/3/library/pathlib.html) - For path-handling operations


---

## Installation Guide

Install the following dependencies before running the application.

```import sys
import fire
import questionary
import csv
from pathlib import Path
```


---

## Usage

1- Launch application

```
python app.py
```

2- First prompt: What is the path to the banking data?
*Input the path to the banking data (path to the CSV file)*

3- Applicant answers the following questions:

*3.1- What's your credit score?*

*3.2- What's your current amount of monthly debt?*

*3.3- What's your total monthly income?*

*3.4- What's your desired loan amount?*

*3.5 - What's your home value?*

4- Save the list of qualifying loans?
*Yes or No*

5- If yes, input the path to save the CSV file with the list of qualifying loans.


---

## Contributors

Aquiba Benarroch

---

## License

*MIT License

Copyright (c) 2021 Aquiba Benarroch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*
