# The path.exists() method is used to check whether a filepath exists in OS,
# and the makedirs() method is used to create directories;
from os import path, makedirs

################ CREATE ORIGINAL FILE, WRITE TO IT, CREATE COPIES

# This is the directory where we will be storing our original file and its
# copies, we assign it to a descriptive variable for efficiency; 
# the double backslashes are used to insert literal backslashes since this script was 
# written for Windows;
directory = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\'

# Checks the filepath to see if the directory exists; if it does NOT exist...
if not path.exists(directory):
    
    # then create it;
    makedirs(directory)

# Create the name for the original text file and assign it to the variable, 
# this is the file we will copy from to create the ten duplicate
# (besides the names) files;
orig_file = 'original.txt'

# We need to use the full filepath for the path.exists() method below;
# the double backslashes are used to insert literal backslashes since this
# script was written for Windows;
orig_full_path = 'C:\\Users\\slushy\\Desktop\\Python\\write.py\\test_files\\original.txt'

# We will use this variable to write the string to our original.txt file;
text = 'Copy this text from original.txt to 10 other text files.'

# If the full filepath of original.txt does NOT exist...
if not path.exists(orig_full_path):
    
    # then create (open) original.txt at the filepath in write mode;
    # we use 'with open as' so f gets closed automatically at end of block;
    with open(orig_full_path, 'w') as f:

        # Then write the text (string) to it;
        f.write(text)

        print()
        print(f'{orig_file} was created and written successfully.')
        print()

# Else if original.txt already exists at that filepath...
elif path.exists(orig_full_path):
    print()
    # simply print out this message and don't do anything else;
    print(f'File {orig_file} already exists in the directory {directory}.')
    print()

else:
    print()
    print('An error has occurred, please investigate and try again.')
    print()

# Copy the text from the original file and use it to create 10 new files,
# each with a different name;

# Open original.txt at its full filepath in read mode under the variable name,
# orig_file; using 'with open' ensures the file gets closed automatically 
# after exiting the 'with' block without having to explicitly use close();
with open(orig_full_path, 'r') as orig_file:
    
    # Read the contents of the file and assign the contents to the variable,
    # content;
    content = orig_file.read()

# Since we are trying to create ten duplicate files (aside from the name),
# we set up a loop that will begin at 1 and end at 10 (the 11 is exclusive);
for i in range(1, 11):

    # Every loop, we create a new file that contains the same text as
    # original.txt, and we add the current value of i in the filename;
    # then we assign the full filepath of the new file to the variable;
    new_full_path = (f'{directory}copy_file{i}.txt')
    
    # Check whether the new file already exists at its full filepath;
    # if it does NOT exist...
    if not path.exists(new_full_path):
        
        # open (create) new file at its full filepath in write mode;
        # again, using 'with open' ensures the file is closed automatically
        # after exiting the 'with' block;
        with open(new_full_path, 'w') as new_file:
            
            # Write the content (contents of original.txt) to it;
            new_file.write(content)
            #new_file.close()

            print(f'copy_file{i} was created and written successfully.')
    
    # Else if new file already exists at its full filepath... 
    elif path.exists(new_full_path):
        
        # just print out this message, don't do anything else;
        print(f'copy_file{i} already exists in {directory}.')

print()

################### ORGANIZE AND CLEAN UP

# os.walk() allows us, in this case, to loop through the contents of a folder
# at a specified path;
from os import walk

# shutil.move() is used to move/rename files, and shutil.rmtree() is used to
# delete entire directories and their contents;
from shutil import move

# We defined the filepath to test_files\ near the top and assigned it to the
# variable, directory; now we use the 'root, dirs, files in walk' to enumerate
# our entire directory, even though we will only use the files; 
for root, dirs, files in walk(directory):
    
    # Now that we have enumerated our files, we can proceed to loop through
    # them one by one;
    for file in files:
        
        # Define the substring as '.txt' because that's what we want to remove
        # from the filename in order to create a directory with the same name;
        substr = '.txt'
        
        # We use the replace() function to replace the substring we defined
        # above with nothing (''), effectively deleting it;
        edit_file = file.replace(substr, '')

        # We join the filepath of the directory with the name of the directory
        # in order to define its full filepath;
        new_fldr = ''.join(f'{directory}' + f'{edit_file}\\')

        # This is the full SOURCE filepath of the text file;
        filepath = (directory+file)

        # We want to check whether the new folder(s) we want to create already
        # exist;
        if not path.exists(new_fldr):

            # Create a subdirectory of the current directory with the same name as the
            # file in this iteration;
            makedirs(new_fldr)
            print(f'{new_fldr} created successfully.')

        # This is the full DESTINATION filepath of the text file;
        new_filepath = (new_fldr+file)

        # Check whether the file already exists at destination path, and if it
        # doesn't then we move it there;
        if not path.exists(new_filepath):
            move(filepath, new_filepath)
            print(f'{file} moved successfully to the folder {new_fldr}.')