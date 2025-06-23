import cv2
import numpy as np

def contar_objetos(imagem_path, imagem_saida_path):
    # Lê imagem original
    imagem = cv2.imread(imagem_path)
    if imagem is None:
        print(f"❌ Erro: não foi possível carregar a imagem '{imagem_path}'")
        return

    # Suaviza ruído
    imagem_blur = cv2.GaussianBlur(imagem, (5, 5), 0)

    # Converte para tons de cinza
    imagem_cinza = cv2.cvtColor(imagem_blur, cv2.COLOR_BGR2GRAY)

    # Binarização com Otsu (inverso porque objetos são mais escuros)
    _, binaria = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Remove pequenos ruídos
    kernel = np.ones((3, 3), np.uint8)
    abertura = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel, iterations=2)

    # Região segura de fundo
    fundo_certo = cv2.dilate(abertura, kernel, iterations=3)

    # Região segura de frente (objetos)
    dist_transform = cv2.distanceTransform(abertura, cv2.DIST_L2, 5)
    _, frente_certa = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

    # Região desconhecida
    frente_certa = np.uint8(frente_certa)
    desconhecido = cv2.subtract(fundo_certo, frente_certa)

    # Marcadores
    _, marcadores = cv2.connectedComponents(frente_certa)
    marcadores = marcadores + 1
    marcadores[desconhecido == 255] = 0

    # Aplica watershed
    marcadores = cv2.watershed(imagem, marcadores)

    # Detecção de contornos por marcador
    contornos = []
    for label in np.unique(marcadores):
        if label <= 1:
            continue
        mascara = np.zeros(imagem_cinza.shape, dtype="uint8")
        mascara[marcadores == label] = 255
        cnts, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos.extend(cnts)

    # Filtra contornos pequenos (ajuste se necessário)
    contornos_filtrados = [c for c in contornos if cv2.contourArea(c) > 100]

    # Desenha contornos
    imagem_resultado = imagem.copy()
    for cnt in contornos_filtrados:
        cv2.drawContours(imagem_resultado, [cnt], -1, (0, 255, 0), 2)

    # Escreve total de objetos
    total = len(contornos_filtrados)
    cv2.putText(imagem_resultado, f"Total de objetos: {total}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Salva imagem
    cv2.imwrite(imagem_saida_path, imagem_resultado)
    print(f"✅ Imagem processada e salva como '{imagem_saida_path}' (Total de objetos: {total})")

# Exemplo de uso
if __name__ == "__main__":
    contar_objetos('seeds.png', 'resultado_seeds.png')
    contar_objetos('chocolates.jpg', 'resultado_chocolates.jpg')
