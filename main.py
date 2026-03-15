import argparse
from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_info
from monitor.disk import get_disk_info
from monitor.system import get_system_info
from monitor.battery import get_battery_info


def main():
    parser = argparse.ArgumentParser(
        description="Linux System Monitor CLI"
    )

    parser.add_argument("--cpu", action="store_true", help="Show CPU usage")
    parser.add_argument("--memory", action="store_true", help="Show memory usage")
    parser.add_argument("--disk", action="store_true", help="Show disk usage")
    parser.add_argument("--system", action="store_true", help="Show system info")
    parser.add_argument("--battery", action="store_true", help="Show battery info")
    parser.add_argument("--all", action="store_true", help="Show all information")

    args = parser.parse_args()

    if args.cpu or args.all:
        print(get_cpu_usage())
        print()

    if args.memory or args.all:
        print(get_memory_info())
        print()

    if args.disk or args.all:
        print(get_disk_info())
        print()

    if args.system or args.all:
        print(get_system_info())
        print()

    if args.battery or args.all:
        print(get_battery_info())
        print()

    if not any(vars(args).values()):
        parser.print_help()


if __name__ == "__main__":
    main()