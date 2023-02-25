# this code will generate qr codes of links gien by he user
import qrcode  #if any library is not installed then type ( pip install library_name) in terminal to install that respective library

def generate(url):
    #creating an object(creating an empty qr code with required specs)
    qr=qrcode.QRCode(version=1, # ranged from 1 to 40 depending on size of url/data
    error_correction=qrcode.constants.ERROR_CORRECT_H, # corrects error in qrcode r(L ,M,Q, H)
    box_size=10, #no of pixcels in each block of qrcode
    border=4, #used to control thickness of border
    )    

    qr.add_data(url)  #puts url data in raw qrcode
    qr.make(fit=True)  #if no specs specified in object creation code it will set specs automatically

    img=qr.make_image(fill_color="black",back_color="white")  #creates qrcode img from above qrcode object

    img.save("qrcodep5.png")  #saves image in current folder


url=input("paste link here to generate qrcode")  
generate(url) #the created qrcode is which explains all of this code in google for future references 