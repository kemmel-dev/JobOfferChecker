# JobOfferChecker
A simple Python web scraper that checks whether there is a vacancy available on a given URL and, if so, sends me an e-mail.

# Dependencies

- Python 3
- Requests (HTTP library module)
- MIMETEXT (should come with Python 3)
- MIMEMULTIPART (should come with Python 3)

You may have to run 
`pip3 install requests` if you haven't already done so.

# How to use

First check whether the dependencies have been installed, then follow the instructions down below.

Now ensure your Google Account settings allow insecure apps to access your account. (See: https://support.google.com/accounts/answer/185833 )

## auto_job_offer_checker.py 
Open the file in a text editor, enter your credentials (be sensible about this, it's probably a better idea to create a throwaway e-mail address for this purpose since you'll be storing your credentials in plaintext) and then set up your computer to run this script periodically (see https://www.jcchouinard.com/python-automation-using-task-scheduler/ ).

## man_job_offer_checker.py 
Open the file in a text editor, enter your credentials and then run the script whenever you want to check for vacancy.
