#read text file
def read_file(file_path):
    with open(file_path) as file:
        data = file.read()
        return data
    
#store content in a variable
file_content = read_file('data/medical_data.txt')

#print the content of the file
print(file_content)