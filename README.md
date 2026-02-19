# 🤖 ML Portfolio — Estudos de Machine Learning com Streamlit

> Portfólio interativo de projetos de Machine Learning desenvolvido com Streamlit, reunindo implementações práticas dos principais algoritmos de aprendizado de máquina para fins de estudo e demonstração.

---

## 📌 Sobre o Projeto

Este portfólio foi criado com o objetivo de consolidar o aprendizado em Machine Learning através de projetos práticos e interativos. Cada seção do app demonstra um algoritmo diferente, permitindo visualizar os dados, ajustar hiperparâmetros e analisar os resultados em tempo real diretamente no navegador.

---

## 🚀 Tecnologias Utilizadas

- **[Python 3.10+](https://www.python.org/)**
- **[Streamlit](https://streamlit.io/)** — Interface interativa
- **[Scikit-learn](https://scikit-learn.org/)** — Algoritmos de ML
- **[Pandas](https://pandas.pydata.org/)** — Manipulação de dados
- **[NumPy](https://numpy.org/)** — Computação numérica
- **[Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/)** — Visualizações
- **[Plotly](https://plotly.com/)** — Gráficos interativos

---

## 📂 Estrutura do Projeto

```
ml-portfolio/
│
├── app.py                        # Página inicial e navegação
├── requirements.txt
├── README.md
│
└── pages/
    ├── 01_regressao_linear.py
    ├── 02_regressao_logistica.py
    ├── 03_svm.py
    ├── 04_knn.py
    ├── 05_kmeans.py
    ├── 06_arvore_decisao.py
    ├── 07_floresta_aleatoria.py
    ├── 08_validacao_cruzada.py
    ├── 09_validacao_alinhada.py
    └── 10_pca.py
```

---

## 🧠 Projetos e Algoritmos

### 📈 Aprendizado Supervisionado

#### Regressão Linear
Previsão de valores contínuos com base em uma ou mais variáveis independentes. O projeto demonstra os conceitos de coeficientes, intercepto, MSE e R², com gráficos de dispersão e linha de regressão ajustada.

#### Regressão Logística
Classificação binária com base em probabilidades. Inclui visualização da curva sigmoide, matriz de confusão e métricas como acurácia, precisão, recall e F1-Score.

#### SVM — Support Vector Machine
Classificador de margem máxima com suporte a kernels linear e RBF. O projeto plota os vetores de suporte e a fronteira de decisão, permitindo ajuste interativo do parâmetro C e gamma.

#### KNN — K-Nearest Neighbors
Classificação por vizinhança. O projeto permite escolher o valor de K e visualizar como ele impacta a fronteira de decisão e a acurácia do modelo.

#### Árvores de Decisão
Modelo interpretável de classificação e regressão baseado em regras. Inclui visualização da árvore gerada, importância das features e controle de profundidade máxima.

#### Florestas Aleatórias
Ensemble de árvores de decisão para classificação e regressão. Demonstra o conceito de bagging, importância das variáveis e comparação com uma única árvore de decisão.

---

### 🔵 Aprendizado Não Supervisionado

#### K-Means
Algoritmo de clusterização por centróides. O projeto permite definir o número de clusters K e visualiza a formação dos grupos em 2D, além do método do cotovelo para escolha ótima de K.

---

### ✅ Validação de Modelos

#### Validação Cruzada (Cross-Validation)
Técnica de avaliação que divide o dataset em K folds para evitar overfitting. O projeto compara diferentes valores de K e exibe a distribuição dos scores por fold.

#### Validação Alinhada (Hold-Out / Estratificada)
Divisão tradicional treino/teste com suporte à estratificação. Demonstra como a proporção da divisão impacta as métricas do modelo e a importância de manter a distribuição das classes.

---

### 📉 Redução de Dimensionalidade

#### PCA — Principal Component Analysis
Redução de dimensionalidade com preservação de variância. O projeto visualiza os componentes principais, a variância explicada acumulada e a projeção dos dados em 2D e 3D.

---

## ▶️ Como Executar

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/ml-portfolio.git
cd ml-portfolio
```

**2. Crie um ambiente virtual e instale as dependências:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Execute o app:**
```bash
streamlit run app.py
```

**4. Acesse no navegador:**
```
http://localhost:8501
```

---

## 📦 Dependências (`requirements.txt`)

```
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
plotly
```

---

## 📊 Datasets Utilizados

Os projetos utilizam datasets clássicos de ML, disponíveis diretamente pelo Scikit-learn:

| Dataset | Uso |
|---|---|
| Boston Housing / California Housing | Regressão Linear |
| Iris / Breast Cancer | Regressão Logística, KNN, SVM |
| Titanic | Regressão Logística |
| Make Blobs / Make Moons | K-Means, SVM |
| Wine | Árvores de Decisão, Florestas Aleatórias |
| Digits / MNIST (subset) | PCA |

---

## 📖 Aprendizados e Objetivos

- Compreender a matemática e intuição por trás de cada algoritmo
- Desenvolver habilidade prática em pré-processamento, treinamento e avaliação de modelos
- Explorar a importância da validação correta para evitar data leakage e overfitting
- Ganhar experiência com visualização de dados e comunicação de resultados
- Construir uma interface interativa profissional com Streamlit

---

## Autor

Feito por Mateus Oliveira Santos

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
