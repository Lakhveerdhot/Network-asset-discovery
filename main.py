"""
Network Asset Discovery Platform
"""

from scanner.scan_engine import ScanEngine


def main():

    engine = ScanEngine()

    engine.run()


if __name__ == "__main__":

    main()