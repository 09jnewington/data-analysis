import numpy as np
import pandas as pd

wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")

wh.drop('Snow depth (cm)', axis=1, inplace=True)

def read_series():
    indexes = []
    values = []
    while True:
        
        num = input("Enter index then value with whitespace between them, hit ENTER to end")
        if num == '':
            break
        else:
            index, value = num.split()
            indexes.append(index)
            values.append(value)
    return pd.Series(values, index=indexes)


def create_series(list1:list, list2:list):
    s1 = pd.Series(list1, index=['a', 'b', 'c'])
    s2 = pd.Series(list2, index=['a', 'b', 'c'])

    return s1, s2

def modify_series(s1, s2):
    c = s2['b']
    s1['d'] == c
    s2 = s2.drop('b')

def inverse_series(s1: pd.Series):
    return pd.Series(s1.index, index=s1.value)




def main():
    rs = read_series()
    print(rs)


if __name__ == '__main__':
    main()