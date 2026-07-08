from scheduler.scheduler import Scheduler
from database.database_manager import DatabaseManager
from database.repositories.scheduler_repository import SchedulerRepository

from config.config import (
    SCAN_INTERVAL_MINUTES,
)


def main():

    scheduler = Scheduler(

        interval_minutes=SCAN_INTERVAL_MINUTES

    )

    scheduler.start()


if __name__ == "__main__":

    main()