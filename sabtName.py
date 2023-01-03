def check_registration_rules(**userpass):
    
    
    for i in list(userpass):
        if i == "quera" or i == "codecup" or len(i)<4 or len(userpass[i])< 6 or userpass[i].isnumeric()==True:
            userpass.pop(i)
            
    return list(userpass)
    
  
    

# check_registration_rules(saeed='1234567', ab='afj$L12')



def check_registration_rules(**kwargs):
    list = []
    for key, value in kwargs.items():
        if key != "quera" and key != "codecup" and len(key) >= 4:
            if len(value) >= 6 and not value.isnumeric():
                list.append(key)
    return list           
print(check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))

