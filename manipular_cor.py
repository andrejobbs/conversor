import cv2 as cv
imagem = cv.imread('/conversor/img_manipular_cor/cidade_3.jpg.jpg', cv.IMREAD_UNCHANGED)   
imagem_cinza=cv.cvtColor(imagem,cv.COLOR_BGR2GRAY)

cv.imshow('cidade_3.jpg', imagem_cinza) 
cv.waitKey(0) 
cv.destroyAllWindows()
# gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
  
# cv.imshow('Grayscale', gray_image) 
# cv.waitKey(0)   
 