import configparser
from optparse import OptionParser
import shelve
import sys

config = configparser.RawConfigParser()
config.read("v:/workspace/Python3Lesson12/src/addressbook.cfg")
shelfLocation = config.get("database", "file")

class InvalidEmail(Exception):
    pass

def validateEmail(email):
    if "@" not in email:
        raise InvalidEmail("Invalid email: " + email)

def emailAdd(email):
    validateEmail(email)
    shelf = shelve.open(shelfLocation)
    if "emails" not in shelf:
        shelf["emails"] = []
    emails = shelf["emails"]
    if email in emails:
        message = False, "Email {0} already in address book". format(email)
    else:
        emails.append(email)
        message = True, "Email {0} added to address book".format(email)
    shelf["emails"] = emails
    shelf.close()
    return message

def emailDelete(email):
    validateEmail(email)
    shelf = shelve.open(shelfLocation)
    if "emails" not in shelf:
        shelf["emails"] = []
    emails = shelf["emails"]
    try:
        emails.remove(email)
        message = True, "Email {} removed from address book".format(email)
    except ValueError:
        message = False, "Email {} was not in the address book".format(email)
    shelf["emails"] = emails
    shelf.close()
    return message

def emailDisplay():
    shelf = shelve.open(shelfLocation)
    emails = shelf["emails"]
    shelf.close()
    text = ""
    for email in emails:
        text += email + "\n"
    return True, text

def main(options):
    "routes requests"
    if options.action == "add":
        return emailAdd(options.email)
    elif options.action == "delete":
        return emailDelete(options.email)
    elif options.display == True:
        return emailDisplay()

if __name__ == "__main__":
    shelf = shelve.open(shelfLocation)
    if "emails" not in shelf:
        shelf["emails"] = []
    shelf.close()
    parser = OptionParser()
    parser.add_option("-a", "--action", dest = "action", action = "store", help = "Requires - e option. Actions: add/delete")
    parser.add_option("-e", "--email", dest = "email", action = "store", help = "Email used in the -a option")
    parser.add_option("-d", "--display", dest = "display", action = "store_true", help = "Show all emails.")
    options, args = parser.parse_args()
    # validation
    if options.action and not options.email:
        parser.error("option -a requires option -e")
    elif options.email and not options.action:
        parser.error("option -e requires option -a")
    try:
        print(main(options)[1])
    except InvalidEmail:
        parser.error("option -e requires a valid email address")