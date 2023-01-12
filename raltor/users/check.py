
from .models import clientauth


def checkData(request,user_name,user_name1,password,password1 ):
    id = clientauth.getID()
    for i in range(0,len(user_name)):
      if user_name[i][0] == user_name1 and password[i][0] == password1 :
        return id[i][0]
      elif user_name[len(user_name)-1][0] != user_name1 :
        return False
        break
