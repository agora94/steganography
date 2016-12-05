
import cv2
import numpy as np

base_cover = 512
height_cover = 512
base_stego = 512
height_stego = 512
img_cover = cv2.imread('cover.jpg')
img_stego = cv2.imread('stego.jpg')
bits_used = 5

def embed():
    if base_cover >= base_stego and height_cover >= height_stego:
        for x in range(base_stego):
            for y in range(height_stego):
                cover_pixel = img_cover[x,y]
                cover_red = '{0:08b}'.format(cover_pixel[0])
                cover_green = '{0:08b}'.format(cover_pixel[1])
                cover_blue = '{0:08b}'.format(cover_pixel[2])
                stego_pixel = img_stego[x,y]
                stego_red = '{0:08b}'.format(stego_pixel[0])
                stego_green = '{0:08b}'.format(stego_pixel[1])
                stego_blue = '{0:08b}'.format(stego_pixel[2])
                result_red = cover_red[0:8-bits_used] + stego_red[0:bits_used]
                result_green = cover_green[0:8-bits_used] + stego_green[0:bits_used]
                result_blue = cover_blue[0:8-bits_used] + stego_blue[0:bits_used]
                result_pixel = [int(result_red, 2), int(result_green, 2), int(result_blue, 2)]
                img_cover[x,y] = result_pixel
    cv2.imwrite('result5.jpg', img_cover)
    
def extract():
    img_result = cv2.imread('resultasdf.jpg')
    if base_cover >= base_stego and height_cover >= height_stego:
        for x in range(base_stego):
            for y in range(height_stego):
                result_pixel = img_result[x,y]
                result_red = '{0:08b}'.format(result_pixel[0])
                result_green = '{0:08b}'.format(result_pixel[1])
                result_blue = '{0:08b}'.format(result_pixel[2])
                zero = '{0:08b}'.format(0)
                extract_red = result_red[8-bits_used:8] + zero[0:bits_used]
                extract_green = result_green[8-bits_used:8] + zero[0:bits_used]
                extract_blue = result_blue[8-bits_used:8] + zero[0:bits_used]
                extract_pixel = [int(extract_red, 2), int(extract_green, 2), int(extract_blue, 2)]
                img_result[x,y] = extract_pixel
    cv2.imwrite('extractasdf.jpg', img_result)
    
               