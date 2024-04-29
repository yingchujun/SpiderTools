from PIL import Image


# 保存路径在36行代码可以进行修改【默认保存在当前目录下，并且按照裁剪顺序命名】
def cutIntoEqualParts(picturePath: str, cropSize: tuple) :
    """
    :param picturePath: 图片路径
    :param cropSize: 裁剪图片大小
    """
    img = Image.open(picturePath)  # 图片路径
    cropSize = (100, 100)  # 宽, 长  [需要裁剪的大小] 


    # 获取原图宽长
    imgWidth = img.size[0]
    imgHeight = img.size[1]

    # 获取裁剪图宽长
    cropWidth = cropSize[0]
    cropHeight = cropSize[1]



    # 左上坐标 x , y
    positionLeft = 0 
    positionUpper = 0

    # 右下坐标 x , y
    positionRight = cropWidth
    positionLower = cropHeight

    count = 1
    while positionRight <= imgWidth  and positionLower <= imgHeight:
        cropPosition = (positionLeft, positionUpper, positionRight, positionLower)
        cropped = img.crop(cropPosition)
        cropped.save('./{}.jpg'.format(count))
        count += 1

        positionLeft += cropWidth
        positionUpper = positionUpper 

        positionRight += cropWidth
        positionLower = positionLower

        if positionLeft == imgWidth:
            positionLeft = 0
            positionUpper += cropHeight

            positionRight = cropWidth
            positionLower += cropHeight



# cutIntoEqualParts('./下载.jpg', (100, 100))