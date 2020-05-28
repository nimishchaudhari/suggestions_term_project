import pandas as pd
from sklearn import model_selection
from sklearn.cluster import KMeans
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def data_preprocess(intrests_list):
    data = pd.read_csv("agenda-des-manifestations-culturelles-so-toulouse.csv", sep=';')
    # print(data)
    data['Type de manifestation'] = data['Type de manifestation'].fillna('Unspecifiled_1')
    data['Catégorie de la manifestation'] = data['Catégorie de la manifestation'].fillna('Unspecifiled_2')
    data['Thème de la manifestation'] = data['Thème de la manifestation'].fillna('Unspecifiled_3')
    for i, m in enumerate(data['Type de manifestation']):
        for n in intrests_list:
                if m.find(n) != -1:
                    print(data.iloc[i])
    # extract new features from original dataset
    mlb = MultiLabelBinarizer()
    encoded1 = pd.DataFrame(mlb.fit_transform(data['Type de manifestation'].str.split(', ')), columns=mlb.classes_)
    encoded2 = pd.DataFrame(mlb.fit_transform(data['Catégorie de la manifestation'].str.split(', ')), columns=mlb.classes_)
    encoded3 = pd.DataFrame(mlb.fit_transform(data['Thème de la manifestation'].str.split(', ')), columns=mlb.classes_)
    data1 = pd.concat([data['Identifiant'], encoded1, encoded2, encoded3], axis=1)
    # print(data1.iloc[0])
    # print(data1.iloc[:,[2]])
    print(data1)
    # pca
    pca = PCA(n_components=3)
    x = pca.fit_transform(data1.iloc[:,1:-1])
    print(x)
    for i in x:
        plt.scatter(i[1], i[2])
    plt.show()

def suggestion():
    if not (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get()
        or var7.get()):
        messagebox.showerror("You have not selected a interest!")
    intrests_list = []
    if var1.get():
        intrests_list.append('Musique')
    if var2.get():
        intrests_list.append('Culturelle')
    if var3.get():
        intrests_list.append('Insolite')
    if var4.get():
        intrests_list.append('Danse')
    if var5.get():
        intrests_list.append('Manifestation commerciale')
    if var6.get():
        intrests_list.append('Sports et loisirs')
    if var7.get():
        intrests_list.append('Nature et détente')
    data_preprocess(intrests_list)

#build user interface
window = tk.Tk()
window.title("Toulouse Go Out!")
intrests = tk.LabelFrame(window, text="Choose your intrests", font='Calibri 12 bold', padx=5, pady=5)
var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Musique', variable=var1)
c1.pack()
var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='Culturelle', variable=var2)
c2.pack()
var3 = tk.IntVar()
c3 = tk.Checkbutton(window, text='Insolite', variable=var3)
c3.pack()
var4 = tk.IntVar()
c4 = tk.Checkbutton(window, text='Danse', variable=var4)
c4.pack()
var5 = tk.IntVar()
c5 = tk.Checkbutton(window, text='Manifestation commerciale', variable=var5)
c5.pack()
var6 = tk.IntVar()
c6 = tk.Checkbutton(window, text='Sports et loisirs', variable=var6)
c6.pack()
var7 = tk.IntVar()
c7 = tk.Checkbutton(window, text='Nature et détente', variable=var7)
c7.pack()
button = tk.Button(window, text="Show me events", command=suggestion)
button.pack()
window.mainloop()