import platform
import psutil
from datetime import datetime


def format_uptime(seconds):
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"


def get_system_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = (datetime.now() - boot_time).total_seconds()

    return (
        "System Information\n"
        f"System: {platform.system()}\n"
        f"Node Name: {platform.node()}\n"
        f"Release: {platform.release()}\n"
        f"Version: {platform.version()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}\n"
        f"Uptime: {format_uptime(uptime_seconds)}"
    )