#!/usr/bin/python3
def weight_average(my_list=[]):
        suma = 0
        prom = 0
        for line in my_list:
                suma += line[0] * line[1]
                prom += line[1]
        return(suma/prom)
