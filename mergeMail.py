from stringParse import stringParse
from mailmerge import MailMerge
from github import Github

def mergeCards(cards):
    with MailMerge("documents/HackathonTemplate.docx") as document:
        
        '''
        Fields used in Word/issue syntax (if applicable)
        Botname/github repo name
        Feature/F: or Feature:
        E# (estimate)/E: or Estimate:
        A# (actual)/A: or Actual:
        Summary
        
        Other card fields
        Business - user defines
        Process - user defines
        '''
        
        listOfCards = []
        botName = "FakeBot"
        businessProcess = "FakeBusiness"
        title = ""
        feature = ""
        estimate = ""
        actual = ""
        summary = ""
        
        
        for card in cards:
            # Extract each issue's data
            # Parse the strings and assign the variables
            # GET SUMMARY
            feature, estimate, actual, summary = stringParse(card.body)
            print ("\n--- " + botName + " - ISSUE #" + str(card.number) + " ---")
            print ("Title:" + card.title + "\nFeature: " + feature + "\nEstimate: " + estimate + "\nActual: " + actual + "\nSummary: " + summary)
            # feature, estimate, actual, summary
            listOfCards.append({'Botname':botName, 'BusinessProcess':businessProcess, 'Title':card.title, 'E#':estimate,'A#':actual,'Summary':summary})
        
        
        document.merge_pages(listOfCards)
        document.write('documents/FinishedCards.docx')
    
