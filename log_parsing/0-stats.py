#!/usr/bin/python3
"""Module script that reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Prints total file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_counts = {}
    allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 9:
                continue

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue

            total_size += file_size

            if status_code in allowed_codes:
                status_counts[status_code] = (
                    status_counts.get(status_code, 0) + 1)

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    if line_count == 0 or line_count % 10 != 0:
        print_stats(total_size, status_counts)
