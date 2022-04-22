# webdriver
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# end of webdriver

# args
import sys
# end of args

# config
import os
import configparser
config = configparser.ConfigParser()
# end of config



def readconfig():
    # config = configparser.ConfigParser()
    config.read('config.ini')
    if config['main']['isfirst'] == '1':
        print('first run!')
        print('please insert your username(Student Code) and return:')
        config['main']['username'] = input("请键入学号:")
        print('please insert your password and return:')
        config['main']['password'] = input("请键入密码:")
        config['main']['isfirst'] = '0' 
        with open('config.ini','w') as configfile:
            config.write(configfile)

        

def initconfig():
    # 
    config['main'] = {
        'isfirst' : '1' ,
        'username' : '' ,
        'password' : '' 
    }
    with open('config.ini','w') as configfile:
        config.write(configfile)


def confighandle():
    isExist = os.path.exists('config.ini')
    if not isExist:
        initconfig()
        print('init configfile over!')
    readconfig()
    print(config['main']['password'])
    print("config handle over!")



def main():
    print ('参数个数为:', len(sys.argv), '个参数。')
    print ('参数列表:', str(sys.argv))
    confighandle()
    

if __name__=="__main__":
    main()
