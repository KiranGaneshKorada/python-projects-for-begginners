from PIL import Image

image=Image.open("image_resize_sample_ori.jpg")

print("current dimensions of image={}\n\n".format(image.size))

resized_image=image.resize((500,500))

resized_image.save("resized_image.jpg")