import cv2 
import random
img = cv2.imread('assets/hamkroun.png', -1)

tag = img [100:200, 250:350]
img[50:150 , 200:300] = tag

# print(type(img))
print(img.shape) #height, width,channels

print(img[45:400])

# for i in range(100): # for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()