
from topic import Topic
from topic import Subtopic

#Search engine has the 2 key words list, which lists the directory of information and search + key word which searches for that word 
#Ex. search climate change 
#Ex. List 

#Brython Notes in website.html

## type list into list bar to list the info 
#Search bar: 
#List 

## Climate Change Instances 
coral_bleaching = Subtopic("coral bleaching", ["cb link 1", "cb link 2"])
deforestation = Subtopic("deforestation",['https://www.pnas.org/content/116/44/22212#:~:text=Our%20results%20suggest%20a%2010,states%20where%20little%20forest%20remains','d link 2'])
climate_change = Topic("Climate Change", [coral_bleaching, deforestation], )

## Systematic Racism
wealth_gap = Subtopic("Wealth Gap", ["https://books.google.com/books?hl=en&lr=&id=ZhpPAAAAMAAJ&oi=fnd&pg=PR11&dq=institutional+racism+housing&ots=mzHGZMLvjr&sig=Ug4oIWsmLrRRwtns9jIbpv2Wbns#v=onepage&q=institutional%20racism%20housing&f=false", ""])
employment = Subtopic("Employment", ["https://www.tandfonline.com/doi/abs/10.1080/13613324.2011.646255", "https://pure.northampton.ac.uk/en/publications/institutional-racism-in-the-academy-a-case-study]"])
housing_discrimination = Subtopic("Housing Discrimination", ["https://www.tandfonline.com/doi/abs/10.1080/13613324.2011.646255", "https://heinonline.org/HOL/LandingPage?handle=hein.journals/illlr112&div=52&id=&page="])
gov_surveillance = Subtopic("Government Surveillance", ["https://www.democracynow.org/2013/9/17/from_mosques_to_soccer_leagues_inside", "http://www.ap.org/Content/AP-In-The-News/2012/AP-series-about-NYPD-surveillance-wins-Pulitzer"])
incarceration = Subtopic("Incarceration", ["https://www.huffpost.com/entry/the-new-jim-crow-a-mustre_b_3679076", "https://www.naacp.org/criminal-justice-fact-sheet/", "https://www.theatlantic.com/politics/archive/2014/10/mapping-the-new-jim-crow/381617/"])

drug_arrests = Subtopic("Crime and Drug Arrests", ["https://www.nytimes.com/2014/07/29/opinion/high-time-the-injustice-of-marijuana-arrests.html?_r=0",
"https://drugwarfacts.org/chapter/marijuana",
"https://www.colorlines.com/tags/marijuana",
]) #Subtopic of crime and is 3levels down in hierarchy
crime = Subtopic("Crime", ["https://www.tandfonline.com/doi/abs/10.1080/10439463.2012.703198"], [drug_arrests])


discriminatory_immigatrion = Subtopic("Immigration", ["http://www.aljazeera.com/indepth/opinion/2013/03/2013329115414268219.html", "https://www.colorlines.com/articles/how-racist-us-immigration-policy"])
systemic_discrimination = Topic("Systemetic Racism",[wealth_gap, employment, housing_discrimination, gov_surveillance, incarceration, crime, discriminatory_immigatrion], )


issues = [climate_change, systemic_discrimination]



searching = True
while searching:
   #Input is in loop so loop isn't indefinite. Needs ability to exit
  user_input = input("Search bar: \n").lower().title().strip()
  inputted_words = user_input.split()
  #print(inputted_words) #for testing 

  if inputted_words[0] == "List" and inputted_words[-1] =="List": #Makes sure that the is input is requesting a certain topic or article, etc. 
    print("Issues:")
    for issue in issues: 
      issue.recursively_list()
      print("") #For the new line 
  #elif inputted_words[0] == "List": 
  elif inputted_words[0] == "Search":
    print("searching runs")
    print(inputted_words[-1])
    for topic in issues: 
      topic.search(inputted_words[-1])
  #Let's wait a bit before running or I can comment this code out so you can test the kivy 
  elif inputted_words[0] == "Quit": 
    searching = False #just creating an exti func for right now. Since it's a search bar, it won't have this
  else: 
    print()
    
      



#elif input_words(0) == "Search": 

''''
stop = input("Would you like to stop searching (y/n)").lower().strip()
if stop == "y" or "yes" : 
  False


topic=input('What problem in the world are you looking to learn more about? If you are not sure just type issues').lower()

if topic  == "issues": 
    print ("The Biggest Social Justice Issues We Face Today: \n1 – Voting\n2 – Climate Change\n3 – Healthcare\n4 – Refugee Crisis and Immigration\n5 – Body Autonomy\n6 – Racial Injustice\n7 – Gun Violence\n8 – LGBTQ+")
elif topic=='Black Lives Matter':
    print('black lives matter is an organization that wants to create racial equality and help fix systemic racism if you want to help raise awareness or learn more about this topic you can checkout these articles and links')
elif topic =='climate change':
    print("Global warming, the gradual heating of Earth's surface, oceans and atmosphere, is caused by human activity, primarily the burning of fossil fuels that pump carbon dioxide (CO2), methane and other greenhouse gases into the atmosphere .")
elif topic == 'gun violence':
    print("Gun-related violence is violence committed with the use of a gun. Gun-related violence may or may not be considered criminal. Criminal violence includes homicide, assault with a deadly weapon, and suicide, or attempted suicide, depending on jurisdiction.")

'''