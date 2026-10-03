# Cálculos quânticos automatizados

Métodos de estrutura eletrônica são aproximações matemáticas para estimar energia e propriedades eletrônicas. Funcional, base e modelo devem ser registrados porque podem alterar o resultado [@he2019dft]. O PySCF fornece a implementação usada no pipeline [@pyscf].

O workflow `quantum.yml` executa H2O, C2, C4 linear, anel C6 e C4 tetraédrico com base STO-3G usando:

- Hartree–Fock;
- DFT/PBE;
- DFT/B3LYP.

Cada job salva energia total, método, base, sistema, convergência, HOMO, LUMO, gap, cargas de Mulliken e geometria como artefato JSON. Esses observáveis descrevem o modelo calculado; não constituem, sozinhos, prova de estabilidade de grafite, diamante ou bateria [@li2023c14; @liu2019diamonddetectors]. Este benchmark valida o pipeline; não representa ainda grafite, diamante, cinzas ou uma bateria.

O resumo gera `quantum-summary.csv` e `quantum-gap.png`. C4 linear e anel C6 são modelos moleculares simplificados; não representam grafite cristalino. C4 tetraédrico é uma aproximação geométrica de coordenação sp3; não representa diamante periódico. Próximos sistemas: grafite periódico, superfície de diamante e defeitos com N/O/Ca/P, após validação dos parâmetros e escolha de código periódico apropriado.
