agentCode = input('Enter Agent Code between 101-999 : ')
seniorctzn = input('Senior Citizen? [Yes/No] : ')
newCust = input('New Customer? [Yes/No] : ')

if(newCust.lower() == "no"):   
    PreferredAgent = input('Prefered Agent? [Yes/No] : ')
elif(newCust.lower() == "yes"):
    PreferredAgent = "no"


if(agentCode == "999"):
    agentName = "Jane"
    agentType = "staff"
    
elif (agentCode == ""):
    agentName = "Random"
    agentType = "self"
    
else:
    agentName = "Random"
    agentType = "general"


if (agentCode is not ""):
    print("https://somecoolcompany.com/buy?agentCode={" + agentCode +
          "}&preferredAgent={"+PreferredAgent.lower()+
          "}&agentType={" + agentType + "}")
else:
    print("https://somecoolcompany.com/buy?preferredAgent={"+PreferredAgent.lower()+
          "}&agentType={" + agentType + "}")
    






