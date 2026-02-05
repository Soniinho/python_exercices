import cv2
import numpy as np

# Abre o vídeo usando o cv2.VideoCapture
video_path = 'yay2.mp4'
cap = cv2.VideoCapture(video_path)
source = cv2.imread('kirby.jpg')

# processando as infos especiais da imagem auxiliar
(srcH, srcW) = source.shape[:2]
# matriz que descreve o tamanho ocupado pela imagem auxiliar
srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
detector = cv2.aruco.ArucoDetector(dictionary)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
##video_writer = cv2.VideoWriter('video_processado.avi', fourcc, 30, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    (imgH, imgW) = frame.shape[:2]
    corners, ids, rejected = detector.detectMarkers(frame)

    if len(corners) != 4:
        continue

    scalar = False
    ids = ids.flatten()
    refPts = []
    for i in (923, 1001, 241, 1007):
        j = np.squeeze(np.where(ids == i))
        if j.size == 0:
            scalar = True
            continue
        corner = np.squeeze(corners[j])
        refPts.append(corner)

    if scalar is True:
        continue

    # descompactando os pontos de referencia da lista
    # top left, top right, bot right, bot left
    (refPtTL, refPtTR, refPtBR, refPtBL) = refPts

    # formar matriz para correlação entre imagem de destino e marcador
    dstMat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
    dstMat = np.array(dstMat)

    # calculando homografia entre ambas as matrizes
    (H, _) = cv2.findHomography(srcMat, dstMat)
    warped = cv2.warpPerspective(source, H, (imgW, imgH))

    # criar mascara do tamanho da imagem auxiliar
    mask = np.zeros((imgH, imgW), dtype="uint8")
    cv2.fillConvexPoly(mask, dstMat.astype("int32"), (255, 255, 255), cv2.LINE_AA)

    # criando com 3 canais
    maskScaled = mask.copy() / 255.0
    maskScaled = np.dstack([maskScaled] * 3)

    # multiplicando a imagem warped com a mascara
    # multiplicando a imagem do marcador com a mascara
    # somando os resultados das multiplicações
    warpedMultiplied = cv2.multiply(warped.astype("float"), maskScaled)
    frameMultiplied = cv2.multiply(frame.astype(float), 1.0 - maskScaled)
    output = cv2.add(warpedMultiplied, frameMultiplied)
    output = output.astype("uint8")

    cv2.imshow('image', output)
    ##video_writer.write(output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
##video_writer.release()
cv2.destroyAllWindows()
