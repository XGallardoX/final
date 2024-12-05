from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
import math
import matplotlib.pyplot as plt
import numpy as np
import random
 

# Definir la clase MLP (Perceptrón Multicapa)
class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        # Inicialización de los pesos y sesgos de las capas
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Pesos y sesgos para las conexiones entre las capas
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
        self.bias_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # Propagación hacia adelante
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)

        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = self.sigmoid(self.output_input)

        return self.output

    def backward(self, X, y):
        # Cálculo del error de salida
        error_output = y - self.output
        d_output = error_output * self.sigmoid_derivative(self.output)

        # Error en la capa oculta
        error_hidden = d_output.dot(self.weights_hidden_output.T)
        d_hidden = error_hidden * self.sigmoid_derivative(self.hidden_output)

        # Actualización de pesos y sesgos
        self.weights_hidden_output += self.hidden_output.T.dot(d_output) * self.learning_rate
        self.bias_output += np.sum(d_output, axis=0, keepdims=True) * self.learning_rate

        self.weights_input_hidden += X.T.dot(d_hidden) * self.learning_rate
        self.bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, y)

    def predict(self, X):
        return np.round(self.forward(X))



class MiVisitor(gramaticaVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitAsignacion(self, ctx: gramaticaParser.AsignacionContext):
        var_name = ctx.getChild(0).getText()
        if(ctx.expresion()):
            value = self.visit(ctx.expresion())
            self.variables[var_name] = value
        elif(ctx.matriz_operaciones()):
            value = self.visit(ctx.matriz_operaciones())
            self.variables[var_name] = value
        elif(ctx.arange()):
            value = self.visit(ctx.arange())
            self.variables[var_name] = value

    def visitV_input(self, ctx: gramaticaParser.V_inputContext):
        var_name = ctx.ID().getText()
        value = input()
        self.variables[var_name] = value

    def visitPrintf(self, ctx: gramaticaParser.PrintfContext): 
        value = self.visit(ctx.expresion())
        print(value)
        return value

    def visitFuncion(self, ctx: gramaticaParser.FuncionContext):
        # Implementa la lógica para definir y llamar funciones aquí
        pass

    def visitLlamafuncion(self, ctx: gramaticaParser.LlamafuncionContext):
        function_name = ctx.ID().getText()
        arguments = ctx.parametro().getText() if ctx.parametro() else ""
        # Implementa la lógica para llamar a funciones aquí
        pass

    def visitCondicional(self, ctx: gramaticaParser.CondicionalContext):
        condition = self.visit(ctx.expresion())
        condition_met = False

        if condition:
            self.visit(ctx.sentencias())
            condition_met = True

        if not condition_met and ctx.elifBlock():
            for elif_ctx in ctx.elifBlock().condicional_elif():
                elif_condition = self.visit(elif_ctx.expresion())
                if elif_condition and not condition_met:
                    self.visit(elif_ctx.sentencias())
                    condition_met = True

        if not condition_met and ctx.condicional_else():
            self.visit(ctx.condicional_else())

    def visitCondicional_else(self, ctx: gramaticaParser.Condicional_elseContext):
        self.visit(ctx.sentencias())

    def visitCiclo_for(self, ctx: gramaticaParser.Ciclo_forContext):
        variable = ctx.getChild(1).getText()  # Obtener el nombre de la variable

        ve = ctx.expresion(0).getText()
        if(ve[0]=="[" or ve[0]=="("):
            if(ve[0]=="["):
                ve = ve[1:-1]
                arr = ve.split(",")
                for i in range(len(arr)):
                    if(arr[i][0]=='"'):
                        arr[i] = arr[i][1:-1]
                        
                for value in arr:
                    self.variables[variable] = value  # Asignar el valor de la variable en cada iteración
                    self.visit(ctx.sentencias())  # Visitar las sentencias dentro del ciclo "for"

        elif len(ctx.expresion()) == 1:
            var = (ctx.expresion(0).getText()) 
            if(var.isalpha()):
                v = int(self.variables[var])
                for value in range(v):
                    self.variables[variable] = value  # Asignar el valor de la variable en cada iteración
                    self.visit(ctx.sentencias())  # Visitar las sentencias dentro del ciclo "for"
            else:
                for value in range(int(var)):
                    self.variables[variable] = value  # Asignar el valor de la variable en cada iteración
                    self.visit(ctx.sentencias())  # Visitar las sentencias dentro del ciclo "for"
        else:
            start = ctx.expresion(0).getText() # Obtener el valor inicial
            if(start.isalpha()):
                start = int(self.variables[start])
            end = ctx.expresion(1).getText()  # Obtener el valor final
            if(end.isalpha()):
                end= int(self.variables[end])
            # Verificar si se proporcionó un incremento
            if len(ctx.expresion()) > 2:
                step = ctx.expresion(2).getText()  # Obtener el incremento
                if(step.isalpha()):
                    step= int(self.variables[step])
            else:
                step = 1  # Valor predeterminado del incremento
            # Iterar desde el valor inicial hasta el valor final (exclusivo) con el incremento especificado
            for value in range(int(start), int(end), int(step)):

                self.variables[variable] = value  # Asignar el valor de la variable en cada iteración
                self.visit(ctx.sentencias())  # Visitar las sentencias dentro del ciclo "for"

    def visitCiclo_while(self, ctx: gramaticaParser.Ciclo_whileContext):
        while self.visit(ctx.expresion()):
            for sentencia in ctx.sentencias():
                self.visit(sentencia)
            condition = self.visit(ctx.expresion())
 
    
    def visitMatriz_operaciones(self, ctx:gramaticaParser.Matriz_operacionesContext):
        if (ctx.getChild(2)==None):
            result = self.visit(ctx.matriz(0))
        else:
            if(ctx.getChild(0).getText()=="trans" or ctx.getChild(0).getText()=="inv"):
                matrix1 = self.visit(ctx.matriz(0))
                matrix1 = np.array(matrix1)
                if ctx.getChild(0).getText()== 'trans':
                    result = np.transpose(matrix1)
                elif ctx.getChild(0).getText()== 'inv':
                    result = np.linalg.inv(matrix1)
            else:
                matrix1 = self.visit(ctx.matriz(0))
                matrix2 = self.visit(ctx.matriz(1))
                matrix1 = np.array(matrix1)
                matrix2 = np.array(matrix2)
                operator = ctx.getChild(1).getText()
                
                if operator == '+':
                    result = np.add(matrix1, matrix2)
                elif operator == '-':
                    result = np.subtract(matrix1, matrix2)
                elif operator == '*':
                    result = np.multiply(matrix1, matrix2)
        return result

    def visitMatriz(self, ctx: gramaticaParser.MatrizContext):
        rows = len(ctx.fila_matriz())
        cols = len(ctx.fila_matriz(0).expresion())

        matrix = np.zeros((rows, cols))
        
        for i, fila in enumerate(ctx.fila_matriz()):
            for j, exp in enumerate(fila.expresion()):
                matrix[i][j] = self.visit(exp)
        return matrix

    def visitExpresion(self, ctx: gramaticaParser.ExpresionContext):
        if ctx.SUMA() or ctx.RESTA() or ctx.MULTIPLICACION() or ctx.DIVISION() or ctx.POTENCIA() or ctx.MODULO():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            op = ctx.getChild(1).getText()
            if op == '+':
                a=left + right
            elif op == '-':
                a= left - right
            elif op == '*':
                a= left * right   
            elif op == '/':
                a = left / right
            elif op == '^':
                a = left ** right
            elif op == '%':
                a = left % right
            #print(a)
            return a
        elif ctx.MAYORQUE() or ctx.MENORQUE() or ctx.MENORIGUAL() or ctx.MAYORIGUAL() or ctx.DIFERENTE() or ctx.IGUAL():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            op = ctx.getChild(1).getText()
            if op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
            elif op == '!=':
                return left != right
            elif op == '==':
                return left == right
        elif ctx.ASIGNACION():
            var_name = ctx.ID().getText()
            value = self.visit(ctx.termino())
            self.variables[var_name] = self.variables.get(value)
            return self.variables.get(var_name)
        elif ctx.OR():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            return left or right
        elif ctx.AND():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            return left and right
        elif ctx.func():
            return self.visit(ctx.func())
        else:
            return self.visit(ctx.termino())


    def visitTermino(self, ctx: gramaticaParser.TerminoContext):
        if ctx.ID():
            var_name = ctx.getChild(0).getText()
            return self.variables.get(var_name)
        elif ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.BOOLEAN():
            bool_value = ctx.BOOLEAN().getText()
            return bool_value == 'True'
        elif ctx.cadena():
            return self.visit(ctx.cadena())
        elif ctx.lista():
            return self.visit(ctx.lista())
        elif ctx.arreglo():
            return self.visit(ctx.arreglo())

    def visitCadena(self, ctx: gramaticaParser.CadenaContext):
        return ctx.getText()[1:-1]
    
    def visitLista(self, ctx: gramaticaParser.ListaContext):
        text = ctx.getText()[1:-1]  # Obtener el texto sin los corchetes
        elements = text.split(',')  # Dividir el texto en función del separador (coma en este caso)
        return [element.strip() for element in elements]  # Crear una lista resultante, eliminando los espacios en blanco alrededor de cada elemento

    def visitArreglo(self, ctx: gramaticaParser.ArregloContext):
        text = ctx.getText()[1:-1]  # Obtener el texto sin los corchetes
        elements = text.split(',')
        elements = [float(x) for x in elements]  # Convertir cada elemento a entero
        return elements
        #elements = text.split(',')  # Dividir el texto en función del separador (coma en este caso)
        #return [element.strip() for element in elements]  # Crear un arreglo resultante, eliminando los espacios en blanco alrededor de cada elemento y convirtiendo los elementos a float
    
    def visitArreglodeArreglos(self, ctx: gramaticaParser.ArregloContext):
        # Extraer los valores del arreglo y convertirlos en una lista de listas de números
        arreglo = []
        for sublist in ctx.arreglo():  # Para cada sublista en el arreglo
            sublist_values = []
            for num in sublist.NUMERO():  # Cada número dentro de la sublista
                sublist_values.append(int(num.getText()))  # Convertir el número a entero y añadirlo
            arreglo.append(sublist_values)  # Añadir la sublista al arreglo
        
        return arreglo

        
        


    def visitGraficas(self, ctx: gramaticaParser.GraficasContext):
        if(ctx.getChild(0).getText()=="scatter"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.scatter(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="plot"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.plot(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="fill_between"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.fill_between(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="barh"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.barh(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="bar"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.bar(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="hist"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.hist(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="boxplot"):
            x = self.visit(ctx.getChild(2))
            fig, ax = plt.subplots()
            ax.boxplot(x)
            plt.show()
        elif(ctx.getChild(0).getText()=="pie"):
            x = self.visit(ctx.getChild(2))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.pie(x)
            plt.show()
        elif(ctx.getChild(0).getText()=="grafsen" or ctx.getChild(0).getText()=="grafcos" or ctx.getChild(0).getText()=="graftan"):
            if(ctx.ID()):
                var_name = ctx.getChild(2).getText()
                print(var_name)
                x = self.variables.get(var_name)
            else:
                print(self.visit(ctx.arange()))
                x = self.visit(ctx.arange())
            y = self.visit(ctx.func())
            fig, ax = plt.subplots()
            ax.set_title(ctx.func().getText()[3:])
            ax.plot(x, y)
            plt.show()

    def visitArange(self, ctx: gramaticaParser.ArangeContext): 
        #print(ctx.expresion(0).getText())
        x = int(ctx.expresion(0).getText())
        y = int(ctx.expresion(1).getText())*np.pi
        #print(ctx.expresion(1).getText())
        z = int(ctx.expresion(2).getText())
        #print(ctx.expresion(2).getText())
        arr = np.linspace(x,y,z)
        return arr

    def visitFunc(self, ctx: gramaticaParser.FuncContext):
        print('entro')
        value = self.visit(ctx.expresion())
        print(self.visit(ctx.expresion()))
        function_name = ctx.getChild(2).getText()
        #Para radianes math
        if(ctx.getChild(0).getText()=="math"):

            if isinstance(self.visit(ctx.expresion()), str):
                value = math.radians(int(value))
            else:
                value = math.radians(value)
            if function_name=="sin":
                a = math.sin(value)
            elif function_name=="cos":
                a = math.cos(value)
            elif function_name== "tan":
                a = math.tan(value)
            elif function_name=="arcsin":
                a = math.asin(value)
            elif function_name=="arccos":
                a = math.acos(value)
            elif function_name== "arctan":
                a = math.atan(value)
            #print(a)
            return a 
        #Sin radianes
        elif(ctx.getChild(0).getText()=="np"):

            if isinstance(self.visit(ctx.expresion()), str):
                value = int(value)

            if function_name=="sin":
                a = np.sin(value)
            elif function_name=="cos":
                 a = np.cos(value)
            elif function_name== "tan":
                 a = np.tan(value)
            elif function_name=="arcsin":
                a = np.arcsin(value)
            elif function_name=="arccos":
                a = np.arccos(value)
            elif function_name== "arctan":
                a = np.arctan(value)
            return a       

    def visitRegresion_lineal(self, ctx: gramaticaParser.Regresion_linealContext):
        # Obtenemos las dos expresiones (x e y) que son las coordenadas
        x = self.visit(ctx.expresion(0))  # Los valores de x
        y = self.visit(ctx.expresion(1))  # Los valores de y
        
        # Convertimos x e y a arrays de numpy para procesar la regresión
        x = np.array(x)
        y = np.array(y)
        
        # Usamos numpy para hacer la regresión lineal
        slope, intercept = np.polyfit(x, y, 1)  # El "1" indica una recta (polinomio de grado 1)
        
        print(f"Pendiente (slope): {slope}")
        print(f"Intersección (intercept): {intercept}")
        
        
        # Graficamos los puntos de datos originales
        plt.scatter(x, y, color='blue', label='Puntos de datos')  # Puntos de datos
        
        # Graficamos la línea de regresión
        plt.plot(x, slope * x + intercept, color='red', label='Línea de regresión')  # Línea de regresión
        
        # Agregamos etiquetas y leyenda
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Regresión Lineal')
        plt.legend()
        
        # Mostramos la gráfica
        plt.show()
        
        # Retornamos la pendiente y la intersección de la recta
        return slope, intercept

    # Función K-means sin sklearn
    def kmeans(self,x, y, k):
        # Número de puntos
        n = len(x)
        
        # Inicializamos los centroides de manera aleatoria
        centroids = random.sample(list(zip(x, y)), k)  # Centroides iniciales
        
        # Iterar hasta que los centroides no cambien (o un número fijo de iteraciones)
        max_iterations = 100
        for _ in range(max_iterations):
            # Crear una lista de clusters vacíos
            clusters = [[] for _ in range(k)]
            
            # Asignar cada punto al cluster más cercano
            for i in range(n):
                distances = [((x[i] - cx)**2 + (y[i] - cy)**2)**0.5 for cx, cy in centroids]
                closest_centroid = distances.index(min(distances))
                clusters[closest_centroid].append((x[i], y[i]))
            
            # Recalcular los centroides
            new_centroids = []
            for cluster in clusters:
                if len(cluster) > 0:
                    avg_x = sum([point[0] for point in cluster]) / len(cluster)
                    avg_y = sum([point[1] for point in cluster]) / len(cluster)
                    new_centroids.append((avg_x, avg_y))
                else:
                    new_centroids.append(random.choice(list(zip(x, y))))  # Si no hay puntos, volver a elegir aleatoriamente

            # Si los centroides no cambian, terminamos
            if new_centroids == centroids:
                break
            
            centroids = new_centroids
        
        # Imprimir los resultados
        print(f"Centroides finales: {centroids}")
        for i, cluster in enumerate(clusters):
            print(f"Cluster {i + 1}: {cluster}")
        
        # Graficar los clusters y los centroides
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']  # Máximo 8 colores
        plt.figure(figsize=(8, 6))
        
        for i, cluster in enumerate(clusters):
            cluster_points = list(zip(*cluster))  # Transponer para obtener x e y
            if cluster_points:  # Verifica que el cluster no esté vacío
                plt.scatter(cluster_points[0], cluster_points[1], color=colors[i % len(colors)], label=f'Cluster {i+1}')
        
        # Dibujar centroides
        centroid_points = list(zip(*centroids))  # Transponer para obtener x e y
        plt.scatter(centroid_points[0], centroid_points[1], color='black', marker='x', s=100, label='Centroides')
        
        # Configurar la gráfica
        plt.title('Resultados del K-means')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()

    def visitK_means(self, ctx: gramaticaParser.K_meansContext):
        # Extraer las dos listas y el número de clusters
        x = self.visit(ctx.arreglo(0))  # Primera lista
        y = self.visit(ctx.arreglo(1))  # Segunda lista
        k = int(ctx.NUMERO().getText())  # Número de clusters

        # Verificar que las entradas sean válidas
        if not isinstance(x, list) or not isinstance(y, list):
            raise ValueError("Los parámetros X e Y deben ser listas.")
        if not isinstance(k, int) or k <= 0:
            raise ValueError("El número de clusters K debe ser un entero positivo.")

        # Llamar al algoritmo K-means
        self.kmeans(x, y, k)

    
    
    # Función para calcular la distancia euclidiana entre dos puntos
    def euclidean_distance(self,point1, point2):
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5
        

    # Función para graficar los resultados de K-means
    def plot_kmeans(data, centers, clusters):
        for i, cluster in enumerate(clusters):
            x, y = zip(*cluster)
            plt.scatter(x, y, label=f'Cluster {i + 1}')
        
        cx, cy = zip(*centers)
        plt.scatter(cx, cy, c='red', marker='X', s=200, label='Centros')
        plt.title("K-means Clustering")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()
    
    
    # DBSCAN
    def dbscan(self,data, eps, min_pts):
        labels = [-1] * len(data)  # -1 significa ruido por defecto
        cluster_id = 0

        def region_query(point):
            """Encuentra los puntos vecinos de un punto dado"""
            neighbors = []
            for i, other_point in enumerate(data):
                if self.euclidean_distance(point, other_point) <= eps:
                    neighbors.append(i)
            return neighbors

        def expand_cluster(point_idx, neighbors):
            """Expande un cluster a partir de un punto dado"""
            nonlocal cluster_id
            labels[point_idx] = cluster_id
            i = 0
            while i < len(neighbors):
                neighbor_idx = neighbors[i]
                if labels[neighbor_idx] == -1:  # Convertir ruido en cluster
                    labels[neighbor_idx] = cluster_id
                elif labels[neighbor_idx] == 0:  # Expandir cluster
                    labels[neighbor_idx] = cluster_id
                    new_neighbors = region_query(data[neighbor_idx])
                    if len(new_neighbors) >= min_pts:
                        neighbors += new_neighbors
                i += 1

        for point_idx, point in enumerate(data):
            if labels[point_idx] != -1:  # Ya visitado
                continue
            neighbors = region_query(point)
            if len(neighbors) < min_pts:
                labels[point_idx] = -1  # Ruido
            else:
                cluster_id += 1
                expand_cluster(point_idx, neighbors)
        print
        #labels = self.dbscan(data, eps, min_pts)

        # Imprime los resultados
        print("Etiquetas de los puntos (labels):")
        print(data)

        return labels
    
    # Función para visualizar los resultados
    def plot_clusters(self,data, labels):
        clusters = {}
        for idx, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(data[idx])

        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
        plt.figure(figsize=(10, 7))
        for cluster_id, points in clusters.items():
            x = [p[0] for p in points]
            y = [p[1] for p in points]
            plt.scatter(x, y, label=f"Cluster {cluster_id}" if cluster_id != -1 else "Noise",
                        color=colors[cluster_id % len(colors)] if cluster_id != -1 else "black")
        plt.legend()
        plt.show()
        
    
    def visitDbscan(self, ctx):
        x = self.visit(ctx.arreglo(0))  # Lista X
        y = self.visit(ctx.arreglo(1))  # Lista Y
        eps = float(ctx.NUMERO(0).getText())  # Epsilon
        min_pts = int(ctx.NUMERO(1).getText())  # MinPts
        
        #int(self.visit(ctx.expresion(3)))

        # Combinar x e y en un solo conjunto de datos
        data = list(zip(x, y))
        labels = self.dbscan(data, eps, min_pts)
        self.plot_clusters(data, labels)  # Visualizar los resultados

    def visitMlp(self, ctx: gramaticaParser.MlpContext):
        # Obtener los parámetros del MLP desde la entrada
        input_size = int(ctx.NUMERO(0).getText())  # Tamaño de la entrada
        hidden_size = int(ctx.NUMERO(1).getText())  # Tamaño de la capa oculta
        output_size = int(ctx.NUMERO(2).getText())  # Tamaño de la salida
        epochs = int(ctx.NUMERO(3).getText())  # Número de épocas de entrenamiento

        # Obtener los arreglos de entradas (X) y salidas (y)
        X2 = self.visit(ctx.arreglo(0))  # El primer arreglo corresponde a X
        X = [[int (X2[i]), int(X2[i+1])] for i in range(0, len(X2), 2)]
        X = np.array(X)
        y2 = self.visit(ctx.arreglo(1))  # El segundo arreglo corresponde a y
        y = np.array([[int (y2[i])]for i in range(0, len(y2))])
        y = np.array(y)
        
        print(f"Configurando MLP: Entrada={input_size}, Capa Oculta={hidden_size}, Salida={output_size}, Épocas={epochs}")
        
        # Crear el modelo MLP con estos parámetros
        mlp = MLP(input_size, hidden_size, output_size)

        # Entrenar el MLP
        mlp.train(X, y, epochs=epochs)

        # Realizar predicciones sobre los mismos datos
        predicciones = mlp.predict(X)

        # Mostrar resultados
        print("Predicciones del MLP:")
        for point, prediction in zip(X, predicciones):
            print(f"Punto: {point}, Predicción: {prediction[0]}")
        
        return mlp


        

def main():
    lexer = gramaticaLexer(InputStream(input()))
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.start()

    visitor = MiVisitor()
    visitor.visit(tree)
    
     # Aquí solo doy un ejemplo de cómo podrían ser los datos:
    #X = np.array([[1, 2], [2, 3], [100, 100], [101, 101], [50, 50]])  # Datos de ejemplo
    #y = np.array([[0], [0], [1], [1], [0]])  # Etiquetas generadas por DBSCAN (0: ruido, 1: clusters)
    
   # print("sapo")
    #print(X,y)

    #Configuración del MLP (Perceptrón Multicapa)
    #input_size = 2  # Tamaño de entrada (dimensión de cada punto)
    #hidden_size = 5  # Número de neuronas en la capa oculta
    #output_size = 1  # Salida binaria (puedes ajustarlo según el número de clases)

    #Inicializar y entrenar el MLP
    #mlp = MLP(input_size, hidden_size, output_size, learning_rate=0.01)
    #mlp.train(X, y, epochs=10000)

    #Predicciones sobre los mismos datos
    #predicciones = mlp.predict(X)

    #Imprimir las predicciones
    #print("Predicciones del clasificador MLP:")
    #for point, prediction in zip(X, predicciones):
     #   print(f"Punto: {point}, Predicción: {prediction[0]}")



if __name__ == '__main__':
    main()
