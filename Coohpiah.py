import re

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia = avalia_textos(textos, ass_cp)
    print("O autor do texto", avalia, "está infectado com COH-PIAH")

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    i = 0
    soma_f = 0

    while i <= 5:
        soma_f = soma_f + (abs(as_a[i] - as_b[i]))
        i = i + 1

    grau_sim = abs(soma_f) / 6

    return grau_sim


def calcula_assinatura(texto):
    lista_palavras = []
    lista_frases = []
    lista_sent = separa_sentencas(texto)
    for sent in lista_sent:
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)
    for fr in lista_frases:
        novas_palavras = separa_palavras(fr)
        lista_palavras.extend(novas_palavras)

    total_palav = len(lista_palavras)
    i = 0
    soma = 0
    while i < total_palav:
        palavra = len(lista_palavras[i])
        i = i + 1
        soma = soma + palavra

    wal_b = soma / len(lista_palavras)  # tamanho medio palavras (corrigido)
    n_dif = n_palavras_diferentes(lista_palavras)
    n_unic = n_palavras_unicas(lista_palavras)
    ttr_b = n_dif / len(lista_palavras)  # Type-Token (corrigido)
    hlr_b = n_unic / len(lista_palavras)  # hapax-lego (corrigido)

    total_sent = len(lista_sent)
    i = 0
    caract = 0
    while i < total_sent:
        palavra = len(lista_sent[i])
        i = i + 1
        caract = caract + palavra

    total_fr = len(lista_frases)
    i = 0
    numero = 0
    while i < total_fr:
        palavra = len(lista_frases[i])
        i = i + 1
        numero = numero + palavra

    sal_b = caract / len(lista_sent)  # numero caracteres em todas as sentenças dividido pelo numero de sentenças
    sac_b = len(lista_frases) / len(lista_sent)  # numero total de frases / numero total sentenças
    pal_b = numero / len(lista_frases)  # media simples numero caracteres por frase

    ass_b = [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]

    return ass_b


def avalia_textos(textos, ass_cp):
    lista_sab = []
    for cadatexto in textos:
        as_texto = calcula_assinatura(cadatexto)
        comparar = compara_assinatura(ass_cp, as_texto)
        lista_sab.append(comparar)

    posicao_menor = []

    for n, valor in enumerate(lista_sab):
        if valor == min(lista_sab):
            posicao_menor.append(n)
    return n
main()
