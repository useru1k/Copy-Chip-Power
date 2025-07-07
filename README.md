# CopyChip Power

📝 A simple cross-platform CLI tool to copy specific lines or ranges from a file directly to the system clipboard using Python — no external libraries or commands required.

### ✨ Features
  - Copy a specific line from a file
  - Copy a range of lines
  - Copy the entire file content
  - Cross-platform (Windows, macOS, Linux)
  - Uses only standard Python libraries

### Installation
No installation required! Just clone the repository and run the script using Python 3.
```
git clone https://github.com/your-username/copyPower.git
cd copyPower
python copychip.py --help
```

## ❓ Why I Made This
As a Linux user, I often work directly in the terminal — running tools, viewing files with cat, head, or less, and needing to copy specific content. However, selecting and copying text with the mouse can be frustrating, especially when the cursor misbehaves or disappears inside the terminal.

On top of that, using Ctrl + C to copy often kills the running process instead of copying the text.

So, I built copyPower — a simple CLI tool to help me copy exact lines, ranges, or entire file content directly to the clipboard without leaving the terminal or relying on the mouse. It's fast, minimal, and makes terminal work more efficient.

### Usage 
```
usage: copychip.py [-h] --file FILE [--line LINE] [--start START] [--end END]
                   [--full]

Copy the text from file to Cilpboard.

options:
  -h, --help     show this help message and exit
  --file FILE
  --line LINE    Copy the one line from the file
  --start START  Start line number in range
  --end END      End line number in range
  --full         Do full copy
```

### 🧪 Examples
- Copy line 5 from a file
```
python copychip.py --file example.txt --line 5
```
- Copy lines 10 to 15
```
python copychip.py --file example.txt --start 10 --end 15
```
- Copy the entire file
```
python copychip.py --file example.txt --full
```


### Contributing
- Contributions, suggestions, and issues are welcome. Please open an issue or submit a pull request.
