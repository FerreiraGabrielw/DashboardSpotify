# Dashboard Spotify

### Dashboard Link : [https://app.powerbi.com/groups/me/reports/54b43cfa-2bb7-40c7-9a38-7749659f650e/ReportSectiondb174d934dc20ebf6e93?experience=power-bi](https://app.powerbi.com/groups/me/reports/76ca68bc-548e-4c6f-aad1-79c11ece500e/ReportSectionf29673a5990829443c5d?experience=power-bi)

- Dataset: Dataset
https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download

## Desenvolvimento

Para tornar o dashboard mais completo e com um melhor aspecto visual, adicionei uma coluna com a URL da foto do álbum, para isso utilizei um código Python com auxílio do ChatGPT.
Foi necessário acessar a API do Spotify para desenvolvedores, criar um APP e copiar o Client ID e o Client Secret.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/cf5f7cb9-1e55-4eb6-99d3-4421654293e2)

 O código Python gerado pelo ChatGPT precisou de alguns ajustes e rodar para conseguir adicionar as URL’s no Dataset, antes de partir para o PowerBI.

Agora, o Dataset possui uma coluna com a URL da imagem de cada álbum, respectivamente:

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/73112dad-7c49-4f4f-98da-ec76172273c5)


Passo 2: Prototipação do Dashboard com Figma

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/d3fcaee0-ef08-476e-900e-45832c1639ed)


![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/aed78c6e-64b1-458b-9355-aff1aa8e3901)


3 Passo:

O dataset está bem completo para se trabalhar dentro do PowerBI, porém possui uma coluna com a data de lançamento, outra coluna com o mês de lançamento e outra com o ano, portanto foi preciso somente realizar uma coluna calculada com essas 3 informações para que consigamos trabalhar com uma data formatada para quaisquer eventuais medidas de inteligência de tempo.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/94c9e0f8-3227-4bf4-9b53-b4ad97a9a64d)


# Power BI
Dentro do PowerBI, já podemos trabalhar com os gráficos e as medidas propostas, destaque apenas para dois gráficos, sendo eles:

•	Imagem do álbum cover com uso de código HTML

Obs: Foi utilizado um visual extra ao PowerBI, o HTML content.

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/a822d5f0-c97e-4181-b5b0-07d3036f47f4)


•	% De Energia da música:

![image](https://github.com/FerreiraGabrielw/DashboardSpotify/assets/165827836/98e539a9-4917-43e3-9f88-aec1f4f03c90)


Para isso foi utilizado também um visual extra ao PowerBI, o DNEB.


Por fim temos as demais medidas DAX e os visuais formatados, para o tema de cores foi utilizado o Adobe Palett Colors com a logo do Spotify.
