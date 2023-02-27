from Thompson import Thompson

def prelab():
    ##Prelab
    ##_______inciso1____________
    inciso1 = Thompson("ab*ab*")
    inciso1.Export("inciso1")
    inciso1.writeTransitionsToFile("inciso1.txt")

    ##________inciso2___________
    inciso2 = Thompson("0?(1?)?0*")
    inciso2.Export("inciso2")
    inciso2.writeTransitionsToFile("inciso2.txt")
    ##________inciso3___________
    inciso3 = Thompson("(a*|b*)c")
    inciso3.Export("inciso3")
    inciso3.writeTransitionsToFile("inciso3.txt")
    ##________inciso4___________
    inciso4 = Thompson("(b|b)*abb(a|b)*")
    inciso4.Export("inciso4")
    inciso4.writeTransitionsToFile("inciso4.txt")

    ##________inciso5____________
    inciso5 = Thompson("(a|#)b(a+)c?")
    inciso5.Export("inciso5")
    inciso5.writeTransitionsToFile("inciso5.txt")
    ##________inciso6____________
    inciso6 = Thompson("(a|b)*a(a|b)(a|b)")
    inciso6.Export("inciso6")
    inciso6.writeTransitionsToFile("inciso6.txt")




  
if __name__ == '__main__':
    prelab()

