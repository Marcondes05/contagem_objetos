# Contagem de Objetos em Imagens - Projeto Prático

Este projeto implementa um algoritmo em Python para detecção e contagem de objetos em imagens, utilizando técnicas avançadas de processamento de imagem com OpenCV. O objetivo é identificar objetos mesmo quando estão próximos ou parcialmente sobrepostos, reduzir falsos positivos, e apresentar uma visualização clara do resultado.

---

## Objetivo

Desenvolver uma solução aprimorada para contar objetos em imagens, usando como base o código inicial fornecido, com melhorias que:

- Identificam corretamente objetos mesmo em situações desafiadoras.
- Reduzem falsos positivos de ruído ou pequenos artefatos.
- Exibem visualmente os contornos dos objetos detectados e a contagem total na imagem.
- Salvam a imagem resultante com as marcações.

---

## Imagens utilizadas

- `seeds.png`
- `chocolates.jpg`

---

## Melhorias Implementadas

- **Segmentação Avançada:** Utilização da transformada de distância e algoritmo watershed para separar objetos próximos ou sobrepostos.
- **Ajuste de Binarização:** Uso de limiarização automática (Otsu) combinada com operações morfológicas (abertura e dilatação) para melhorar a máscara dos objetos.
- **Filtragem de Contornos:** Remoção de contornos pequenos e ruídos através do filtro por área mínima.
- **Visualização:** Contornos desenhados em verde e número total de objetos exibido em vermelho na imagem final.
- **Organização e Comentários:** Código estruturado e comentado para melhor compreensão e manutenção.
- **Salvamento:** Imagens processadas salvas em disco com as marcações aplicadas.

---

## Requisitos

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Instale as dependências com:

```bash
pip install opencv-python numpy
```

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/Marcondes05/contagem_objetos.git
```

2. Certifique-se de ter as imagens `seeds.png` e `chocolates.jpg` na pasta do projeto (ou ajuste os caminhos no script).

3. Execute o script:

```bash
python contagem_aprimorada.py
```

4. As imagens de saída `resultado_seeds.png` e `resultado_chocolates.jpg` serão geradas com os objetos destacados e a contagem exibida.

---

## Estrutura do código

- `contar_objetos(imagem_path, imagem_saida_path)`: Função principal que processa a imagem, segmenta os objetos, filtra contornos e gera a imagem resultado.
- Passos principais:
  - Suavização com GaussianBlur
  - Conversão para escala de cinza
  - Binarização usando Otsu (com inversão)
  - Operações morfológicas para limpeza e definição de regiões seguras
  - Transformada de distância para identificar centros dos objetos
  - Aplicação do watershed para segmentar objetos conectados
  - Contagem e filtro dos contornos encontrados
  - Desenho dos contornos e texto na imagem final
  - Salvamento do arquivo resultado

---

## Observações

- Ajuste o parâmetro `cv2.contourArea(c) > 100` para adaptar a sensibilidade da detecção conforme o tamanho dos objetos nas suas imagens.
- O método pode precisar de ajustes para funcionar melhor com imagens com iluminação ou contraste diferentes.


