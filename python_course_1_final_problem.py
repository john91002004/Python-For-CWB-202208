from python_course_1 import convertComplexIntoDict, outputMxNComplexToFile, readFromFile, saveAsJson

def outputMxNComplexAsJson(M, N): 
    outputMxNComplexToFile(M, N)
    complex_list = readComplexTxtFileAsComplexList('MxNComplex.txt')
    complex_dict = convertComplexListIntoDict(complex_list)
    saveAsJson(complex_dict, json_file='MxNComplex.json')

def readComplexTxtFileAsComplexList(filename): 
    s = readFromFile(filename)
    tmp_list = s.split('\n')
    num_list = [] 
    for item in tmp_list: 
        num_list.extend( item.split(', ') ) 
    return [ complex(item) for item in num_list ]

def convertComplexListIntoDict(complex_list):
    complex_dict = {} 
    for item in complex_list: 
        complex_dict[ str(item) ] = convertComplexIntoDict(item) 
    return complex_dict
