#show_notification.py
'''
This file is used to display notification
'''
def show_notification(title, message):
    from plyer import notification
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Display time in seconds
    )