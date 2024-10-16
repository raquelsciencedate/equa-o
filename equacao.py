from math import sqrt
#import math
primeiro_grau = lambda a, b: -b/a
#equacao de segundo grau
def segundo_grau(a,b,c):
    # Calcula o discriminante
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1 = ((-b))+sqrt(delta)/(2*a)
        x2 = ((-b))+sqrt(delta)/(2*a)
        yield  f"Valor real de x': {x}."
        yield  f'Valor real de x": {x}.'
    elif delta == 0:
        x = -b/(2*a)
        yield f"valor real de x: {x1}."
        yield f"valor real de x: {x2}."
    elif delta ==0:
        x = -b/(2*a)
        yield f"Valor  de x': {x}."
    else:
        yield f"não existe valores para essa equação."
        

    
    
    
    
   
    