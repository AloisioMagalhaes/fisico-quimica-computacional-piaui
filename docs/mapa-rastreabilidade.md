# Mapa de rastreabilidade documental

Este mapa liga afirmações recorrentes dos documentos a fontes e ao registro de fichamento. A citação deve aparecer no texto próximo da afirmação; o mapa evita que uma fonte seja usada sem informar método, resultado e limitação.

| Documento e afirmação | Fontes principais | Método da fonte | Resultado usado | Limitação a declarar |
|---|---|---|---|---|
| `docs/calculos-quanticos.md`: HF/DFT e observáveis eletrônicos | @he2019dft; @pyscf | revisão de DFT e documentação de implementação | energia e propriedades eletrônicas são calculáveis por aproximações | dependência de funcional, base e convergência |
| `docs/calculos-quanticos.md`: diamante e defeitos | @li2023c14; @liu2019diamonddetectors | primeiros princípios e caracterização de dispositivo | defeitos influenciam propriedades do diamante | modelo não substitui fabricação e medição |
| `docs/matriz-oportunidades.md`: HPHT/CVD | @ashfold2017cvd; @hpht2022review; @cvd2023review | revisão de crescimento e processamento | rotas e variáveis de síntese diferem | condições industriais não são reproduzidas no GitHub Actions |
| `docs/modelo-ciclo-c14.md`: decaimento e atividade | @li2023c14; @tavares2023viability | modelagem físico-matemática e análise de viabilidade | atividade depende de quantidade, meia-vida e composição | parâmetro publicado não prova atividade de uma amostra desconhecida |
| `docs/triagem-bibliografica.md`: critérios de seleção | `data/bibliografia/triagem-80.csv` | metadados Crossref e conferência humana planejada | DOI e URL tornam a fonte rastreável | metadado validado não equivale a leitura crítica |
| `docs/protocolo-qualidade-escrita.md`: integridade e recuperação | @cope2011plagiarism; @mcdermott2021retrieval | orientação de integridade e revisão experimental | paráfrase autoral e recuperação favorecem aprendizagem | não eliminam erro, plágio ou necessidade de revisão |
| `docs/guia-feynman.md`: explicação em camadas | @mcdermott2021retrieval; @feynmanbot2025 | revisão de aprendizagem e estudo exploratório | explicar e recuperar conceitos torna lacunas visíveis | técnica pedagógica não valida resultados científicos |
| `docs/especificacao-pesquisa.md`: hipóteses e métricas | @he2019dft; @li2023c14 | DFT e estudo de primeiros princípios | impurezas e parâmetros podem ser variáveis do modelo | hipóteses permanecem abertas até teste e comparação |

## Regra de revisão

Antes de fechar uma seção, procurar cada afirmação factual, número, unidade, definição técnica e relação causal. Para cada item, preencher método, resultado, limitação e uso. Quando não houver fonte adequada, reescrever como hipótese, inferência ou limitação.
