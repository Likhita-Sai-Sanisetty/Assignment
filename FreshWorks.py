import os
import json



print("Enter the path for file creation")
filepath =input()
file = os.path.join(filepath, 'datastore.txt')
# If Path is empty then file named datastore is created at the location of python file
f = open(file, "a")
    
def ins_value():
    
    key = list(map(str,input("Enter json keys separated by ,:\n").split(',')))
    value = list(map(str,input("Enter json values separated by ,:\n").split(',')))
    in_dict=dict(zip(key,value))

    with open("value.json","a")as outfile:
        json.dump(in_dict,outfile)
    return in_dict
    

'''def create():
    print("Enter main key")
    data={}
    
    key = input()
    
    if len(key)<=32 and (key not in data.keys()):
        data[key]=ins_value()
    elif key in data.keys():
        print("Already data exists")
    else:
        print("Key should be small size")
    f = open(file,'a')
    datastore=str(data)
    f.write(datastore)
    
   
         
def read():

    print("Enter the key to Read")
    r=input()
    for item in data:
        if data[item]==r:
            print(data[r])
    
def delete():
    print("Delete")'''
    
def main():
    
    
    while True:
        print(" 1 to create data in datastore\n 2 to read \n 3 to delete\n 4 to exit")
        x=int(input())
        if(x==1):
            #create()
            print("Enter main key")
            data={}
            
            key = input()
            
            if len(key)<=32 and (key not in data.keys()):
                data[key]=ins_value()
            elif key in data.keys():
                print("Already data exists")
            else:
                print("Key should be small size")
            f = open(file,'w')
            datastore=str(data)
            f.write(datastore)
        elif(x==2):
            #read()
            print("Enter the key to Read")
            r_inp=input()
            for item in data:
                if (data[item]==r_inp):
                    print(data[r_inp])
                else:
                    print("Not found create new record")
        elif(x==3):
            delete()
        elif(x==4):
            break
        else:
            print("Enter correct value")   
if __name__=='__main__':
    main()












