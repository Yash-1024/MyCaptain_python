# Task 1
radius = int(input("Input the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {3.14*radius**2}")


# Task 2
file_Name = input("Input the Filename: ")
extentions = {".doc": "doctype",".docx": "doctype",".html" : "hyper text markup language",".htm" : "hyper text markup language",".odt" : "OpenOffice Document file",".pdf" : "Portable Document Format",".xls" : "Excel Binary File Format",".xlsx" : "Excel Workbook",".ods" : "OpenDocument Spreadsheet",".ppt" : "PowerPoint file",".pptx" : "default presentation file format",".txt" : "text file",".py" : "python file",".java" : "java file",".c" : "c language file",".css" : "Cascading Style Sheets",".json" : "JavaScript Object Notation"}


try:
    with open('extension_list.txt', 'r') as f:     #  A file with name extention_list.txt exists with name of all above extension in it 
        for i in range(17):
            text = f.readline()
            text = text.lower()
            text = text.replace("\n","")
            # print(text)
            if (file_Name.find(text) != -1):
                print(f"The extension of the file {file_Name} is : {extentions.get(text)}")
                break
        else:
            print("!!!---Extension not recorgised---!!!")
except Exception as e:
    print("You do not have a file of extention to run this program\nKindly download the file extension file and run again")
finally:
    print("Run sucessful")


