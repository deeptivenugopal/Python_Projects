import time
from plyer import notification

if __name__ == "__main__":
	while True:
		notification.notify(
			title = "REMINDER!!",
			message = "Demo",
			#app_icon= "Reminder",
			timeout = 60
		)
		time.sleep(60)

