import graphviz
import State
import matplotlib.pyplot as plt
import networkx as nx
import pydot


#Clase Automata para el algoritmo de thompson

#Automata tiene un estado inicial y uno final, estado de aceptación
#start - Estado inicial
#final - Estado final
class Automata():
    def __init__(self, start: State, final:State) -> None:
        self.start = start
        self.final = final
        self.transitions = self.Transiciones()
        self.edges = []
        self.trans_symbols  = {}
        
    #prints transitions
    def show(self):
        stack = [self.start]
        visited = []
        while len(stack) != 0:
            afn = stack.pop()
            transiciones = afn.transitions.items()

            for key, value in transiciones:
                if afn not in visited:
                    stack.append(key)
                    print(afn.name, "-->",value,"-->", key.name)
            visited.append(afn)
    #pone todas las transiciones en un diccionario
    def Transiciones(self):
        stack = [self.start]
        visited = []
        trans = {}
        while len(stack) != 0:
            afn = stack.pop()
            transiciones = afn.transitions.items()

            for key, value in transiciones:
                if afn not in visited:
                    stack.append(key)
                    if afn.name in trans.keys():
                        trans[afn.name] = {value: [key.name, anterior]}
                        
                    #Transiiciones
                    #Trans = transiciones
                    #trans[afn.name] = {nombre del estado actual: {simobolo: estado al que va}}
                    
                    else:
                        trans[afn.name] = {value: key.name}
                anterior = key.name
                    
            visited.append(afn)
                
        return trans
    def getTransition(self):
        self.edges = []
        self.trans_symbols = {}
            
        for i in self.transitions:
            for j in self.transitions[i]:
                if self.transitions[i][j][0]=="s":
                    self.edges.append((i, self.transitions[i][j]))
                    self.trans_symbols[(i,self.transitions[i][j])] = j
                else:
                    for k in self.transitions[i][j]:
                        self.edges.append((i,k))
                        self.trans_symbols[(i,k)] = j
        
    def Export(self, output_file):
            self.getTransition()
            G = graphviz.Digraph(format='png', graph_attr={'rankdir':'LR'})

            # Agregar nodos al grafo
            G.node(self.start.name, style='filled', fillcolor='aqua')
            G.node(self.final.name, style='filled', fillcolor='skyblue')
            for i in self.transitions:
                G.node(i)

            # Agregar arcos al grafo
            for edge in self.edges:
                G.edge(edge[0], edge[1], label=self.trans_symbols[(edge[0], edge[1])])

            # Guardar el grafo en un archivo PNG
            G.render(output_file, view=True)

# Función para escribir todas las transiciones en un archivo de texto
    def writeTransitionsToFile(self, filename):
        self.getTransition()
        with open(filename, "w") as file:
            for i, j in self.trans_symbols.items():
                file.write(f"{i[0]} --> {i[1]}: {j}\n")
        print(f"Transitions written to file '{filename}'")
