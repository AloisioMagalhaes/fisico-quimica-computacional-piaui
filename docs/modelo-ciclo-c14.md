# Primeiro modelo do ciclo do carbono-14

Este marco implementa um modelo didatico e normalizado de decaimento e incorporacao biologica. `prod` e `turn` sao parametros demonstrativos, nao estimativas ambientais. Nenhuma conclusao quantitativa sobre plantas, cinzas ou baterias deve ser extraida antes da substituicao por dados publicados e validacao independente.

O modelo usa:

\[
N(t)=N_0e^{-\lambda t},\qquad \lambda=\frac{\ln 2}{5730\;anos}
\]

O CSV gerado registra o estoque normalizado, uma incorporacao biologica simplificada e a fracao remanescente. O teste verifica a meia-vida, a existencia do artefato e a reproducibilidade basica.

Proxima etapa: substituir os parametros demonstrativos por series publicadas de fluxo atmosferico, intercambio biosfera-atmosfera e razao isotopica, mantendo analise de sensibilidade e incerteza.
