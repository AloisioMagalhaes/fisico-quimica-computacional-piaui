# Protocolo de qualidade, escrita e aprendizagem

## 1. Escopo

Este protocolo controla a qualidade formal, a integridade acadêmica, a rastreabilidade das fontes e a compreensão do estudo sobre modelagem de materiais diamantados. O objetivo é escrever de forma autoral e verificável, nunca manipular detectores de similaridade.

## 2. Normas ABNT de referência

| Norma | Aplicação | Controle |
|---|---|---|
| NBR 6022:2018 | Estrutura de artigo científico | título, autoria, resumo, palavras-chave, seções, referências |
| NBR 10520:2023 | Citações | citação direta, indireta, autoria, página e localização |
| NBR 6023:2025 | Referências | dados completos, DOI, URL e data de acesso |
| NBR 14724:2024 | Trabalhos acadêmicos | elementos pré-textuais, textuais, pós-textuais, margens e paginação |
| NBR 15287:2025 | Projeto de pesquisa | problema, hipótese, objetivos, justificativa e metodologia |

Confirmar sempre o manual da instituição, pois ele pode estabelecer modelo próprio. As normas oficiais devem ser consultadas no catálogo da ABNT; guias universitários são auxiliares, não substitutos.

## 3. Portão de qualidade por seção

| Seção | Pergunta de aprovação |
|---|---|
| Introdução | O problema, contexto, lacuna e contribuição estão explícitos? |
| Objetivos | O objetivo geral é único e os específicos são mensuráveis? |
| Revisão | Cada afirmação relevante tem fonte adequada e limite declarado? |
| Método | Outra pessoa consegue repetir o cálculo com os dados fornecidos? |
| Resultados | Há unidades, incerteza, comparação e separação entre dado e interpretação? |
| Discussão | A conclusão não excede a evidência? |
| Conclusão | A pergunta foi respondida e as limitações foram registradas? |
| Referências | Toda citação aparece na bibliografia e toda referência é citada? |

## 4. Escrita autoral e integridade

1. Ler a fonte e registrar a ideia, método, resultado e limitação no fichamento.
2. Fechar a fonte antes de escrever a primeira versão da paráfrase.
3. Escrever a explicação com estrutura própria e manter a interpretação separada do resultado da fonte.
4. Reabrir a fonte e conferir fidelidade, números, unidades e escopo.
5. Inserir citação indireta imediatamente após a afirmação.
6. Usar aspas e página para texto literal; evitar citações literais longas.
7. Não traduzir ou trocar sinônimos mantendo a estrutura original.
8. Registrar fonte, versão, data, DOI, URL, arquivo de dados e ferramenta de IA usada.
9. Revisar similaridade como diagnóstico, nunca como meta numérica.
10. Corrigir citações ausentes mesmo quando o texto foi escrito com auxílio de IA.

## 5. Feynman aplicado ao estudo

A redação de cada parágrafo seguirá também o método ABCD documentado em [metodo-abcd.md](metodo-abcd.md): Afirmação, Base, Comentário crítico e Desdobramento. A estrutura é uma adaptação transparente de guias universitários de argumento baseado em ideia principal, evidência, análise e ligação [@ttu_meal; @brandeis_argument].

Para cada conceito, criar um arquivo ou seção com:

- conceito em uma frase simples;
- explicação para uma pessoa iniciante;
- equação ou mecanismo essencial;
- exemplo numérico ou material;
- ponto em que a explicação falha;
- fonte que corrige a falha;
- pergunta de recuperação sem consultar notas;
- revisão posterior em 1, 3, 7 e 14 dias.

Exemplo: explicar por que carbono-14 biogênico não equivale a uma fonte radioisotópica concentrada. Depois, escrever a equação de decaimento, estimar a atividade e comparar com o limite de detecção. A resposta deve distinguir fato, hipótese e inferência.

A técnica Feynman será combinada com prática de recuperação: tentar explicar sem consultar o texto, receber correção e repetir em intervalo posterior. A prática de recuperação possui suporte experimental e revisão na literatura de psicologia da aprendizagem.

## 6. Registro mínimo por fonte

```text
chave_bibtex:
doi:
pergunta_respondida:
metodo:
resultado:
limitação:
trecho_literal_e_pagina:
parafrase_autoral:
secao_do_artigo:
data_de_acesso:
```

## 7. Checklist antes de publicar

- [ ] Norma institucional conferida.
- [ ] Problema e objetivo são coerentes.
- [ ] Hipótese é falsificável.
- [ ] Todas as afirmações externas têm fonte.
- [ ] Todas as citações têm registro BibTeX.
- [ ] Valores numéricos têm unidade e incerteza.
- [ ] Resultados computacionais têm ambiente e parâmetros.
- [ ] Não há promessa de segurança ou viabilidade sem validação.
- [ ] A explicação Feynman foi registrada para cada conceito central.
- [ ] Revisão humana concluída.

## Fontes metodológicas

- ABNT NBR 14724:2024, versão com Errata 1 de 2025: https://engenhariaedesenvolvimentosustentavel.ufes.br/sites/engenhariaedesenvolvimentosustentavel.ufes.br/files/field/anexo/abnt_nbr_14724.pdf
- Guia USP para NBR 6023 e NBR 10520: https://sddarquivos.webhostusp.sti.usp.br/arquivos/Guia_Referencias_ABNT6023_FOB-USP.html
- COPE, integridade e plágio: https://publicationethics.org/files/COPE_plagiarism_discussion_%20doc_26%20Apr%2011.pdf
- McDermott, 2021, prática de recuperação: https://doi.org/10.1146/annurev-psych-010419-051019
- Feynman Bot, estratégia de aprendizagem ativa: https://arxiv.org/abs/2506.09055
