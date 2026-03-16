import psutil


def bytes_to_gb(value):
    return value / (1024 ** 3)


def get_disk_info():
    disk = psutil.disk_usage("/")

    return (
        "Disk Information\n"
        f"Total: {bytes_to_gb(disk.total):.2f} GB\n"
        f"Used: {bytes_to_gb(disk.used):.2f} GB\n"
        f"Free: {bytes_to_gb(disk.free):.2f} GB\n"
        f"Usage: {disk.percent}%"
    )