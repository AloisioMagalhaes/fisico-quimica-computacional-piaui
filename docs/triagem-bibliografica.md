# Triagem bibliográfica

Os arquivos em `data/bibliografia/` são candidatos obtidos por consulta reprodutível ao OpenAlex. Eles não são automaticamente aprovados: cada item deve ser conferido no periódico, DOI, resumo e texto integral antes de entrar na revisão final.

## Critérios de inclusão

- Artigo de periódico revisado por pares.
- DOI ou URL acadêmica resolvível.
- Relação com pelo menos um subtema: carbono biogênico, isótopos, cinzas, HPHT, CVD, DFT, diamante, betavoltaica, caracterização ou segurança.
- Método e limitação identificáveis.

## Critérios de exclusão

- Duplicatas.
- Blog, notícia ou material promocional.
- Patente sem artigo técnico correspondente.
- DOI inexistente ou metadados não verificáveis.
- Resultado sem relação com a pergunta.

## Patentes

Patentes serão cadastradas separadamente em `data/bibliografia/patentes.csv`, com jurisdição, número, prioridade, titulares, inventores, status e link oficial. Elas documentam reivindicações e processos descritos pelo depositante, mas não contam para as 80 referências revisadas por pares.

## Fichamento obrigatório

Para cada referência aprovada, preencher pergunta, método, amostra/sistema, resultado, limitação, DOI, acesso e uso na dissertação em `docs/fichamento-modelo.md`.
