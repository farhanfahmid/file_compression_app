import FreeSimpleGUI as sg
import zipper

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

#define success message
success_message = sg.Text(key="output")


# design the gui window
window = sg.Window(title="File Zipper",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_button, success_message]])

while True:
    event, values = window.read()
    print("event: ", event)
    print("values: ", values)
    filepaths = values['filepath'].split(";")
    folderpaths = values['folderpath']
    zipper.make_archive(filepaths, folderpaths)
    window['output'].update(value = "Compression Successful!")

    match event:
        case sg.WINDOW_CLOSED: break

window.close()



