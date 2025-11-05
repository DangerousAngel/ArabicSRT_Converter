# DangerousAngel
import os
import sys

def convert_file(filename):
    try:
        with open(filename, 'r', encoding='windows-1256') as f:
            content = f.read()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Converted: {filename}")
    except Exception as e:
        print(f"Error converting {filename}: {e}")

def convert_all_srt_files():
    files = [f for f in os.listdir('.') if f.lower().endswith('.srt')]
    if not files:
        print("No .srt files found in the current directory.")
        return
    for file in files:
        convert_file(file)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            convert_file(filename)
        else:
            print(f"File not found: {filename}")
        return
    print("Choose an option:")
    print("a - Convert all .srt files in the current directory")
    print("s - Convert a single .srt file")

    choice = input("Enter your choice (a/s): ").strip().lower()

    if choice == 'a':
        convert_all_srt_files()
    elif choice == 's':
        filename = input("Enter the filename (with .srt extension): ").strip()
        if os.path.isfile(filename):
            convert_file(filename)
        else:
            print(f"File not found: {filename}")
    else:
        print("Invalid choice. Please enter 'a' or 's'.")

if __name__ == "__main__":
    main()
