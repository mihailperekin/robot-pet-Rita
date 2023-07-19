import face_recognition
from PIL import Image, ImageDraw

def face():
    me = face_recognition.load_image_file('nekit.jpg')
    nekit = face_recognition.face_locations(me)
    print(nekit)

    pil_img1 = Image.fromarray(me)
    draw = ImageDraw.Draw(pil_img1)

    for(top,right,bottom,left) in nekit:
        draw.rectangle(((left,top),(right,bottom)), outline=(255,0,0), width= 4)
    del draw
    pil_img1.save('out.jpg')
def maim():
    face()

maim()