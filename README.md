# Simulação da Geodésica de Fótons na Métrica de Schwarzschild
                                
## Modelo Físico

Na Relatividade Geral de Einstein, as equações de campo descrevem como a geometria do espaço-tempo é curvada pela presença de massa e energia. Neste contexto, a única solução esfericamente simétrica para o vácuo ao redor de um corpo estático é a **Métrica de Schwarzschild**, cuja unicidade é garantida pelo Teorema de Birkhoff.

A geometria do problema é descrita pelo seguinte elemento de linha:

$$ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

###  A Simulação

Nesta simulação, calculamos as trajetórias de fótons (luz) ao passarem nas proximidades de um buraco negro. Como mostrado na Figura 1, observamos fenômenos como a deflexão da luz e a captura orbital.

<p align="center">
  <img src="./imagens/Geodesica 5 fótons.png" width="600" title="Simulação das Geodésicas">
  <br>
  <em>Figura 1: Trajetórias de fótons (coloridos) sendo defletidos ou capturados pelo buraco negro.</em>
</p>

Para realizar essa simulação, não podemos utilizar a gravitação Newtoniana clássica, visto que fótons não possuem massa de repouso ($m=0$). Em vez disso, utilizamos o formalismo do **Potencial Efetivo** ($V_{eff}$) derivado da métrica de Schwarzschild:

$$V_{eff}(r) = \frac{L^2}{r^2} \left(1 - \frac{r_s}{r}\right)$$

A partir desse potencial, obtemos a equação de movimento radial. O termo de correção relativística gera uma "força atrativa" extra (proporcional a $r^{-5}$), permitindo a existência de órbitas instáveis e a captura da luz:

$$\vec{a}_{eff} \propto - \frac{3GM L^2}{r^5} \vec{r}$$
