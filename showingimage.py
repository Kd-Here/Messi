# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()
# root.title("KD Show")
# root.geometry("1000x600")
# root.config(bg="black")
# root.resizable(0, 0)


# def start():                                                     
#     global i, show
#     if i >= (len(images)-1):
#         i = 0
#         slide_image.config(image = images[i])
#     else:
#         i = i + 1
#         slide_image.configure(image = images[i])
#     show = slide_image.after(2000 , start)
# def stop():
#     global show
#     slide_image.after_cancel(show)
    
# def resume():
#     start()
# img1 = Image.open('slide1.png')
# img1.thumbnail((600, 650))      # 650 --> 550
# img2 = Image.open('slide2.png')
# img2.thumbnail((600, 650))
# img3 = Image.open('slide3.png')
# img3.thumbnail((600, 650))
# img4 = Image.open('slide4.png')
# img4.thumbnail((600, 650))




# im=Image.open('messi.jpg')
# #im1 = im.filter(ImageFilter.BoxBlur(4))
# im1 = im.filter(ImageFilter.GaussianBlur)
# im1 = im.filter(ImageFilter.DETAIL)
# #im1 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
# #im1 = im.filter(ImageFilter.FIND_EDGES)
# #im1 = im.filter(ImageFilter.UnsharpMask(4))


# #we wanted to create image presernation i.e. lsoide shown for our oillow images

# im1.show()


from PIL import Image, ImageFilter
#pil is module used for processing Images in Python


pahila =Image.open("messi.jpg")
#here think why we used Image.open instead of open bcoz python is name spaced we need to tell which open we need here we wanted open of module Image so Image.open
#inside of Image lib there function that takes arguments name of fiel which u wnateed to open

natr = pahila.filter(ImageFilter.BoxBlur(10))
#pahila we used here as object so filter is method of class who takes  argumeent as ImageFilter.BoxBlur(10)
#remember we used objectname.class name

ask=natr.save("MessiGoal.png")


# natr.show()