from plyer import notification
import time
from show_notification import show_notification
# Main program
if __name__ == "__main__":
    # Get user input
    title = input("Enter notification title: ")
    message = input("Enter notification message: ")

    # Show the notification
    show_notification(title, message)
    time.sleep(5)  # Wait for 5 seconds before exiting
