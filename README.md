# Fisico-Quimica Computacional no Piaui

Projeto educacional para modelagem matematica, simulacao de materiais e estudo teorico de interacoes fisico-quimicas.

Este repositorio nao autoriza obter, concentrar, cristalizar ou manipular material radioativo. A hipotese sobre carbono-14 e bateria diamantada sera tratada apenas por literatura verificavel e simulacao numerica.

Gitflow: `main` e releases estaveis; `develop` integra trabalho; `feature/*`, `research/*`, `docs/*` e `release/*` sao temporarias. Commits seguem Conventional Commits e releases seguem SemVer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\modelo.py
python scripts\pyscf_exemplo.py
```

ABNT: NBR 6022:2018, NBR 14724, NBR 10520:2023 e NBR 6023:2018, confirmando a edicao exigida pela instituicao. Fontes computacionais: https://pyscf.org/ e https://psi4.github.io/psi4docs/master/. Fonte de contexto: https://www.ukaea.org/news/diamonds-are-forever-worlds-first-carbon-14-diamond-battery-produced/ . Sci-Hub nao sera usado; utilizar DOI, repositorios institucionais, PubMed Central, arXiv ou acesso aberto legal.

Materiais de pesquisa: [matriz de oportunidades](docs/matriz-oportunidades.md), [modelo de fichamento](docs/fichamento-modelo.md) e [evidencias bibliograficas](docs/evidencias.md).

Protocolo de qualidade: [ABNT, integridade, escrita autoral e Feynman](docs/protocolo-qualidade-escrita.md).

Explicação progressiva dos cálculos, limites e resultados: [Guia Feynman](docs/guia-feynman.md).

Escrita rastreável por afirmação, base, comentário e desdobramento: [Método ABCD](docs/metodo-abcd.md). O vínculo entre afirmações, fontes e limitações está em [Mapa de rastreabilidade](docs/mapa-rastreabilidade.md).

Plano de formação e orientação científica: [Guia de orientação da pesquisa](docs/guia-orientacao-pesquisa.md).

O guia incorpora transparência, reprodutibilidade, integridade e publicação no Brasil, com base no [PRISMA 2020](https://www.prisma-statement.org/prisma-2020), na [EQUATOR Network](https://www.equator-network.org/about-us/what-is-a-reporting-guideline/), no [CNPq](https://www.gov.br/cnpq/pt-br/composicao/comissao-de-integridade/diretrizes) e na [CAPES](https://www.gov.br/capes/pt-br/acesso-a-informacao/perguntas-frequentes/avaliacao-da-pos-graduacao).
