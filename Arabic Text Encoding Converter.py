# DangerousAngel
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python script.py input_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = f"converted_{input_file}"

try:
    with open(input_file, 'r', encoding='windows-1256') as src:
        with open(output_file, 'w', encoding='utf-8') as dst:
            for line in src:
                dst.write(line)
    print(f"File converted successfully: {output_file}")
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found")
except Exception as e:
    print(f"An error occurred: {e}")
