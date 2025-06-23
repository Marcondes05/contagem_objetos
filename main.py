import cv2
import numpy as np

# 1. Carregar a imagem
img = cv2.imread('images/chocolates.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Binarizar (teste com Otsu direto ou adaptativa)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. Remover ruídos
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
morph = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 🔁 Inverter: moedas em branco
morph_inv = cv2.bitwise_not(morph)

# 4. Detectar contornos
contours, _ = cv2.findContours(morph_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. Desenhar contornos
contagem = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 100:
        contagem += 1
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)


print(f'Objetos detectados: {contagem}')

# 6. Salvar a imagem da máscara
cv2.imwrite('images/mask.png', morph)

# 7. Exibir imagem
cv2.imshow("Morph", morph)
cv2.imshow("IMG", img)
cv2.waitKey(0)  # Espera até apertar alguma tecla
cv2.destroyAllWindows()  # Fecha todas as janelas abertas
