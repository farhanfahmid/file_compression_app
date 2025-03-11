import FreeSimpleGUI as sg

#define the labels first
label1 = sg.Text("Select Files to Compress")
label2 = sg.Text("Select Destination Folder")

#design the input box
input_box1 = sg.InputText()
input_box2 = sg.InputText()

#design the buttons
choose_button1 = sg.FilesBrowse("Choose", key='filepath')
choose_button2 = sg.FolderBrowse("Choose", key='folderpath')
compress_button = sg.Button("Compress")


# design the gui window
window = sg.Window(title="File Zipper",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_button]])

while True:
    event, values = window.read()
    print("event: ", event)
    print("values: ", values)
    filepaths = values['filepath'].split(";")
    folderpaths = values['folderpath']

window.close()



