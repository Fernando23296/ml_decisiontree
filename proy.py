'''SISTEMA ASISTENTE DE DETECCION DE ESCOLIOSIS'''
'''BRUNO FERNANDO SILVA PLATA'''
from Tkinter import *

import tkSimpleDialog

import tkMessageBox
from sklearn import tree
'''DATASET'''
features = [[1,0,1,5,3],
			[2,0,2,5,2],
			[3,0,5,4,2],
			[4,0,3,5,3],
			[5,0,4,4,2],
			[6,0,7,6,4],
			[7,0,8,7,4],
			[8,0,1,5,3,],
			[9,0,2,4,3],
			[10,0,4,4,3],
			[11,0,9,6,4],
			[12,0,5,4,2],
			[13,0,11,28,6],
			[14,0,9,6,4],
			[15,0,13,30,15],
			[16,0,3,10,8],
			[17,0,2,6,4],
			[18,0,5,8,5],
			[19,0,1,5,3],
			[20,0,2,7,4],
			[21,0,5,15,12],
			[22,0,8,20,15],
			[23,0,9,21,17],
			[24,0,11,21,16],
			[25,0,12,21,17],
			[25,5,2,6,4],
			[25,6,9,21,18],
			[25,7,5,19,16],
			[25,8,12,26,21],
			[25,9,6,21,18],
			[25,10,4,15,13],
			[26,5,7,15,13],
			[26,6,8,16,13],
			[26,7,12,20,17],
			[26,8,11,20,16],
			[26,9,5,13,9],
			[26,10,6,15,13],
			[27,5,8,19,15],
			[27,6,11,23,19],
			[27,7,12,23,20],
			[27,8,14,22,19],
			[27,9,18,30,23],
			[27,10,1,5,4],
			[28,5,17,32,28],
			[28,6,15,27,19],
			[28,7,11,19,18],
			[28,8,12,23,19],
			[28,9,15,36,31],
			[28,10,16,33,29],
			[29,5,1,5,4],
			[29,6,15,28,20],
			[29,7,9,8,6],
			[29,8,13,32,27],
			[29,9,17,26,21],
			[29,10,19,30,28],
			[30,5,11,20,34],
			[30,6,12,19,18],
			[30,7,15,24,20],
			[30,8,14,23,20],
			[30,9,11,19,17],
			[30,10,19,24,21],
			[30,0,12,19,16],
			[31,0,11,21,19],
			[32,0,9,16,13],
			[33,0,7,17,14],
			[34,0,4,11,11],
			[35,0,11,24,21],
			[36,0,18,30,27],
			[37,0,9,15,13],
			[38,0,11,19,17],
			[39,0,21,35,29],
			[40,0,15,26,21],
			[41,0,11,19,19],
			[42,0,14,25,21],
			[43,0,19,39,33],
			[44,0,20,45,39],
			[45,0,21,40,29],
			[46,0,15,27,25],
			[47,0,14,21,20],
			[48,0,17,23,19],
			[49,0,21,39,33],
			[50,0,11,21,18],
			[51,0,29,45,19],
			[52,0,35,45,40],
			[53,0,43,46,41],
			[54,0,23,43,38],
			[55,0,37,48,44],
			[56,0,22,39,36],
			[58,0,29,41,39],	
			[59,0,31,42,38],
			[60,0,35,47,41],
			[61,0,28,41,39],
			[62,0,21,38,31]]


labels =[
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1,
		 1, 
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 2,
		 3,
		 3, 
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3,
		 3]
'''FIN DATASET'''
'''-------'''
'''USO DE ARBOLES DE DECISION'''
clf= tree.DecisionTreeClassifier()
clf=clf.fit(features, labels)

'''USO DE TKINTER PARA INTERFAZ GRAFICA'''
root = Tk()
root.geometry("650x850+0+0")
root.title("Sistema Asistente de Deteccion de Escoliosis")
root.configure(background='white')

Tops = Frame(root, width=90, height=10, bd=1, relief="flat")
Tops.pack(side=TOP)

Botto = Frame(root, width=1350, height=10, bd=1, relief="flat")
Botto.pack(side=TOP)



