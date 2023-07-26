import ReadEmails as RE
import TextingService as TS
import ScheduleSending as SS
import os
import time


def clear_console():
    os.system('cls')


while True:
    try:
        subjCommand, reminder = (
            RE.get_Email.process_latest_email_subject())
        sCommand = subjCommand.lower().strip()
        rem = reminder.strip()
    except Exception as e:
        print("couldnt find an email in the unseen")
        time.sleep(3)
        clear_console()
        time.sleep(0.5)
    else:
        break

try:
    if sCommand == 'rm2':
        try:
            SS.Scheduled_Message(1, rem, 4).schedule_message()
        except:
            print("couldnt find an email in the unseen")
except:
    print("failed to execute")
finally:
    print("finished")
