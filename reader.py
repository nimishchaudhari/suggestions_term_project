#Script to extract interesting data for categorization

import csv

def extraction_of_features(filename):
    """
    This is to extract interesting features for this task
    Rows are: Type de manifestation , Catégorie de la manifestation , Thème de la manifestation
    
    Output: Dictionary file in following format
    {
        ID : {
            type : [t1,t2],
            category : [c1,c2],
            theme : [th1,th2]            
        }
    }
    
    
    """
    dict_item = {}
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     # This code is to take the csv's interesting rows 
        for row in spamreader:                              # And put it into a dictionary
            dict_item[row[0]] = {
                "type":row[16].split(","),
                "category":row[17].split(","),
                "theme":row[18].split(",")
            }
    dict_item.pop("Identifiant")        
    return dict_item


extracted = extraction_of_features("agenda_csv.csv")

print(extracted)