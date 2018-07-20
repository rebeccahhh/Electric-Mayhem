from github import Github
from mergeMail import mergeCards
import sys

# or using an access token
g = Github("d4cfa9c6bc4353c3767c9dd1a2d3628d8f8f0d5a")
#class github.Issue.Issue
#test
def getAllIssues():
    repo = g.get_user().get_repo("Electric-Mayhem")
    all_issues = repo.get_issues();
    mergeCards(all_issues)
    return ("Finished");

            
def getOneSpecificIssue(issueNumber):
    repo = g.get_user().get_repo("Electric-Mayhem")
    issue = repo.get_issue(issueNumber);
    return (issue);
    
def getSpecifiedIssues(cardNumbers):
    cardList = cardNumbers.replace(" ","").split(",")
    print(cardList)
    cards = []
    for item in cardList:
        if (item.find("-") != -1):
            a, b = item.split("-")
            low = int(a)
            high = int(b)
            while (low <= high):
                cards = cards + [getOneSpecificIssue(low)]
                low+=1
        else:
             cards = cards + [getOneSpecificIssue(int(item))]
    mergeCards(cards)
    return("Finished")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        getSpecifiedIssues(sys.argv[1])
    else:
        getAllIssues()

