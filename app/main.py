import time

from app.batch.batch_dispatcher import send_batch


def run():
    while True:
        send_batch(
            endpoint="http://localhost:5000/api/phone_tracker",
            batch_size=3
        )
        time.sleep(2)

if __name__ == '__main__':
    run()