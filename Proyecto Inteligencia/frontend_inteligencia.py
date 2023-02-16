from tkinter import *
from tkinter import ttk
from modelo import *

root = Tk()
root.title("Formulario Cardiovascular")
root.resizable(False,False)
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 550
hventana = 700

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

opcionGenero = IntVar()
comboHiperglu = StringVar()
comboHiperten = StringVar()
combo_hdl_bajo = StringVar()
combo_hipertri = StringVar()
combo_cintalta = StringVar()
spinbox_edad = StringVar()
combo_fuma = StringVar()
combo_toma = StringVar()
combo_poliuria = StringVar()
respuesta_string = StringVar()


def obtenerValores():
    valoresPredecir = [int(spinbox_edad.get()),opcionGenero.get()
    ,comboHiperglu.get(),comboHiperten.get(),combo_hdl_bajo.get(),
    combo_hipertri.get(),combo_cintalta.get(),combo_fuma.get(),
    combo_toma.get(),combo_poliuria.get()]
    global valorPredecido
    valorPredecido = predecir_valor(convertirValoresNumericos(valoresPredecir))
    print("-----------",valorPredecido)
    respuesta_string.set(sufre_enfermedad(valorPredecido))
    botonGraficoCircular.config(state="normal")
    botonGraficaX.config(state="normal")
    """
    print("edad",spinbox_edad.get())
    print("Genero: ", opcionGenero.get())
    print("HiperGlucemia: ", comboHiperglu.get())
    print("Hipertension: ", comboHiperten.get())
    print("Colesterol bajo: ", combo_hdl_bajo.get())
    print("Hipertrigliceridemia: ", combo_hipertri.get())
    print("cintalta: ", combo_cintalta.get())
    print("Fuma: " , combo_fuma.get())
    print("toma: " , combo_toma.get())
    print("poliuria: " , combo_poliuria.get())
    print("----------------------------------------------------")
    print(convertirValoresNumericos(valoresPredecir)) 
    """ 
   
def convertirValoresNumericos(list):
    listResult = []
    for i in range(0,len(list)):
        if i < 2:
            listResult.append(list[i])
        else: 
            if list[i] == "Si":
                listResult.append(1)
            else:
                listResult.append(0)
    return listResult

        
def generarDiagramaCircular():
    grafica_circular(valorPredecido)

def generarArbolDecision():
        mostrar_arbol_decision()

def generarGraficaX():
    pass



