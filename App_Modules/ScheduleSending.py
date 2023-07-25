import schedule
import time
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

        while True:
            print("Getting ready to send")
            schedule.run_pending()
            time.sleep(1)


# Call the scheduling function with the message and wait time
message1 = Scheduled_Message(1, "hey", 5)
message1.schedule_message()
