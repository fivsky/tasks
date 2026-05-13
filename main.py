import sys
import datetime
import platform


def main():
    print("Hello, World!")
    print(f"Toay is {datetime.date.today()}")
    print(f"Python version: {platform.python_version()}")

if __name__ == "__main__":
    main()

