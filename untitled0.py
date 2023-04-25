from tkinter import *

root=Tk()

root.title("fibonacci")
root.geometry("400x400")

label_series=Label(root,text="fibonacci")
label_flower=Label(root)
label_spiral=Label(root)

def fibonacci():
    
    num = 10
    first_num=0
    sec_num=1
    sum=0
    counter=1
while (counter<=num):        
label_series["text"] += str(sum) +" "
counter=counter+1 
first_num = sec_num
sec_num=sum
sum=first_num+sec_num
label_flower['text'] ="flower is fully bloomed"
label_spiral['text'] ="spiral in right direction are"+
str(first_num)+"and spiral in left direction are"+str(sec_num)+
"\n.total spirals are"+str(sum)

btn = Button(root,text="fibonacci",command=fibonacci)    
btn.pack()
label_flower.pack()
label_series.pack()
label_spiral.pack()    
    

root.mainloop();

