# Dashboard Spotify

### Dashboard Link : [https://app.powerbi.com/groups/me/reports/54b43cfa-2bb7-40c7-9a38-7749659f650e/ReportSectiondb174d934dc20ebf6e93?experience=power-bi](https://app.powerbi.com/groups/me/reports/76ca68bc-548e-4c6f-aad1-79c11ece500e/ReportSectionf29673a5990829443c5d?experience=power-bi)

## Etapas

1° Donwload do Dataset (Kaggle)

2° Incrementar o Dataset com Python e AI 

3° Prototipação com Figma

4° ETL

5° Criação das medidas DAX

6° Código HTML para o Cover do Album

7° Código e visual DENEB para a Energia da música

8° Formatação dos visuais

### 1° Passo (Dataset)
- Dataset: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download

## Desenvolvimento

### 2° Passo (Incrementação com Python e IA)

Para tornar o dashboard mais completo e com um melhor aspecto visual, adicionei uma coluna com a URL da foto do álbum, para isso utilizei um código Python com auxílio do ChatGPT.
Foi necessário acessar a API do Spotify para desenvolvedores, criar um APP e copiar o Client ID e o Client Secret, o código está disponivel nos arquivos.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/cf5f7cb9-1e55-4eb6-99d3-4421654293e2)

 O código Python gerado pelo ChatGPT precisou de alguns ajustes e rodar para conseguir adicionar as URL’s no Dataset, antes de partir para o PowerBI.

Agora, o Dataset possui uma coluna com a URL da imagem de cada álbum, respectivamente:

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/73112dad-7c49-4f4f-98da-ec76172273c5)


### 3° Passo (Prototipação com Figma)

Utilização do Software Figma para criação do design do Dashboard.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/d3fcaee0-ef08-476e-900e-45832c1639ed)


![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/aed78c6e-64b1-458b-9355-aff1aa8e3901)


### 4° Passo (ETL)

O dataset está bem completo para se trabalhar dentro do PowerBI, porém possui uma coluna com a data de lançamento, outra coluna com o mês de lançamento e outra com o ano, portanto foi preciso somente realizar uma coluna calculada com essas 3 informações para que consigamos trabalhar com uma data formatada para quaisquer eventuais medidas de inteligência de tempo.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/94c9e0f8-3227-4bf4-9b53-b4ad97a9a64d)


### 5° Passo (Criação das medidas DAX)

Dentro do PowerBI, já podemos trabalhar com os gráficos e as medidas propostas, destaque apenas para dois visuais, sendo eles:

•	Imagem do álbum cover com uso de código HTML;

•	% De Energia da música:

### 6° Passo (Visual HTML para o Album Cover)

Obs: Foi utilizado um visual extra ao PowerBI, o HTML content, e o código está disponivel nos arquivos.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/8f04cc8d-01a2-4f23-8d47-bce17c57eb32)


### 7° Passo (Visual DNEB)



![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/9679545a-8d9f-4006-9c69-ca03ac93fc4a)


Para isso foi utilizado também um visual extra ao PowerBI, o DNEB, e o código também está disponivel nos arquivos.

### 8° Passo (Formatação dos visuais)

Por fim temos as demais medidas DAX e os visuais formatados.
Para o tema de cores foi utilizado o Adobe Palett Colors com a logo do Spotify.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/df05f1eb-d121-47d5-bbde-27017d5d62ae)
