# Text Analyzer

This project contains a simple Python script that analyzes the content of a text file line by line. It reports the number of characters, the number of uppercase letters, and the percentage of uppercase letters for each line.

## Files

- `analyze_text.py`: The main Python script that performs the analysis.
- `sample.txt`: A sample text file to be analyzed. You can replace this with any `.txt` file of your choice.

## How It Works

The script reads the text file line by line and calculates the following for each line:

- **Total characters** (excluding leading/trailing whitespace)
- **Uppercase characters**
- **Percentage of uppercase characters**

## Sample Input (`sample.txt`)
Hello World!
THIS is a TEST.
python Is FUN

## Sample Output

Line Chars Uppercase % Upper
1 12 2 16.67%
2 15 9 60.0%
3 13 4 30.77%

## Usage

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/mg555555/SC00041_Exercise1.git
   cd text-analyzer

Run the script:

   ```bash
   python3 analyze_text.py
   ```
## License 

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
