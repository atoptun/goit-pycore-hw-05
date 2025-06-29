import sys
from datetime import datetime
from collections import Counter, namedtuple


LogItem = namedtuple("LogItem", ["time", "level", "message"])


def load_logs(file_path: str) -> list[LogItem]:
    result = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = parse_log_line(line)
                if record:
                    result.append(record)
    except IOError as e:
        print(f"Load file error: {e.strerror}")
    return result


def parse_log_line(line: str) -> LogItem|None:
    # line format: 2024-01-22 13:30:30 INFO Scheduled maintenance.
    try:
        date, time, level, *msg = line.split()
        result = LogItem(
            time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S"),
            level = level.upper(),
            message = " ".join(msg),
        )
        return result
    except Exception as e:
        # print(e)
        return None # silent. line skipped - wrong format


def count_logs_by_level(logs: list[LogItem]) -> dict:
    result = Counter([log.level for log in logs])
    return  result


def display_log_counts(counts: dict):
    print(f"Level\t|Amont", "-"*15, sep="\n")
    for level, amount in counts.items():
        print(f"{level}\t|{amount}")
    print()
    

def filter_logs_by_level(logs: list[LogItem], level: str|None = None) -> list[LogItem]:
    if level is None:
        return []
    level = level.upper()
    return list(filter(lambda l: level == "ALL" or l.level == level, logs))


def display_logs(logs: list[LogItem], level: str|None):
    if not logs:
        return
    print(f"Details log for level '{level}'")    
    for log in logs:
        print(f"{log.time.strftime("%Y-%m-%d %H:%M:%S")} {log.level} {log.message}")



info = """
Command format: python3 task_03.py <path> <level>
path\tpath to log file
level\tINFO|DEBUG|ERROR|WARNING|ALL
"""

def main():
    print("Log analyzer.\n")
    if len(sys.argv) == 1:
        print(info)
        return

    file_path = ""
    show_level = None
    if len(sys.argv) >= 2:
        file_path = sys.argv[1].strip()
    if len(sys.argv) >= 3:
        show_level = sys.argv[2].strip().upper()

    logs = load_logs(file_path)
    if not logs:
        return
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    display_logs(filter_logs_by_level(logs, show_level), show_level)


if __name__ == "__main__":
    main()
