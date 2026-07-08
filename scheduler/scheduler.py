"""
Network Scan Scheduler
"""

import time
from datetime import datetime, timedelta
from scanner.scan_engine import ScanEngine
from utils.logger import setup_logger
from database.database_manager import DatabaseManager
from database.repositories.scheduler_repository import SchedulerRepository

logger = setup_logger()

class Scheduler:
    def __init__(
        self,
        interval_minutes=30
    ):

        self.interval = interval_minutes

        self.engine = ScanEngine()

        self.database = DatabaseManager()

        self.scheduler_repo = SchedulerRepository(
            self.database
        )

        self.previous_state = None

    # -------------------------------------

    def start(self):

        print()

        print("=" * 70)

        print("NETWORK ASSET DISCOVERY SCHEDULER")

        print("=" * 70)

        print()

        print(

            f"Scan Interval : {self.interval} Minutes"

        )

        print()

        while True:

            self.interval = self.scheduler_repo.interval()

            if self.scheduler_repo.is_enabled():

                if self.previous_state != "running":

                    print()

                    print("=" * 70)

                    print("Scheduler Running")

                    print("=" * 70)

                    print()

                    logger.info("Scheduler Running")

                    self.previous_state = "running"

                last_enabled = datetime.strptime(

                    self.scheduler_repo.last_enabled(),

                    "%Y-%m-%d %H:%M:%S"

                )

                elapsed = (

                    datetime.now()

                    - last_enabled

                ).total_seconds()

                if elapsed >= self.interval * 60:

                    logger.info(

                        "Scheduled Scan Started"

                    )

                    print(

                        "Starting Scan...\n"

                    )

                    hosts = self.engine.run()

                    print()

                    logger.info(

                        "Scheduled Scan Completed"

                    )

                    print()

                    print(

                        f"Discovered {len(hosts)} device(s)."

                    )

                    print()

                    print(

                        "Scan Completed."

                    )

                    self.scheduler_repo.enable()

                else:

                    remaining = (

                        self.interval * 60

                        - elapsed

                    )

            else:

                if self.previous_state != "paused":

                    print()

                    print("=" * 70)

                    print("Scheduler Paused")

                    print("=" * 70)

                    print()

                    logger.info("Scheduler Paused")

                    self.previous_state = "paused"
                    
            time.sleep(1)