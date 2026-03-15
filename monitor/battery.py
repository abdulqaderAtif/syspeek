import psutil


def get_battery_info():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery Information\nBattery not detected."

    plugged = "Yes" if battery.power_plugged else "No"

    return (
        "Battery Information\n"
        f"Percentage: {battery.percent}%\n"
        f"Charging: {plugged}"
    )