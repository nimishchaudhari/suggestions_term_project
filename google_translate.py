from googletrans import Translator
import pandas as pd

data=pd.read_csv("./agenda-des-manifestations-culturelles-so-toulouse.csv",sep=';')
translator = Translator()
Descriptif_long_eng=[]
for i in range(len(data['Descriptif long'])):
    string=data['Descriptif long'][i]
    result=translator.translate(string,dest='en',src='fr')
    Descriptif_long_eng.append(result.text)
data['Descriptif long_eng']=Descriptif_long_eng
writer = pd.ExcelWriter('new-agenda-des-manifestations-culturelles-so-toulouse.xlsx')
data.to_excel(writer)
writer.save()