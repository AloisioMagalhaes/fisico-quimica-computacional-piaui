# Cinzas, cristalização e carbono: protocolo orientador

## Decisão científica

O projeto será dividido em duas linhas que não devem ser confundidas:

1. **Linha mineralógica:** identificar e comparar fases cristalinas formadas em cinzas de biomassa.
2. **Linha carbonosa/eletroquímica:** caracterizar biochar ou carbono residual como material de eletrodo em célula não radioativa.

Não se assume que plantas contenham carbono-14 em concentração útil. O carbono-14 natural é produzido principalmente por reações de nêutrons secundários com nitrogênio atmosférico, especialmente `14N(n,p)14C`, e depois circula como `14CO2` no sistema atmosfera--biosfera [1,2]. A confirmação isotópica exige laboratório especializado.

## Pergunta orientadora

Quais fases minerais cristalinas aparecem em cinzas de biomassa sob condições térmicas controladas e em que medida a fração carbonosa residual ou derivada de biochar pode ser caracterizada como material de eletrodo em uma célula eletroquímica não radioativa?

## Hipótese

Cinzas de biomassa formarão principalmente carbonatos, silicatos, óxidos, sulfatos, cloretos e fosfatos. O carbono útil para eletrodos estará preferencialmente em carvão ou biochar, não na cinza de combustão completa. A resposta eletroquímica dependerá de composição, porosidade, área superficial e condutividade.

## Estado da literatura

| Tema | Evidência | Limitação |
|---|---|---|
| Mineralogia de cinzas | XRD e Rietveld identificam calcita, quartzo, fosfatos, sulfatos e fases amorfas [3--5]. | A composição varia com espécie, solo, temperatura e atmosfera. |
| Carbonatação | CO2 pode mineralizar-se em cinzas ricas em cálcio, com formação de calcita confirmada por XRD [3]. | Carbonato de cálcio não é carbono elementar nem diamante. |
| Cristalização | Combustão pode causar fusão, sinterização, recristalização e aglomeração mineral [5]. | Forma cristalina não prova desempenho elétrico. |
| Carbono residual | Carbono tende a permanecer em carvão/biochar quando a combustão é incompleta. | É necessário medir carbono total, estrutura e condutividade. |
| Betavoltaica | Estudos teóricos modelam diamante com carbono-14 como fonte beta e semicondutor [6,7]. | Exige radioisótopo controlado, junção semicondutora, encapsulamento e licenciamento. |

## Protocolo seguro de pesquisa

### Fase A — amostragem não radioativa

Usar somente biomassa vegetal comum, com origem, espécie, massa, umidade e condições térmicas registradas. Não coletar cinzas de origem desconhecida, resíduos hospitalares, industriais, nucleares ou de cremação.

### Fase B — separação conceitual

Manter três materiais identificados: cinza mineral, carvão/biochar e carbono comercial de referência. Não chamar toda cinza de “carbono cristalizado”.

### Fase C — caracterização

Priorizar XRD para fases cristalinas; fluorescência de raios X ou ICP para elementos; Raman para grafítico/disordem; microscopia para morfologia; TGA para frações voláteis e estabilidade; análise elementar para carbono total.

### Fase D — modelagem

Usar DFT molecular apenas para comparar fragmentos e adsorção. Para sólidos, usar modelos periódicos e testar convergência de célula, malha k, energia de corte, funcional e correções. A modelagem não substitui XRD, Raman ou medida elétrica.

### Fase E — eletroquímica não radioativa

Avaliar o carbono como eletrodo em sistema aprovado institucionalmente, comparando com grafite ou carbono ativado comercial. Registrar curva de carga/descarga, resistência interna, estabilidade, massa ativa e incerteza. A energia vem da reação eletroquímica, não da simples existência de uma cinza cristalina.

## O que não será concluído

- Cristalização de sais minerais não será chamada de cristalização de carbono.
- Carbono estável não será apresentado como bateria nuclear.
- DFT molecular não será apresentado como prova de diamante ou dispositivo.
- Nenhuma amostra será tratada como contendo carbono-14 sem análise isotópica autorizada.
- Não haverá instrução de concentração, purificação, irradiação ou manipulação de radioisótopos.

## Critério de avanço

O projeto só avança para material de eletrodo se houver: composição reprodutível, identificação estrutural, carbono mensurável, condutividade, comparação com controle e documentação de segurança. A hipótese betavoltaica permanece revisão teórica, não experimento escolar.

## Próximo estágio implementado

O repositório agora gera `data/generated/triagem_fases_cinzas.csv` e `.json` com fases de referência para orientar a leitura de difratogramas. A triagem calcula apenas descritores estequiométricos e massa molar; não identifica automaticamente uma amostra, não substitui XRD e não simula cristalização.

## Referências rastreáveis

[1] NRC. [Uses of radiation](https://www.nrc.gov/education-regulatory-research/the-student-corner/unit-2-uses-of-radiation).

[2] OSTI. [Measurements of the 14C content of carbon dioxide in air](https://www.osti.gov/pages/servlets/purl/1357349).

[3] Nam et al. [Valorisation of agricultural biomass-ash with CO2](https://www.nature.com/articles/s41598-020-70504-1). Scientific Reports, 2020.

[4] [Physicochemical and mineralogical characterization of biomass ash](https://pmc.ncbi.nlm.nih.gov/articles/PMC7286596/).

[5] [The Use of Biomass Ash as a Catalyst in the Gasification Process](https://www.mdpi.com/1996-1073/18/21/5653). Energies, 2025.

[6] [14C diamond as energy converting material in betavoltaic battery](https://pubs.aip.org/aip/adv/article/13/11/115314/2921598/14C-diamond-as-energy-converting-material-in). AIP Advances, 2023.

[7] [Optimal Selection and Experimental Verification of Wide-Bandgap Semiconductor for Betavoltaic Battery](https://pmc.ncbi.nlm.nih.gov/articles/PMC12073746/).
