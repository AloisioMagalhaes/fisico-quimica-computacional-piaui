# Plano computacional seguro
1. Revisar literatura primaria sobre betavoltaica, carbono-14, diamante e baterias de sal.
2. Separar fatos demonstrados, hipoteses e alegacoes sem fonte.
3. Modelar decaimento radioativo somente com parametros publicados.
4. Modelar agua, carbonatos e superficies nao radioativas com PySCF ou Psi4.
5. Comparar HF/DFT e analise de sensibilidade.
6. Publicar entrada, versao, ambiente, saida e checksum.
7. Fazer revisao humana antes de qualquer atividade experimental.

Nao incluir protocolos de preparacao, concentracao, cristalizacao ou blindagem de material radioativo.

## Experimento escolar permitido

Usar apenas materiais nao radioativos e comerciais, como grafite, carvao ativado e carbonato de calcio, para observar diferencas de composicao, Raman, massa e solubilidade sob supervisao docente. O resultado deve ser descrito como analogia de materiais, nao como producao de diamante ou bateria nuclear.

## Simulacao no GitHub Actions

O workflow `simulacao-segura.yml` executa o modelo matematico de decaimento com parametros publicados e valida o artefato CSV. Ele nao acessa, gera ou manipula isotopos, cinzas, fontes radioativas ou instrucoes experimentais.
