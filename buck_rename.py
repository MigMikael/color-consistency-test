import os

device = "iPad"
images_dir = "./" + device +"_image/"

verbose = 1

count = 1
for filename in os.listdir(images_dir):
    if filename.endswith(".jpg") or filename.endswith(".JPG") :
        name, extension = filename.split(".")
        old_name = images_dir + filename
        new_name = images_dir + str(count) + "." + extension
        os.rename(old_name, new_name)
        
        if count % verbose == 0:
            print(count, "Finish", str(count) + "." + extension)
            
        count +=1