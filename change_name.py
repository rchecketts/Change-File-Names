def change_name(look_for, replace_with, directory, test = False):
    '''
    purpose:
        This will look in a folder and will update filenames based on changes
        you would like to make.
    
    inputs:
        look_for: str, the string that will be replaced in the filename
        replace_with: str, the string that will replace the old string
        directory: str or pathlib.Path, folder to look in
        test: boolean, test = False will make changes, test = True only shows what will happen
        
    outputs:
        None
        
    examples:
        change_name(look_for = "tst2", replace_with = "tst20", directory = "C:\\Users\\u0408224\\Downloads", test = False)
        change_name(look_for = "tst2", replace_with = "tst20", directory = "C:\\Users\\u0408224\\Downloads", test = True)
    '''
    
    
    #Import Libraries
    from os import rename
    from os import listdir
    from pathlib import Path
    
    pathdir = Path(directory)
    
    n_changes = 0
    
    #This is to test what will be changed
    if test == True:
        for i in listdir(pathdir):
            if look_for in i:    
                n_changes += 1
                print("Test Mode. Change {} to {}".format(i, i.replace(look_for,replace_with)))
            else:
                print("No change needed for {}".format(i))
                
        print("Test Mode. There would have been {} changes made.".format(str(n_changes)))
    
    #This will make actual changes (test = True)
    else:
        for i in listdir(pathdir):
            if look_for in i:    
                n_changes += 1
                rename(pathdir / i, pathdir / i.replace(look_for,replace_with))
                print("Changed {} to {}".format(i, i.replace(look_for,replace_with)))

        print("Complete! There were {} changes made.".format(str(n_changes)))    
    
    
    
