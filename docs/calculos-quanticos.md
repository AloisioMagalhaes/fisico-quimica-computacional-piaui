# Cálculos quânticos automatizados

O workflow `quantum.yml` executa a molécula de água com base STO-3G usando:

- Hartree–Fock;
- DFT/PBE;
- DFT/B3LYP.

Cada job salva energia total, método, base, sistema, convergência, HOMO, LUMO, gap, cargas de Mulliken e geometria como artefato JSON. Este benchmark valida o pipeline; não representa ainda grafite, diamante, cinzas ou uma bateria.

Próximos sistemas: grafite periódico, superfície de diamante e defeitos com N/O/Ca/P, após validação dos parâmetros e escolha de código periódico apropriado.
