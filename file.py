try:
    file=open("sample.txt",'r')
    reading_file=file.read()
    print("Reading File Content: ")
    print(reading_file)
    file.close()

except FileNotFoundError:
    print("Error: The file sample.txt is not found")