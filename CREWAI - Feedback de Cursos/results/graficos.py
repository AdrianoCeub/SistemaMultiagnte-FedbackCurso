
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
import random

# Dados dos feedbacks (positivos e negativos)
feedbacks_positivos = {
    "Excelência do conteúdo": 3,
    "Organização e clareza": 3,
    "Relevância e aplicabilidade": 2,
    "Eficácia da metodologia": 2,
    "Benefícios da interação": 1,
    "Domínio e clareza do professor": 2,
    "Qualidade do material didático": 2,
    "Estrutura do curso": 2,
    "Organização e tempo das aulas": 1,
    "Equilíbrio entre teoria e prática": 1,
    "Eficácia e clareza das explicações": 1,
    "Enriquecimento pessoal e profissional": 1,
    "Dinâmica das aulas": 1,
    "Superação das expectativas": 1,
    "Planejamento e foco do conteúdo": 1,
    "Recursos e materiais didáticos": 1
}

feedbacks_negativos = {
    "Falta de interação": 1,
    "Problemas técnicos": 1,
    "Comunicação do professor": 1,
    "Falta de materiais complementares": 1,
    "Condições físicas": 1,
    "Falta de clareza": 1,
    "Conteúdo inadequado": 1,
    "Superficialidade": 1,
    "Duração insuficiente": 1,
    "Falta de clareza em exemplos": 1
}


# Contagem de feedbacks positivos e negativos
total_positivos = sum(feedbacks_positivos.values())
total_negativos = sum(feedbacks_negativos.values())

# Gráfico de pizza
labels = 'Positivos', 'Negativos'
sizes = [total_positivos, total_negativos]
colors = ['green', 'red']
explode = (0.1, 0)  # explode 1st slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Porcentagem de Feedbacks Positivos e Negativos')
plt.savefig('grafico_pizza.png')


# Gráfico de barras
labels = ['Positivos', 'Negativos']
values = [total_positivos, total_negativos]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['green', 'red'])
plt.title('Número de Feedbacks Positivos e Negativos')
plt.ylabel('Número de Feedbacks')
plt.savefig('grafico_barras.png')


# Nuvem de palavras (positivos)
stopwords = set(STOPWORDS)
stopwords.update(["curso", "professor", "aulas", "conteúdo", "material", "didático", "bem", "muito", "o", "a", "e", "da", "dos", "das", "de", "em", "um", "uma", "para"])

text_positivos = " ".join([chave for chave, valor in feedbacks_positivos.items() for i in range(valor)])
wordcloud_positivos = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(text_positivos)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_positivos, interpolation='bilinear')
plt.axis("off")
plt.title('Nuvem de Palavras - Feedbacks Positivos')
plt.savefig('nuvem_palavras_positivos.png')



# Nuvem de palavras (negativos)
text_negativos = " ".join([chave for chave, valor in feedbacks_negativos.items() for i in range(valor)])
wordcloud_negativos = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(text_negativos)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_negativos, interpolation='bilinear')
plt.axis("off")
plt.title('Nuvem de Palavras - Feedbacks Negativos')
plt.savefig('nuvem_palavras_negativos.png')

plt.show()

