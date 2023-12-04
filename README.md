# Projeto Exapansão Airbnb
![New York Airbnb](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/5ee99c0a-f6f2-40b7-af47-b46fae6a857c)

Projeto de Análise e  Ciência de Dados “New York City Airbnb Open Data”  do Kaggle ( Dados Abertos do Airbnb de Nova York )

O Projeto Expansion Airbnb é um projeto do tipo Insights reais que busca analisar as melhores oportunidades de compras de imóveis para a empresa Airbnb. O conjunto de dados descreve a atividade e as métricas de listagem em NYC, NY, para 2019.
Esse projeto é uma proposta do Curso: Python para Ciências de Dados, da Comunidade DS. O conjunto de dados públicos utilizados está disponível em [Kaggle](https://www.kaggle.com/datasets?search=New+York+City+Airbnb+Open+Data).

## 1.	Questões de Negócio
A empresa Airbnb trabalha com o seguinte modelo de negócio: comprar imóveis a preços baixos e  e loca-los para hospedes. 
### 1.1.	Problemática
Esse projeto de expansão é muito importante para o Airbnb, mas também é muito arriscado. Qualquer decisão errada por parte do CEO pode levar a empresa a ter um prejuízo enorme.
Para diminuir o risco desse projeto, responderemos algumas perguntas, utilizando dados que o ajudarão a tomar melhores decisões comerciais e de marketing.
### 1.2.	Objetivo
Indicar as melhores regiões para compra de imóveis, na cidade de Nova York, Estados Unidos. 

## 2.	Premissas de negócio
Os atributos do conjunto de dados são:
| Atributos  | Descrição |
| --- | --- |
| id | Identificador  |
| host_id | Identificador  |
| name | Nome do anuncio   |
| host_name | Nome do hospede |
| neighbourhood_group | Região  |
| neighbourhood | Bairro |
| lat | Latitude |
| long | Longitude |
| room_type | Tipo de quarto  |
| price | Preço |
| minimum_nights | Mínio de noites  |
| number_of_reviews | Número de avaliações  |
| last_review | Última revisão |
| reviews_per_month | Avaliações por mês  |
| calculated_host_listings_count | Contagem calculada de listagens de anfitriões |
| availability_365 | Disponibilidade |

- Neste projeto realizarei uma análise descritiva e exploratória, a fim de compreender alguns fenômenos, além de gerar hipóteses úteis para as tomadas de decisões.
- Toda a análise seguira uma estrutura simples e direta, bem detalhada em todos os tópicos.
- Para realizar este trabalho utilizei técnicas estatísticas muito comuns em qualquer tipo de análise, simples ou complexa, como histogramas, média e desvio padrão.

**Para a limpeza dos dados:** 
- Desconsideramos a coluna 'availability_365'

## 3.	Planejamento da solução

### 3.1.	Produto final
- Entregar quatro Insights dos dados;
- Fazer recomendações de compras de imóveis;
- Painel com os gráficos.

### 3.2.	Ferramentas
**Linguagem de programação:**
- Python 3.10
- PyCharm
**Visualização de dados:**
- Mapas no Python
- Gráficos no Python
**Estatística:**
- Média
- Desvio padrão
- Histograma
**Google Collabs**
**Vscode**
- IDE ( Ambiente de Desenvolvimento Integrado )
**Git e Github**
- Hospedagem e controle de versionamento do projeto 

## 4.	Insights dos dados
Após realizar análises, notei algumas hipóteses que geraram insights interessantes:

**H1:** A variação média dos preços é média de U$ 152.72 com desvio padrão
de U$ 240.15

**H2:** Existem mais de 2.000 imóveis com o valor de aluguel até U$ 100
dólares. Ou seja, existe uma concentração de imóveis nos valores baixos de
aluguel que caracteriza a maioria como sendo imóveis mais baratos. Veja o
histograma abaixo:

![Histograma H2](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/9a7d2f3d-4e90-4bab-9c49-3331e3320305)

**H3:** Existem quase 30.000 imóveis com até 10 avaliações. Ou seja, existem
muitos imóveis com poucas avaliações. Veja o histograma abaixo:

![Histograma H3](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/76ac60f0-850f-43bf-91dc-2811c0de1a62)

**H4:** Há três regiões onde os alugueis tem uma rentabilidade maior, Brooklyn, Manhatran e Quens. Veja o gráfico abaixo:

![newplot](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/537a83e8-326f-4aed-acd5-901e2a26961f)

Para uma análise mais detalhada e precisa, fui mais afundo para sabermos onde estão localizados esses imóveis e quais tipos de imóveis são esses.

### Bronx: 
![local bronx](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/1db4f60a-8670-46ab-b9e3-82995fccc9df)

### Brooklyn:
![local brooklyn](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/49238446-0926-4ac1-a3bd-91bd2282dab7)

### Manhattan:
![local manhattan](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/ef948a51-fc7d-43c2-b15b-1f1b312c7b31)

### Queens:
![local queens](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/47120376-d970-45ce-a60c-f532576fc60e)

### Staten Island:
![local satante island](https://github.com/mariacdev/Projeto-New-York-City-Airbnb-Open-Data/assets/134116444/236e250d-ed6f-44ad-864f-435fd9bd7f8d)

### **5. Resultados**

**5.1. Resultados financeiros**

Nessa primeira etapa, na busca por grandes oportunidades de compras de imóveis, focamos em imóveis que tenham:

- Localização dos imóveis com valor do aluguel mais caro;
- Os tipos de imóveis e  o valor do aluguel (diária) mais caro de cada região;
- A variação média dos preços;
- As avaliações dos imóveis;

Satisfazendo todos esses critérios, foram selecionados 3 regiões, Bronx, Brooklyn e Manhattan. Considerando suas localidades e rentabilidade alta, esperasse um bom faturamento de suas locações.

## **6. Conclusões**

Os insights apresentados para o time de negócio podem ser grande contribuição para selecionar outros imóveis que também possam ser grandes oportunidades.

 Além de possibilitar um novo modelo de negócio para a empresa.

## **7. Próximos passos**

Como mencionado anteriormente, os insights analisados abriram portas para duas grandes possibilidades de negócio:

- Analisar as possibilidades de expandir a empresa com um novo modelo de negócio: compra de imóveis em condições ruins, para reforma-los e incorporar uma taxa de lucro maior.

## **8. Referências**

HARLFOXEM. New York City Airbnb Open Data.

[1] [New York City Airbnb Open Data (kaggle.com)](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).
 
[2] LOPES, Meigarom. Curso de Python do ZERO ao DS - Comunidade DS. [(https://alunos.comunidadeds.com/area/produto/item/1734980)].
