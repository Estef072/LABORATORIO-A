from State import State
from Automata import Automata

def InfixPostfix(regex:str):
    if PosiblesErrores(regex)==False:
        return None
    precedence = {"|": 0, ".": 1, "*": 2, "+": 2, "?": 2}
    newRegex = ""
    #Agrega un signo ? cada vez que hay una concatenación
    for i in range(len(regex)):
        if i == len(regex)-1:
            newRegex += regex[i]
        else:
            if regex[i+1] not in precedence.keys() and regex[i+1]!= ")":
                if regex[i] == "*":
                    newRegex += regex[i]
                    newRegex += "."
                elif regex[i] == "?":
                    newRegex += regex[i]
                    newRegex += "."
                elif regex[i] == "+":
                    newRegex += regex[i]
                    newRegex += "."
                elif regex[i] not in precedence.keys() and regex[i]!="(":
                    newRegex += regex[i]
                    newRegex+= "."
                else:
                    newRegex+=regex[i]
            else:
                newRegex +=regex[i]
                
    postfixString = ""
    operatorStack = []
    regex = newRegex
    #convertir infix postfix
    for i in regex:
        #print(i)
        if i in precedence.keys() or i=="(" or i == ")":
            if len(operatorStack)==0 or operatorStack[-1]=="(" or i == "(":
                operatorStack.append(i)
            elif i == ")":
                check = ""
                while check!="(":

                    postfixString += operatorStack.pop()
                    check = operatorStack[-1]
                operatorStack.pop()
            elif precedence[i] < precedence[operatorStack[-1]]:
                while precedence[i] < precedence[operatorStack[-1]]:
                    postfixString += operatorStack.pop()
                    if len(operatorStack) == 0 or operatorStack[-1]=="(":
                       break
                operatorStack.append(i)
            elif precedence[i] > precedence[operatorStack[-1]]:
                operatorStack.append(i)
            elif precedence[i] == precedence[operatorStack[-1]]:
                postfixString += operatorStack.pop()
                operatorStack.append(i)
                
        else:
            postfixString += i
        #print("stack: ", operatorStack, "string: ", postfixString)
    while len(operatorStack)!=0:
        postfixString += operatorStack.pop()
    return (postfixString)

def Thompson(expression:str):
    expression = InfixPostfix(expression)   
    stack = []
    # "#" representa epsilon
    contador = 0
    for i in expression:
        
        #UNION
        #Forma:
        #con epsilon: S0 (inicio) -> s1 
        #con epsilon: S0 (inicio) -> s2
        #con char1: S1 -> S3
        #con char2: S2 -> S4
        #con espsilon: S3 -> S5 (final)
        #con espsilon: S4 -> S5 (final)
        
        if i == "|":
            inicio = State(name = f's{contador}')
            contador+=1
            end = State(name = f's{contador}')
            afn1 = stack.pop()
            afn2 = stack.pop()
            inicio.AddTransition(afn1.start, "#") #S0 (inicio) -> S1
            inicio.AddTransition(afn2.start, "#") #S0 (inicio) -> S2
            afn1.final.AddTransition(end, "#")    #S3 -> S5 (final)
            afn2.final.AddTransition(end, "#")    #S4 -> S5 (final)
            afn = Automata(inicio, end)
            stack.append(afn)
            
        elif i == "+":
            inicio = State(name = f's{contador}')
            contador+=1
            end = State(name = f's{contador}')
            afn1 = stack.pop()
            inicio.AddTransition(afn1.start, "#")
            afn1.final.AddTransition(afn1.start, "#")
            afn1.final.AddTransition(end, "#")
            afn = Automata(inicio, end)
            stack.append(afn)
        
        elif i == ".":
            afn1 = stack.pop()
            afn2 = stack.pop()
            afn2.final.transitions = afn1.start.transitions
            afn = Automata(afn2.start, afn1.final)
            stack.append(afn)
            
            
        

        elif i == "?":
    
            inicio = State(name = f's{contador}')
            contador+=1
            end = State(name = f's{contador}')
            afn1 = stack.pop()
            inicio.AddTransition(afn1.start, "#")
            afn1.final.AddTransition(end, "#")
            inicio.AddTransition(end, "#")
            afn = Automata(inicio, end)
            stack.append(afn)
            
        #Estrella de Kleene
        #Forma:
        #con epsilon: S0 (inicio) -> S1 (inicio del automata de stack)
        #con epsilon: S2 (final del automata de stack) -> S1 (inicio del automata de stack)
        #con epsilon: S2 (final del automata de stack) -> S3 (final)
        #con epsilon: S0 (inicio) -> S3 (final)
        
        elif i == "*":
            inicio = State(name = f's{contador}')
            contador+=1
            end = State(name = f's{contador}')
            afn1 = stack.pop()
            inicio.AddTransition(afn1.start, "#")
            afn1.final.AddTransition(afn1.start, "#")
            afn1.final.AddTransition(end, "#")
            inicio.AddTransition(end, "#")
            afn = Automata(inicio, end)
            stack.append(afn)
            
        #Inicilización de elementos del alfabeto
        #forma:
        #con char: start -> fin
        
        else:
            #print(contador)
            #print(i)
            inicio = State(name = f's{contador}')
            contador+=1
            end = State(name = f's{contador}')
            inicio.AddTransition(end, i)
            

            afn = Automata(start = inicio, final = end)
            stack.append(afn)
        if i!=".":
            contador +=1
    return stack.pop()


def PosiblesErrores(regex: str):
    operadores = ["|","*","+",".","?"]
    if not regex:
        return False
    
    if regex[0] in operadores:
        return False