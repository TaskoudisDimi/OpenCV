








# # Male
# import cv2
# import numpy as np
# import random

# # i = models
# # j = delta betas
# for i in range(248,251):
#     for j in range(0,193):
#     # print(i)
#     # 
#         try:
    
#             img = cv2.imread(f"D:/Thesis/results/200-250/male/model-{i}/model-{i}tex_c.png")
    
    
#             color1 = img[700:720 , 260:280, :]

#             lower1 = color1[0][0][0] - 10, color1[0][0][1] - 10, color1[0][0][2] - 10
#             lower_color1 = np.array(lower1, dtype=np.int32)
#             upper1 = color1[0][0][0] + 10, color1[0][0][1] + 10, color1[0][0][2] + 10
#             upper_color1 = np.array(upper1, dtype=np.int32)
        
#             mask1 = cv2.inRange(img, lower_color1, upper_color1)

#             indices = np.where(mask1==255)

#             img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
        
    
    

    
    
#             color2 = img[370:390 , 670:680, :]
    
#             lower2 = color2[0][0][0] - 20, color2[0][0][1] - 20, color2[0][0][2] - 20
#             lower_color2 = np.array(lower2, dtype=np.int32)
#             upper2 = color2[0][0][0] + 20, color2[0][0][1] + 20, color2[0][0][2] + 20
#             upper_color2 = np.array(upper2, dtype=np.int32)

#             mask2 = cv2.inRange(img, lower_color2, upper_color2)
        
#             indices = np.where(mask2==255)
        
#             img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
    

        
#             cv2.imwrite(f'C:/Users/ASUS/Desktop/thesis/My_Codes/Create_Delta_betas/data/models_male/textures/model-{i}-{j}.png', img) 
            
#         except:
#             i = i + 1



    




# # # Female
# import cv2
# import numpy as np
# import random

# # i = models
# # j = delta betas
# for i in range(231,246):
#     for j in range(0,192):
#     # print(i)
#     # 
#         try:
    
#             img = cv2.imread(f"D:/Thesis/results/200-250/female/model-{i}/model-{i}tex_c.png")
    
    
#             color1 = img[700:720 , 260:280, :]

#             lower1 = color1[0][0][0] - 10, color1[0][0][1] - 10, color1[0][0][2] - 10
#             lower_color1 = np.array(lower1, dtype=np.int32)
#             upper1 = color1[0][0][0] + 10, color1[0][0][1] + 10, color1[0][0][2] + 10
#             upper_color1 = np.array(upper1, dtype=np.int32)
        
#             mask1 = cv2.inRange(img, lower_color1, upper_color1)

#             indices = np.where(mask1==255)

#             img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
        
    
    

    
    
#             color2 = img[370:390 , 670:680, :]
    
#             lower2 = color2[0][0][0] - 20, color2[0][0][1] - 20, color2[0][0][2] - 20
#             lower_color2 = np.array(lower2, dtype=np.int32)
#             upper2 = color2[0][0][0] + 20, color2[0][0][1] + 20, color2[0][0][2] + 20
#             upper_color2 = np.array(upper2, dtype=np.int32)

#             mask2 = cv2.inRange(img, lower_color2, upper_color2)
        
#             indices = np.where(mask2==255)
        
#             img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
    

        
#             cv2.imwrite(f'C:/Users/ASUS/Desktop/thesis/My_Codes/Create_Delta_betas/data/models_female/textures/model-{i}-{j}.png', img) 
            
#         except:
#             i = i + 1









# # Neutral Female
import cv2
import numpy as np
import random

# i = models
# j = delta betas
for i in range(230,231):
    for j in range(0,192):
    # print(i)
    # 
        try:
    
            img = cv2.imread(f"D:/Thesis/results/200-250/male/model-{i}/model-{i}tex_c.png")
    
    
            color1 = img[700:720 , 260:280, :]

            lower1 = color1[0][0][0] - 10, color1[0][0][1] - 10, color1[0][0][2] - 10
            lower_color1 = np.array(lower1, dtype=np.int32)
            upper1 = color1[0][0][0] + 10, color1[0][0][1] + 10, color1[0][0][2] + 10
            upper_color1 = np.array(upper1, dtype=np.int32)
        
            mask1 = cv2.inRange(img, lower_color1, upper_color1)

            indices = np.where(mask1==255)

            img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
        
    
    

    
    
            color2 = img[370:390 , 670:680, :]
    
            lower2 = color2[0][0][0] - 10, color2[0][0][1] - 10, color2[0][0][2] - 10
            lower_color2 = np.array(lower2, dtype=np.int32)
            upper2 = color2[0][0][0] + 10, color2[0][0][1] + 10, color2[0][0][2] + 10
            upper_color2 = np.array(upper2, dtype=np.int32)

            mask2 = cv2.inRange(img, lower_color2, upper_color2)
        
            indices = np.where(mask2==255)
        
            img[indices[0], indices[1], :] = list(np.random.choice(range(256), size=3))
    

        
            cv2.imwrite(f'C:/Users/ASUS/Desktop/thesis/My_Codes/Create_Delta_betas/data/models_neutral_male/textures/model-{i}-{j}.png', img) 
            
        except:
            i = i + 1










# image = cv2.imread("C:/Users/ASUS/Desktop/thesis/My_Codes/OpenCV/test.png")


# image[700:720 , 260:280, :]   = [0, 0, 255]

# cv2.imwrite("C:/Users/ASUS/Desktop/thesis/My_Codes/OpenCV/image.png", image)




