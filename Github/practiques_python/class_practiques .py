from tkinter import filedialog
import tkinter as tk
import pandas as pd
# for an earlier version of Excel, you may need to use the file extension of 'xls'
df = pd.read_excel(r'/Users/fcolell/Desktop/materials.xlsx')
print(df)
# Python3 code here creating class


class mat:
    def __init__(self, matfam, factor):
        self.matfam = matfam
        self.factor = factor


# creating list
list = []

# appending instances to list
list.append(mat('PP', 1.03))
list.append(mat('POM', 1.002))
list.append(mat('PA66', 1.000005))

for obj in list:
    print(obj.matfam, obj.factor, sep=' ')

# We can also access instances attributes
# as list[0].matfam, list[0].factor
# and so on.

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
canvas1.pack()


def getExcel():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)
    print(df)


browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel,
                               bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