def inicializarValores():
    #Entrenamos el modelo 
    modelo_arbol_decision()
    #Inicializar el titulo
    tituloFrame = Frame(root)
    tituloFrame.grid(row = 0, column=0,columnspan= 3)
    labelFrame = Label(tituloFrame,text= "Formulario de prediccion de enfermedades cardiovasculares"
    ,font = ('Segoe UI Black', 13))
    labelFrame.config(pady=20)
    labelFrame.grid(row = 0, column=0,sticky="N")
    #Inicializar valores del formulario
    formFrame = Frame(root)
    formFrame.grid(row = 1, column=0)
    #Edad
    edad_label = Label(formFrame, text= "Edad:")
    edad_label.grid(row = 0, column=0, sticky="W")
    edad_spindBox = Spinbox(formFrame,from_= 1, to = 110,wrap=True,textvariable=spinbox_edad)
    edad_spindBox.grid(row = 0, column=1)  
    #Genero
    labelGenero = Label(formFrame, text = "Genero: ")
    labelGenero.grid(row=1,column=0,sticky="w")
    #Frame de de los radioButton
    radioFrame = Frame(formFrame)
    radioFrame.grid(row = 1, column= 1,sticky="w")
    masculino = Radiobutton(radioFrame, text = "Masculino",value = 1,variable=opcionGenero)
    masculino.grid(row=0,column=0)
    femenino = Radiobutton(radioFrame, text = "Femenino",value = 0,variable=opcionGenero)
    femenino.grid(row=1,column=0)
    
    #Hiperglucemia
    hiperglucemiaLabel = Label(formFrame, text= "¿Sufre de Hiperglucemia?")
    values =["Si","No"]
    hiperglucemiaLabel.grid(row = 2, column=0, sticky="W")
    hiperglucemiaCombo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=comboHiperglu)
    hiperglucemiaCombo.current(0)
    hiperglucemiaCombo.grid(row = 2, column=1,pady= 20,padx = 10)
    #Hipertencion
    hipertension_label = Label(formFrame, text= "¿Sufre de Hipertension?")
    hipertension_label.grid(row = 3, column=0, sticky="W")
    hipertension_Combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=comboHiperten)
    hipertension_Combo.current(0)
    hipertension_Combo.grid(row = 3, column=1,pady= 20,padx = 10)
    #HDL BAJO
    hdl_label = Label(formFrame, text= "¿Sufre de colesterol bajo?")
    hdl_label.grid(row = 4, column=0, sticky="W")
    hdl_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_hdl_bajo)
    hdl_combo.current(0)
    hdl_combo.grid(row = 4, column=1,pady= 20,padx = 10)
    #Hipertrigliceridemia
    hipertri_label = Label(formFrame, text= "¿Tiene triglicéridos en la sangre superior a 150 mg/dl?")
    hipertri_label.grid(row = 5, column=0, sticky="W")
    hipertri_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_hipertri)
    hipertri_combo.current(0)
    hipertri_combo.grid(row = 5, column=1,pady= 20,padx = 10)
    #Familiares con enfermades cardiovasculares
    cintalta_label = Label(formFrame, text= "¿Tiene familiares con enfermedades cardiovasculares o con antecentes?")
    cintalta_label.grid(row = 6, column=0, sticky="W")
    cintalta_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_cintalta)
    cintalta_combo.current(0)
    cintalta_combo.grid(row = 6, column=1,pady= 20,padx = 10)
    #Fuma
    fuma_label = Label(formFrame, text= "¿El paciente fuma?")
    fuma_label.grid(row = 7, column=0, sticky="W")
    fuma_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_fuma)
    fuma_combo.current(0)
    fuma_combo.grid(row = 7, column=1,pady= 20,padx = 10)
    #Toma
    toma_label = Label(formFrame, text= "¿El paciente consume una gran cantidad de alcohol?")
    toma_label.grid(row = 8, column=0, sticky="W")
    toma_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_toma)
    toma_combo.current(0)
    toma_combo.grid(row = 8, column=1,pady= 20,padx = 10)
    #Toma
    toma_label = Label(formFrame, text= "¿El paciente tiene poliuria?")
    toma_label.grid(row = 9, column=0, sticky="W")
    toma_combo = ttk.Combobox(formFrame, state="readonly",
    values = values,textvariable=combo_poliuria)
    toma_combo.current(0)
    toma_combo.grid(row = 9, column=1,pady= 20,padx = 10)
    #¿Sufriria la enfermedad?
    enfermedad = Label(formFrame, text= "¿El paciente puede sufrir la enfermedad?")
    enfermedad.grid(row=10, column=0, sticky="W")
    global respuesta
    respuesta = Label(formFrame, textvariable= respuesta_string)
    respuesta.grid(row=10, column=1, sticky="W")

    #Inicializar botones 
    buttonFrame = Frame(root)
    buttonFrame.grid(row = 3, column=0,pady= 20)
    botonPredecir = Button(buttonFrame,text = "Predecir",command=obtenerValores,width=10)
    botonPredecir.grid(row=0,column=0,padx=5)

    global botonGraficoCircular
    botonGraficoCircular = Button(buttonFrame,text = "Grafico circular",command=generarDiagramaCircular,width=15)
    botonGraficoCircular.config(state="disabled")
    botonGraficoCircular.grid(row=0,column=1,padx=5)
    botonArbolDecision = Button(buttonFrame,text = "Arbol de desicion",command=generarArbolDecision,width=15)
    botonArbolDecision.grid(row=0,column=2,padx=5)
    global botonGraficaX
    botonGraficaX = Button(buttonFrame,text= "Grafica x",command=generarGraficaX,width=15)
    botonGraficaX.config(state="disabled")
    botonGraficaX.grid(row = 0, column=3,padx=5)

inicializarValores()
root.mainloop()