lblInfo=Label(Tops, font=('Helvetica',30,'bold'), text="Sistema Asistente de \n Deteccion de Escoliosis",
			bd=16).grid(row=0,column=0)

inBotto1= Frame(Botto, width=650, height=100, border=0,relief="flat")
inBotto1.pack(side=TOP)




Buttons=Frame(inBotto1, width = 1350, height=100, bd=1, relief="flat")
Buttons.pack(side=BOTTOM)

AnsBotto2=Frame(inBotto1, width=1350, height=200, bd=1, relief="flat")
AnsBotto2.pack(side=TOP)

'''FUNCION PREDICTORA'''
def Sum():
	

		curva = int(firstnum.get())
		progresion = int(secondnum.get())
		edad = int(thirdnum.get())
		espaldas = int(fourthnum.get())
		espaldai = int (fifthnum.get())
		

		xd= clf.predict([[curva,progresion,edad,espaldas,espaldai]])
		if xd==1:
			mensaje="Requiere de observacion."
		elif xd==2:
			mensaje="Seguir un tratamiento."
		else:
			mensaje="Cirugia lo mas antes posible."
		Total.set(mensaje)
	

def Reset():
	firstnum.set("")
	secondnum.set("")
	thirdnum.set("")
	fourthnum.set("")
	fifthnum.set("")
	Total.set("")

var= IntVar()
firstnum = IntVar()
secondnum = IntVar()
thirdnum = IntVar()
fourthnum = IntVar()
fifthnum = IntVar()
Total =IntVar()


firstnum.set("")
secondnum.set("")
thirdnum.set("")
fourthnum.set("")
fifthnum.set("")
Total.set("")




'''INTERFAZ DE INPUTS'''
lblfirst= Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Ingrese la curvatura (en grados)", fg="black", bd=16).grid(row=0,column=0, sticky=W)
txtfirst= Entry(AnsBotto2, font=('Helvetica',13,'bold'),bd=4, width=34, bg="white", textvariable=firstnum).grid(row=0,column=1)

lblsecond= Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Ingrese la progresion (en grados)", fg="black", bd=16).grid(row=1,column=0, sticky=W)
txtsecond= Entry(AnsBotto2, font=('Helvetica',13,'bold'),bd=4, width=34, bg="white", textvariable=secondnum).grid(row=1,column=1)

lblthird= Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Ingrese la edad del paciente", fg="black", bd=16).grid(row=2,column=0, sticky=W)
txtthird= Entry(AnsBotto2, font=('Helvetica',13,'bold'),bd=4, width=34, bg="white", textvariable=thirdnum).grid(row=2,column=1)


lblfourth= Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Ingrese medida de la espalda superior", fg="black", bd=16).grid(row=4,column=0, sticky=W)
txtfifth= Entry(AnsBotto2, font=('Helvetica',13,'bold'),bd=4, width=34, bg="white", textvariable=fourthnum).grid(row=4,column=1)


lblfifth= Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Ingrese medida de la espalda inferior", fg="black", bd=16).grid(row=6,column=0, sticky=W)
txtsixth= Entry(AnsBotto2, font=('Helvetica',13,'bold'),bd=4, width=34, bg="white", textvariable=fifthnum).grid(row=6,column=1)

lblTotal = Label(AnsBotto2, font=('Helvetica',13,'bold'),text="Consejo: ",fg="black", bd=16, justify="left")
lblTotal.grid(row=7, column=0, sticky=W)

LAnswer = Label(AnsBotto2, font=('Helvetica', 13, 'bold'), bd=4, width=30, bg= "white", textvariable=Total, relief='sunken').grid(row=8, column=0, columnspan=4, sticky=W+E+N+S, rowspan=4)

SumUP=Button(Buttons, pady=8, bd=8, fg="black", font=('Helvetica', 16, 'bold'), command=Sum,width=12, text="Diagnosticar", bg="white").grid(row=0, column=0)
Reset=Button(Buttons, pady=8, bd=8, fg="black", font=('Helvetica', 16, 'bold'), command = Reset, width=12, text="Borrar", bg="white").grid(row=0, column=1)
Exit=Button(Buttons, pady=8, bd=8, fg="black", font=('Helvetica', 16, 'bold'), width=12, text="Salir", bg="white").grid(row=0, column=2)





root.mainloop()
