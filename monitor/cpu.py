import psutil


def get_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    cores = psutil.cpu_count(logical=True)

    return (
        "CPU Information\n"
        f"Usage: {usage}%\n"
        f"Logical cores: {cores}"
    )