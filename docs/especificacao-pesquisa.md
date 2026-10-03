# Especificação operacional da pesquisa

## Pergunta

Sob condições computacionais documentadas, quais composições e impurezas alteram a estabilidade relativa de modelos de carbono sp2, sp3 e amorfo?

## Objeto

Modelos atomísticos não radioativos de carbono, grafite, estruturas sp3, carbonatos e impurezas de C, N, O, Ca e P.

## Objetivo geral

Avaliar, por modelagem multiescala, a viabilidade teórica de carbono biogênico como precursor parcial de materiais de carbono, sem afirmar origem individual, produção de diamante ou desempenho de bateria sem validação experimental.

## Hipóteses

- H1: N, O, Ca e P modificam energia relativa, geometria, defeitos e propriedades eletrônicas.
- H2: a estabilidade prevista depende do método, da base, do tamanho do sistema e das condições de contorno.
- H3: origem biológica, sozinha, não demonstra concentração útil de carbono-14 nem desempenho betavoltaico.

## Variáveis

Independentes: composição, impureza, concentração de defeito, método eletrônico, base, temperatura e tamanho do modelo.

Dependentes: energia total e relativa, distância interatômica, coordenação, fração sp2/sp3, gap, cargas, estabilidade temporal e incerteza.

Controladas: geometria inicial, critérios de convergência, unidades, versão do programa, hardware, sementes e parâmetros publicados.

## Métricas de aprovação

1. O cálculo termina sem erro e informa convergência.
2. As unidades e o método aparecem na saída.
3. O resultado pode ser reproduzido por outra execução limpa.
4. A sensibilidade a método, base e tamanho é registrada.
5. A interpretação separa resultado, hipótese, evidência e limitação.
6. Cada afirmação relevante aponta para literatura ou artefato.

## Critérios de não conclusão

O estudo não pode declarar viabilidade material ou energética quando faltar convergência, caracterização, comparação bibliográfica, validação experimental ou análise de segurança.

## Ficha Feynman

Para cada execução, registrar: o que foi calculado; entrada; hipótese; equação; unidade; resultado; evidência; limitação; próximo teste.

## Segurança

O repositório não contém protocolo para obter, concentrar, cristalizar, blindar ou manipular radioisótopos. Carbono-14 será tratado somente com dados publicados e modelos matemáticos.
