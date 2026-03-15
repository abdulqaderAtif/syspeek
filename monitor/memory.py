import psutil


def bytes_to_gb(value):
    return value / (1024 ** 3)


def get_memory_info():
    memory = psutil.virtual_memory()

    return (
        "Memory Information\n"
        f"Total: {bytes_to_gb(memory.total):.2f} GB\n"
        f"Used: {bytes_to_gb(memory.used):.2f} GB\n"
        f"Available: {bytes_to_gb(memory.available):.2f} GB\n"
        f"Usage: {memory.percent}%"
    )