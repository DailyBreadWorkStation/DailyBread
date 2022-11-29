# data = r'C:\Users\ppsde\logs\clamp.txt'
# with open(data, 'r', encoding='utf-8') as f:
#    lines = f.readlines()
#    print(lines)
# import codecs
# f = codecs.open('C:\\Users\\ppsde\\logs\\clamp.txt',"w",encoding= "utf-8")
# import os
# def rename(directory):
#     for name in os.listdir(directory):
#         print(name)
#         os.rename(os.path.join(directory,name), 
#     os.path.join(directory,'0'+name))
# path = input(r"C:\\Users\\ppsde\\logs\\clamp.txt")
# rename(path)
import subprocess
subprocess.run(['yts', 'discover'], capture_output=True, shell=True)
