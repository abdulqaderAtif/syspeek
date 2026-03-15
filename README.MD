# SysPeek

A simple **Linux System Monitor CLI** built with Python.

SysPeek allows you to quickly inspect system resources directly from the terminal such as CPU usage, memory usage, disk usage, battery status, and system information.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Battery status
- System information
- CLI interface using argparse
- Lightweight and fast

## Tech Stack

- Python
- psutil
- argparse
- Linux system information

## Installation

Clone the repository:

```bash
git clone https://github.com/abdulqaderAtif/syspeek.git
cd syspeek
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI tool with the following commands:

Show CPU usage:

```bash
python main.py --cpu
```

Show memory usage:

```bash
python main.py --memory
```

Show disk usage:

```bash
python main.py --disk
```

Show battery information:

```bash
python main.py --battery
```

Show system information:

```bash
python main.py --system
```

Show all information:

```bash
python main.py --all
```

## Project Structure

```
syspeek
│
├── main.py
├── monitor
│   ├── battery.py
│   ├── cpu.py
│   ├── disk.py
│   ├── memory.py
│   └── system.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- Live monitoring mode

- Network statistics

- Top processes by CPU usage

- Colored CLI output

- Packaging as an installable CLI tool
