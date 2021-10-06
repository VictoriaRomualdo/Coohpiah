# Coohpiah - Detecção de Autoria

# Em que consiste o programa?
Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

# Traços linguísticos
Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

- Tamanho médio de palavra: Média simples do número de caracteres por palavra.
- Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
- Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
- Tamanho médio de sentença: Média simples do número de caracteres por sentença.
- Complexidade de sentença: Média simples do número de frases por sentença.
- Tamanho médio de frase: Média simples do número de caracteres por frase.

# Funcionamento do programa
A partir da assinatura conhecida de um portador de COH-PIAH, o programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que o programa deve utilizar são calculados da seguinte forma:

- Tamanho médio de palavra: é a soma dos tamanhos das palavras dividida pelo número total de palavras;
- Relação Type-Token: é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale  4/5 = 0.8; 
- Razão Hapax Legomana: é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale  3/5 = 0.6;  
- Tamanho médio de sentença: é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença);
- Complexidade de sentença: é o número total de frases divido pelo número de sentenças;
- Tamanho médio de frase: é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase);

Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos,
A e B, é dado pela fórmula:

![formula](https://user-images.githubusercontent.com/71527962/136276331-4547bfe9-8487-441d-8cef-7a8b1be7b2a9.jpg)

Onde:

 S 
  ab  é o grau de similaridade entre os textos  a e b;

 f 
  i,a é o valor de cada traço linguístico i no texto a; 

 f 
  i,b é o valor de cada traço linguístico i no texto b.

Nesse caso, o texto b não é conhecido, mas tem a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, é sabido o valor de  f(i,b) que é dado como valor de entrada do programa. 

![formula-explicada](https://user-images.githubusercontent.com/71527962/136277996-456d5e79-73e2-41d4-8cfa-a658a21ed787.jpg)


Perceba que quanto mais similares A e B forem, menor  S{ab} será. 
Para cada texto, deve ser calculado o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).
