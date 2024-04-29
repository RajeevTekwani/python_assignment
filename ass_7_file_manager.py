import shutil
import os 
def manage_file():
    name_ls=os.listdir()
    source_dir=r"C:\Users\Rajeev\Desktop\python 45\JECRC"
    for item in name_ls:
        if(item.endswith(".png")):
            shutil.move(os.path.join(source_dir,item),"image_folder")
        elif(item.endswith(".pdf")):
            shutil.move(os.path.join(source_dir,item),"pdf_folder")
        else:
            shutil.move(os.path.join(source_dir,item),"text_folder")
        print(item)
print("files managed!!")

manage_file()

