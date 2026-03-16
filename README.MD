# SysPeek

> A lightweight **Linux System Monitor CLI** built with Python.

SysPeek lets you instantly inspect your system's vital stats — CPU, memory, disk, battery, and more — right from your terminal. No bloat, no GUI, just clean and fast output.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

| Flag          | Description                                     |
|---------------|-------------------------------------------------|
| `--cpu`       | CPU usage percentage and logical core count     |
| `--memory`    | Total, used, and available RAM                  |
| `--disk`      | Total, used, and free disk space                |
| `--battery`   | Battery percentage and charging state           |
| `--system`    | OS name, hostname, kernel, machine, and uptime  |
| `--all`       | Display all of the above at once                |

---

## Tech Stack

- **Python 3.10+**
- **[psutil](https://pypi.org/project/psutil/)** — cross-platform system info library

---

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/abdulqaderAtif/syspeek.git
cd syspeek
```

**2. Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install the package:**

```bash
pip install .
```

---

## Usage

```bash
syspeek [--cpu] [--memory] [--disk] [--battery] [--system] [--all]
```

| Command             | Description              |
|---------------------|--------------------------|
| `syspeek --cpu`     | Show CPU usage           |
| `syspeek --memory`  | Show memory usage        |
| `syspeek --disk`    | Show disk usage          |
| `syspeek --battery` | Show battery status      |
| `syspeek --system`  | Show system information  |
| `syspeek --all`     | Show everything at once  |

### Sample Output

```text
CPU Information
Usage: 12.3%
Logical cores: 8

Memory Information
Total: 15.56 GB
Used: 6.42 GB
Available: 9.14 GB
Usage: 41.3%

Disk Information
Total: 476.84 GB
Used: 198.22 GB
Free: 278.62 GB
Usage: 41.6%

System Information
System: Linux
Node Name: my-machine
Release: 6.8.0-52-generic
Machine: x86_64
Processor: x86_64
Uptime: 3h 27m 14s

Battery Information
Percentage: 87%
Charging: Yes
```

---

## Project Structure

```text
syspeek/
├── syspeek/
│   ├── __init__.py
│   ├── main.py          ← CLI entry point
│   └── monitor/
│       ├── __init__.py
│       ├── cpu.py       ← CPU stats
│       ├── memory.py    ← RAM stats
│       ├── disk.py      ← Disk stats
│       ├── battery.py   ← Battery info
│       └── system.py   ← OS & uptime
├── pyproject.toml
├── README.MD
└── .gitignore
```

---

## License

This project is licensed under the [MIT License](LICENSE).
