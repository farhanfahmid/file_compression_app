import FreeSimpleGUI as sg
import functions

import time

#define the labels first
label1 = sg.Text("Select File(s) to Compress or Extract")
label2 = sg.Text("Select Destination Folder")

#design the input box
input_box1 = sg.InputText(expand_x=True)
input_box2 = sg.InputText(expand_x=True)

#design the buttons
choose_button1 = sg.FilesBrowse("Choose", key='filepath')
choose_button2 = sg.FolderBrowse("Choose", key='folderpath')
compress_button = sg.Button("Compress")
extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")

#define success message
success_message1 = sg.Text(key="compressed")
success_message2 = sg.Text(key="extracted")


# design the gui window
window = sg.Window(title="Ziptract",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_button, extract_button, exit_button],
                           [success_message1, success_message2]])

while True:
    event, values = window.read()
    # print("event: ", event)
    # print("values: ", values)

    match event:
      case "Compress":
        filepaths = values['filepath'].split(";")
        folderpaths = values['folderpath']
        functions.make_archive(filepaths, folderpaths)
        window['compressed'].update(value = "Compression Successful!")
        # make the success message disappear after 7 seconds
        window.refresh()
        time.sleep(7)
        window['compressed'].update(value="")
      case "Extract":
          filepaths = values['filepath']
          folderpaths = values['folderpath']
          functions.extract_archive(filepaths, folderpaths)
          window['extracted'].update(value="Extraction Successful!")
          #make the success message disappear after 7 seconds
          window.refresh()
          time.sleep(7)
          window['extracted'].update(value="")
      case "Exit":
          break



window.close()



