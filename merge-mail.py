from mailmerge import MailMerge

'''
Fields used in Word/issue syntax (if applicable)
Botname/subfolder
Business/folder
Process/B
Feature
E# (estimate)
A# (actual)
Summary
'''

list_of_cards = []
Botname = ""
Business = ""
Process = ""
Feature = ""
Estimate = ""
Actual = ""
Summary = ""
issues = "" #batch of issues from github

#########################
# TODO: Get data from Github issues (From git-acces.py)
#########################


#########################
# TODO: For loop for processing each of the cards, putting it into correct format and appending it to the list that will merge the pages.
#########################

for i in issues:
    # Extract each issue's data
    # Parse the strings and assign the variables
    list_of_cards.append("test")


document.merge_pages(ist_of_cards)
