import argparse
import random

def newton_method(func, start_x, max_iter, d, precision, max_restarts = 5):
    x = start_x
    restarts = 0
    while restarts <= max_restarts:
        for it in range(max_iter):
            fx = func(x)
            dfx = (func(x+d)-func(x))/d
            if abs(dfx)<1e-10:
                print(f'utknięto w punkcie:{x:.4f}')
                x = random.uniform(-10,10)
                restarts += 1
                break
            x_new = x - fx / dfx
            if abs(x_new - x) < precision:
                return f'x = {x}, max_iter = {max_iter +1}, restarts = {restarts}'
            x = x_new
        else:
            return f'x = {x}, max_iter = {max_iter}, restarts = {restarts}'
    return None    

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('formula', type=str, help='funkcja jako def arg')
#     parser.add_argument('-start', '--starting_point', type=float, help='punkt startowy', default= 1.0)
#     parser.add_argument('-n', '--max_iter', type=int, help='maxymalna ilość iteracji', default=100)
#     parser.add_argument('-d', '--delta', type=float, help='iloraz różnicowy', default=0.00001)
#     parser.add_argument('-p', '--precision', type=float, help='precyzja strzału', default=0.00001)
#     args = parser.parse_args() 
#     func = lambda x : eval(args.formula , {'x' : x, '__builtins__':{}})   
#     print(f"Start: {args.starting_point}, Iteracje: {args.max_iter}")
#     wynik , iteracje, restarty = newton_method(func, args.starting_point, args.max_iter, args.delta, args.precision)
#     print(f'Znalezione miejsce zerowe: {wynik:.5f} po {iteracje} krokach. ilość restartów: {restarty}')
# if __name__ == "__main__" :
#     main()


print(newton_method(lambda x : x**2 + 5*x -10, 0,100,1e-10,1e-10))