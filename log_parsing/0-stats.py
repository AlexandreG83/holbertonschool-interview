#!/usr/bin/python3
"""
Reads log lines from stdin and computes streaming statistics.
Prints summary every 10 valid lines or on interruption.
"""

import sys
import re
from collections import defaultdict


LOG_PATTERN = re.compile(
    r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def extract_metrics(line):
    """
    Try to extract status code and file size from a log line.

    Returns:
        tuple (status_code or None, size or None)
        Returns (None, None) if line does not match expected format.
    """
    match = LOG_PATTERN.match(line)
    if not match:
        return None, None

    status_raw, size_raw = match.groups()

    try:
        return int(status_raw), int(size_raw)
    except ValueError:
        return None, None


def print_stats(total_bytes, status_counts):
    """Display aggregated metrics sorted by status code."""
    print(f"File size: {total_bytes}")

    for code in sorted(status_counts.keys()):
        if status_counts[code] == 0:
            continue
        print(f"{code}: {status_counts[code]}")


def run():
    """Main loop reading stdin and triggering periodic reporting."""
    tracked_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    counters = defaultdict(int)
    total_size = 0
    line_counter = 0

    try:
        for raw in sys.stdin:
            line_counter += 1

            res = extract_metrics(raw.strip())

            if res != (None, None):
                status, size = res
                total_size += size
                if status in tracked_codes:
                    counters[status] += 1

            if line_counter % 10 == 0:
                print_stats(total_size, counters)

    except KeyboardInterrupt:
        print_stats(total_size, counters)
        raise
    else:
        print_stats(total_size, counters)


if __name__ == "__main__":
    run()