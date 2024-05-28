# First try-except-finally block
try:
    f = open("kristal.txt")  # This file exists in the directory
except Exception as e:
    print(e)
    f = None  # To be safe, file pointer points to nothing
else:
    print("Opened successfully\n")
finally:
    print("Finally will run anyway")
    if f:
        f.close()

# Second try-except-finally block
try:
    f1 = open("_existing_file.txt")  # This file doesn't exist, so it will throw an error
    # even if this file exists, finally block will be executed anyway

# Multiple exceptions
except EOFError as e:  # When end of file error encounters
    print("EOF ERROR HAS OCCURED", e)
except IOError as e:  # When input/output error encounters
    print("IO ERROR HAS OCCURED", e)
except KeyboardInterrupt as e:
    print("Keyboard interrupt error occurred", e)
except Exception as e:  # It catches any type of error, the most general
    # similar to catch any exception in C++
    print("ERROR occurred:", e)
    f1 = None
else:  # When no error occurs
    print("Else will run only if except block doesn't run")
    print("Program running successfully up to now")
finally:
    print("This will run anyway")  # You should close the files when the program encounters an error for code cleanup
    if f1:
        f1.close()

print("IMPORTANT STUFF TO RUN")
