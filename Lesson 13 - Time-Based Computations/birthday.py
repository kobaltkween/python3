import logging
from datetime import datetime, timedelta
from optparse import OptionParser

logging.basicConfig(filename = "birthday.log", level = logging.DEBUG)

class InvalidDateFormat(Exception):
    pass

def stringToDate(date):
    """
    Converts 'MM-DD-YYYY' to a date/time object
        or throws an InvalidDateFormat exception
    """
    try: 
        # create a datetime object from the date value
        formatterString = "%m-%d-%Y"
        birthday = datetime.strptime(date, formatterString)
    except ValueError as e:
        # Log the format error then raise it again so it can be handled gracefully.
        logging.error(e)
        raise InvalidDateFormat(e)
    return birthday

def birthdayCounter(birthday):
    """
    Returns the number of days until your birthday.
    """
    now = datetime.now()
    birthday = stringToDate(birthday)
    logging.debug("birthday : {}".format(birthday))
    # Construct the upcoming birthday from this year, your birthday month, and birthday day
    upcoming = datetime(now.year, birthday.month, birthday.day)
    logging.debug("upcoming: {}".format(upcoming))
    # Make sure that upcoming is in the future, not the past
    if upcoming < now:
        upcoming = upcoming + timedelta(365)
        logging.debug("fixed upcoming {}".format(upcoming))
    duration = upcoming - now
    logging.debug("duration: {}".format(duration))
    # Return only the days
    return duration.days
    
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-b", "--birthday", dest = "birthday", action = "store",
                      help = "Your birthday in MM-DD-YYY format")
    options, args = parser.parse_args()
    formatErrorMessage = "birthday.py requires a date in MM-DD-YYYY format"
    if not options.birthday:
        parser.error(formatErrorMessage)
    try:
        print(birthdayCounter(options.birthday))
    except InvalidDateFormat:
        parser.error(formatErrorMessage)