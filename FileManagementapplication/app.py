import os

def create_file(filename):
    try:#used if already file exists
        with open(filename,'x') as f:
            print(f"file {filename}: created successfully")
    except FileExistsError:        
        print(f"file {filename}: already exists")
    except Exception as E:
        print('an error occured')

def view_all_files():
    files=os.listdir()            
    if not files:
        print('no files found')
    else:
        print('file found')  
        for file in files:
            print(file)  
def delete_file(filename):            
    try:
        os.remove(filename)
        print(f'file {filename}: has been deleted successfully')
    except FileNotFoundError:    
        print(f'file {filename}: does not exist')
    except Exception as e:
        print('an error occured')    

def read_file(filename):        
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f'content of {filename}:\n{content}')
    except FileNotFoundError:
        print(f'file {filename}: does not exist')
    except Exception as e:
        print('an error occured')

def edit_file(filename):        
    try:
        with open(filename,'a') as f:
            content=input('enter the content you want to add:')
            f.write(content + '\n')
            print(f'content added{filename} successfully')
    except FileNotFoundError:
        print(f'file {filename}: does not exist')  
    except Exception as e:
        print('an error occured')    

def main():
    while True:              
        print('FILE MANAGEMENT APPLICATION')
        print('1.create file')
        print('2.view all files')
        print('3.delete file')
        print('4.read file')
        print('5.edit file')
        print('6 exit')

        choice=input('Enter a choice (1-6):')
        if choice == '1':
            filename=input('Enter the file to create ==')
            create_file(filename)
        elif choice == '2':  
          view_all_files()
        elif choice == '3':
            filename=input('Enter the file to delete ==')  
            delete_file(filename)
        elif choice == '4':
            filename=input('Enter the file to read ==')            
            read_file(filename)
        elif choice == '5':    
            filename=input('Enter the file to edit ==')            
            edit_file(filename)
        elif choice == '6': 
            print('THANKS FOR USING FILE MANAGEMENT APPLICATION')   
            break
        else:
            print('invalid choice')

if __name__ == '__main__':            
    main()
       