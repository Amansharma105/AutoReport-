from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def generate_report():
    print("Generating scheduled report...")

scheduler.add_job(generate_report, "interval", minutes=1)

if __name__ == "__main__":
    scheduler.start()
