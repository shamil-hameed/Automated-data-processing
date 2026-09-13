import re
#this messy data is provided by AI     
messy_names = ["   john SMITH  ", "alice johnson", "BOB MARLEY", "  charlie   brown ", "", 
    "  ", "david  jones", "EMILY   watson", "frank_miller", "grace.kelly", 
    "HENRY 8", "   ", "   iSAbella  tUrner  ", "JACKSON...", "karen!!", 
    "LEO  ", "  mia  ", "NATHAN", "oliver  TWIST", "  penelope  ", 
    "QUINN", "  ryan  reynolds  ", "SAMANTHA", "thomas   AE", "URSULA", 
    "  victor  ", "WENDY_darling", "  XAVIER  ", "yolanda", "ZACHARY", 
    "aaron smith", "  BART simpson  ", "  ", "CHLOE", "  daniel  ", 
    "emma  stone", "   FRED   ", "george  w", "  hannah  ", "IAN", 
    "julia   roberts", "KEVIN   ", "  lisa  ", "matthew   ", "  NINA  ", 
    "oscar", "  paula  ", "quentin", "  rachel  ", "steven   spielberg", 
    "  tina  ", "UMBERTO", "  valerie  ", "william  ", "   ", 
    "YASMIN", "zane", "  AMY  ", "brian_O'conner", "  catherine  ", 
    "diana  ", "  EDWARD  ", "fiona", "  GARY  ", "helen  ", 
    "  isaac  ", "jessica   ALBA", "kyle", "  LAURA  ", "marcus  ", 
    "  NATALIE  ", "owen  ", "  PAIGE  ", "quincy", "  REBECCA  ", 
    "simon", "  TAYLOR  ", "ulysses", "  VANESSA  ", "walter", 
    "XENA", "  YVONNE  ", "zack", "  arthur  ", "BEATRICE", 
    "  connor  ", "DOMINIC", "  elena  ", "FELIX", "  gillian  ", 
    "HARVEY", "  iris  ", "JASON", "  katie  ", "LEWIS", 
    "  megan  ", "NOAH", "  OPHELIA  ", "patrick", "  QUINTON  "
]
standard_names=[]
#for stripping the whitespaces and to make the name to lower case 
for name in messy_names:
    stripped=name.strip().lower()
    
#for removing empty names from list
    if stripped =='':
        continue
    
#for removing other characters except alphabet and removing  extra spaces 
# making the first character alphabet  and sorting in alphabetical order
    name_s=re.sub(r'[^a-zA-Z ]', '',stripped)
    perfect_name=" ".join(name_s.split()).title()
    perfect_name=perfect_name[0].upper()+ perfect_name[1:]
    standard_names.append(perfect_name) 
    standard_names.sort()
    
print(standard_names)                 