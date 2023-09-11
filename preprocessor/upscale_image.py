import os
import cv2
filename = "/nfs/home/luorui/Tag2Pix/Tag2Pix-master/dataset/train_image_base"
filename_1 = "/nfs/home/luorui/Tag2Pix/Tag2Pix-master/dataset/cropped_rgb"
filedir = os.listdir(filename)
int size=768
for file in filedir:
    filepath=filename+'/'+file
    img = cv2.imread(filepath)
    print(img.shape)
    img = cv2.resize(img, (size, size), cv2.INTER_LINEAR)
    cv2.imwrite(filepath,img)
    print(img.shape)
    print("写入成功！")