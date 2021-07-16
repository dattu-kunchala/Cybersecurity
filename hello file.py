import sys, os ,time

user = input('enter your name please')
print('hello', user, 'you are using python version :', sys.version, 'version', )
if os.name == "nt":
    while(1):
        print("1.system details\n2.ram details\n3.compiler versions\n4.directx version\n5.quit")
        usr_select = int(input('choose your options'))
   
        if usr_select == 1:
            print(os.system('msinfo32'))
            time.sleep(1)
        if usr_select ==2:
            print("no of ram slots available and ram size in eah slot :")
            print(os.system('wmic MEMORYCHIP get BankLabel,capacity'))
            print('\n')
            time.sleep(1)
            print("Device locator:")
            print(os.system('wmic MEMORYCHIP get BankLabel,devicelocator'))
            print('\n')
            time.sleep(1)
            print('memory type:','(note:if output displayed :\n26->DDR4,\n25->DDR3,\n24->DDR2-FB DIMM,\n22->DDR2)')
            print(os.system('wmic MEMORYCHIP get BankLabel,SMBIOSMemoryType'))
            print('\n')
            time.sleep(1)
            print('type of ram: ')
            print(os.system('wmic MEMORYCHIP get BankLabel,TypeDetail'))
            print('\n')
            time.sleep(1)
            print('memory speed:')
            print(os.system('wmic MEMORYCHIP get BakLabel,speed'))
            print('\n') 
            time.sleep(1)
        if usr_select == 3:
            print("C compiler version:")
            print(os.system('gcc-v'))
            print('\n')
            time.sleep(1)
        
        if usr_select == 4:
            print("your system direct x version is:")
            print(os.system("dxdiag"))
            print('\n')
            time.sleep(1)
        if usr_select == 5:
            print("you choose to exit thank you for using the program")
            break;
    
        