import cv2
import os
import numpy as np

#i created 2 different classes in order to be more intuitive to understand the concept

def rectify_right(img_path):
    img=cv2.imread(img_path)
    count=img_path.split('/')[-1]
    #Camera matrix provides details about intrinsics of the camera sensor 
    cameraMatrix=np.array([[526.866127, 0.000000, 315.455904],
                            [0.0, 525.2691751508863, 234.380157],
                            [ 0.0, 0.0, 1.0]])
    
    distortion=np.array([-0.351948, 0.141118 ,0.001470, -0.000935, 0.0000])
    
    rectification=np.array([[0.999900,-0.002158, -0.018235],
                    [0.002099, 0.999997, -0.003222],
                    [0.018241, 0.003183, 0.999829]])

    """projection=[[501.301670, 0.000000, 325.716686, 0.000000],
                [0.000000, 501.301670, 244.231571 ,0.000000],
                [0.000000, 0.000000, 1.000000 ,0.000000]]"""
    NewCameraMtx=cv2.getOptimalNewCameraMatrix(cameraMatrix,distortion,(640,480),0)
    necammtrx=NewCameraMtx[0]
  
    map1,map2=cv2.initUndistortRectifyMap(cameraMatrix,distortion,rectification,necammtrx,(630,480),cv2.CV_32FC1)

    rect_img=cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
    cv2.imwrite(os.path.join('/media/evdo/INTENSO/SBC_diplomatiki_backup/dataset/right_rectified',count),rect_img)
    


def rectify_left(img_path):
    img=cv2.imread(img_path)
    count=img_path.split('/')[-1]
    cameraMatrix=np.array([[521.915083, 0.000000, 318.494617],
                            [0.000000, 520.459241, 252.232156],
                            [ 0.0, 0.0, 1.0]])
    
    distortion=np.array([-0.345397, 0.133021 ,-0.000488, -0.001225, 0.0000])
    
    rectification=np.array([[0.999900 ,-0.000077, -0.014112],
                    [0.000122, 0.999995 ,0.003202],
                    [0.014111 ,-0.003203, 0.999895]])

    NewCameraMtx=cv2.getOptimalNewCameraMatrix(cameraMatrix,distortion,(640,480),0)
    necammtrx=NewCameraMtx[0]
  
    map1,map2=cv2.initUndistortRectifyMap(cameraMatrix,distortion,rectification,necammtrx,(630,480),cv2.CV_32FC1)

    rect_img=cv2.remap(img,map1,map2,cv2.INTER_LINEAR)
    cv2.imwrite(os.path.join('/media/evdo/INTENSO/SBC_diplomatiki_backup/dataset/left_rectified',count),rect_img)




if __name__ == "__main__":
    #insert path of dataset directory which includes the subdirectories
    # r=root, d=directories, f = files
    for r,d,f in os.walk('/path/of/dataset/directory'):
        for files in f:
            if files.endswith(".jpg"):
                if r.split('/')[-1]== 'right_unrectified':
                    rectify_right(os.path.join(r,files))
                else:
                    rectify_left(os.path.join(r,files))
