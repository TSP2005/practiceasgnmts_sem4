import cv2
import pandas as pd
img= cv2.imread("L_dn.png",cv2.IMREAD_GRAYSCALE)
pd.DataFrame(img).to_csv('matrix.csv',index=False)
df=pd.read_csv('matrix.csv').iloc[:-1,:-1]
df.to_excel('excel.xlsx',index=False)