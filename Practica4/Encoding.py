import base64
imagen1 = open('vol1.jpg', 'rb')
imagen2 = open('blueeyes.jpg', 'rb')
holam = open('hola mundo.cpp', 'rb')
imagen1_read = imagen1.read()
imagen2_read = imagen2.read()
holam_read = holam.read()
imagen1_encode = base64.encodebytes(imagen1_read)
imagen2_encode = base64.encodebytes(imagen2_read)
holam_encode = base64.encodebytes(holam_read)
imagen1_decode = base64.decodebytes(imagen1_encode)
imagen2_decode = base64.decodebytes(imagen2_encode)
holam_decode = base64.decodebytes(holam_encode)
imagen1_res = open('img1_decode.jpg', 'wb')
imagen2_res = open('img2_decode.jpg', 'wb')
holam_res = open('holam_decode.txt', 'wb')
imagen1_res.write(imagen1_decode)
imagen2_res.write(imagen2_decode)
holam_res.write(holam_encode)
holam_res.write(holam_decode)
holam_res.close()
