__author__ = 'Hernan Y.Ke'

prices = {
    'A': 100,
    'B': 10,
    'C': 20,
    'D': 50
}

#extract1

subdict1 = {key:value for key,value in prices if value>50}

subdict1 = dict((key,value) for key,value in prices if value>50)  #alternative  note syntax. (faster)