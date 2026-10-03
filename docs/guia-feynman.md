# Guia Feynman do projeto

## 1. O que estamos tentando descobrir?

Queremos saber, com cálculos reproduzíveis, como a composição do carbono e de suas impurezas pode influenciar estruturas de carbono e materiais relacionados a conversão de energia.

A pergunta não é “como fabricar uma bateria radioativa em casa”. A pergunta segura é: “quais propriedades podem ser previstas por modelos computacionais e quais evidências seriam necessárias para testar essas previsões?”.

## 2. O que é um modelo?

Um modelo é uma versão simplificada da realidade. Em vez de simular uma floresta, uma cinza inteira ou uma bateria completa, começamos com poucos átomos e leis conhecidas.

Se o modelo for pequeno demais, ele pode ser rápido, mas representar pouco. Se for grande demais, pode ser fiel, mas caro. Por isso o projeto cresce em etapas.

## 3. O que o GitHub Actions está fazendo?

Ele recebe os arquivos do repositório, instala as dependências, executa os scripts e guarda os resultados. É uma esteira automática de cálculo e teste.

O benchmark atual usa H2O, base STO-3G e três métodos: HF, PBE e B3LYP. Isso é pequeno porque serve para verificar se o encanamento funciona: instalação, execução, validação e armazenamento.

Resultado rápido não significa pesquisa completa. Significa que o exemplo atual tem poucos átomos, poucos elétrons e poucas configurações.

## 4. O que significam HF e DFT?

HF estima o estado eletrônico tratando cada elétron como se ele se movesse em um campo médio criado pelos demais.

DFT trabalha principalmente com a densidade eletrônica. PBE e B3LYP são escolhas diferentes de aproximação para calcular essa densidade e a energia.

Nenhum método é “a verdade”. Cada método tem custo, hipóteses e erros. A comparação entre métodos mostra se uma conclusão é estável ou depende da aproximação escolhida.

## 5. O que são HOMO, LUMO e gap?

HOMO é o orbital ocupado de maior energia. LUMO é o orbital desocupado de menor energia. O gap é a diferença entre eles.

Uma analogia simples: imagine uma escada. O HOMO é o último degrau ocupado; o LUMO é o próximo degrau disponível. O espaço entre os dois ajuda a discutir propriedades eletrônicas, mas não determina sozinho se um material será uma boa bateria.

## 6. O que será modelado depois?

O aumento de complexidade recomendado é:

1. moléculas simples;
2. dímeros e pequenos aglomerados de carbono;
3. grafeno e estruturas sp2;
4. pequenas estruturas sp3 semelhantes ao diamante;
5. defeitos e impurezas de C, N, O, Ca e P;
6. superfícies;
7. supercélulas periódicas;
8. dinâmica molecular;
9. comparação com dados experimentais publicados.

Cada etapa deve ter entrada, versão do programa, método, parâmetros, saída, teste e interpretação.

## 7. Por que a simulação não prova uma bateria?

Uma bateria envolve material, eletrodos, contatos, transporte de carga, perdas, estabilidade, encapsulamento e medição. Um cálculo eletrônico fornece apenas parte das propriedades.

Para uma bateria betavoltaica também seriam necessários dados confiáveis sobre atividade, espectro, absorção, geração de pares elétron-lacuna, corrente, potência e segurança radiológica. O repositório não produz nem concentra radioisótopos.

## 8. Como estudar cada resultado?

Para cada artefato, responda:

- O que foi calculado?
- Qual hipótese foi usada?
- Quais dados entraram?
- Qual unidade aparece?
- O resultado convergiu?
- O que ele permite afirmar?
- O que ele não permite afirmar?
- Como outra pessoa reproduziria o cálculo?

Se não for possível explicar o resultado sem copiar a documentação, o estudo ainda não foi compreendido.

## 9. Ficha Feynman de cada cálculo

### Nome

Escreva o nome do sistema e do método em uma frase.

### Explicação simples

Explique o cálculo para uma pessoa que conhece química básica, sem usar siglas sem definição.

### Equação ou ideia central

Registre a grandeza calculada, a unidade e a relação física usada.

### Evidência

Indique o arquivo de entrada, o workflow, o artefato e a referência acadêmica.

### Limitação

Registre o tamanho do modelo, a aproximação, a ausência de validação experimental e qualquer parâmetro sensível.

### Correção

Liste o que precisa ser estudado novamente quando o resultado parecer estranho.

## 10. Regra de interpretação

Um resultado computacional deve ser apresentado como:

“Sob as hipóteses A, B e C, o modelo calculou D. Isso sugere E, mas não demonstra F porque faltam G e H.”

Essa frase impede que uma previsão seja confundida com uma demonstração experimental.

## 11. Como saber se o projeto avançou?

O projeto avança quando uma etapa pequena é reproduzida, explicada, testada e comparada com literatura. Aumentar o tamanho do cálculo sem entender a etapa anterior não é avanço científico.

## 12. Limite de segurança

Cinzas desconhecidas, materiais radioativos, carbono-14 concentrado e processos de cristalização radioativa ficam fora do experimento escolar. O trabalho prático deve usar materiais não radioativos e o trabalho radioativo deve permanecer na literatura, nos parâmetros publicados e em modelos matemáticos.
