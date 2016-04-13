from datetime import datetime, timedelta

now = datetime.now()
delta = timedelta(31) # create a timedelta of 31 days
delivery = now + delta
print("Today is: %s" % now.strftime("%d"))
print("Delivery: %s " % delivery.strftime("%d"))