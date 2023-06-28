from pynotifier import Notification

Notification(
    title="Notification",
    description="welcome to Notifications, you have 5 unread messages",
    duration=30,
    urgency=Notification.URGENCY_CRITICAL
).send()
