#!/usr/bin/python3


import sys
import signal
# Function to handle interrupt (CTRL+C)


def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


# Initialize variables
total_size = 0
status_codes = {}

# Set up signal handler for interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    # Process input line by line
    for i, line in enumerate(sys.stdin, 1):
        try:
            # Parse the input line
            parts = line.split()
            ip_address = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                if status_code not in status_codes:
                    status_codes[status_code] = 1
                else:
                    status_codes[status_code] += 1

            # Print statistics every 10 lines
            if i % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

except KeyboardInterrupt:
    # Handle keyboard interrupt (CTRL+C)
    print_stats()
    sys.exit(0)
