import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt



def modelo_arbol_decision():
    pacientes =  pd.read_csv('https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Pacientes2.csv', engine = 'python' , index_col = 0)
    #Variables Predictoras
    global X
    X = pacientes.iloc[:,1:11]
    #Variables a predecir
    global Y
    Y = pacientes.iloc[:,0]
    #X_train y Y_train para entrenamiento
    #Y_test y Y_test para prueba
    global X_test
    global Y_test
    X_train, X_test, Y_train , Y_test = train_test_split(X,Y,train_size=0.75,random_state = 0)
    global arbol
    arbol = DecisionTreeClassifier(max_depth = 5)
    # Entrenamos el modelo
    global arbol_enfermedad
    arbol_enfermedad = arbol.fit(X_train,Y_train)

def mostrar_arbol_decision():
    #Le indicamos las dimensiones del grafico
    fig = plt.figure(figsize= (20,25))
    #Indicamos donde se encuentra la informacion a graficar,lo que tuvimos del 
    #entrenamiento, obtenemos los valores de las columnas del objeto x y nombres de 
    #las clases de predecir que lo tenemos en la lista de y
    tree.plot_tree(arbol_enfermedad, feature_names = list(X.columns.values),
                class_names = list(Y.values) , filled = True)
    plt.show()

def efectividad_arbol_decision():
    Y_pred = arbol_enfermedad.predict(X_test)
    return arbol.score(X_test,Y_test)

def predecir_valor(list):
    #Cargamos datos y entrenamos el arbol
    modelo_arbol_decision()
    columns = ["HIPERTEN", "HIPERGLU", "HDLBAJA", "HIPERTRI", "CINTALTA", "EDAD", "GENERO", "FUMA", "ALCOHOL",
          "POLIURIA"]
    #listNumpy = np.array(list)
    b = pd.DataFrame([list],columns = columns, index = ["924"])  
    return arbol.predict_proba(b)


def sufre_enfermedad(numpyArray):
    if numpyArray[0][0] > numpyArray[0][1]:
        return "No, lo sufre"
    else:
        return "Si, lo sufre"


def grafica_circular(list):
    plt.figure(figsize=[10,8])
    columns = ["No, puede sufrir", "Si, puede Sufrir"]
    print("***************",list)
    listResult = [list[0][0],list[0][1]]
    plt.style.use("ggplot")
    plt.title("Porcentaje del paciente de tener una enfermedad cardiovascular")
    plt.pie(x = listResult,labels = columns, autopct = "%.2f%%", shadow=True)
    plt.axis = ("equal")
    plt.legend(loc = "upper left")
    plt.show()