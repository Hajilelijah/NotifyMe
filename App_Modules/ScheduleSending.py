import schedule
import time
from tqdm import tqdm
import TextingService
from functools import partial


def send_message(message):
    # Call the TextingService.Text.message() method with the provided message
    TextingService.Text.message(message)


class Scheduled_Message:
    def __init__(self, message_id, message, wait_time):
        self.message_is = message_id
        self.message = message
        self.wait_time = wait_time

    def schedule_message(self):
        # wait is in ten seconds
        # Create a callable function with predefined message argument
        send_with_message = partial(send_message, self.message)

        # Schedule the message sending job
        schedule.every(self.wait_time).seconds.do(send_with_message)

        count = 0

        # Use tqdm to create a progress bar
        for i in tqdm(range(self.wait_time + 1), desc="Processing", ncols=100):
            # Simulate some work (replace this with your actual processing code)

            schedule.run_pending()
            time.sleep(1)

            time.sleep(0.1)


# Example loop to simulate progress
total_iterations = 100


# Call the scheduling function with the message and wait time
# message1 = Scheduled_Message(1, "hey", 5)
# message1.schedule_message()
