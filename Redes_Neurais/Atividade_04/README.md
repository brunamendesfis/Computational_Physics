# Atividade 4

## Physics Informed Neural Networks (PINNs)

Redes Neurais Informadas por Física (PINNs) vão além de regressões e classificações tradicionais, e incorporam fundamentos de física no seu treinamento. Em geral, são projetadas para resolver problemas de equações diferenciais parciais (PDEs) e sistemas dinâmicos regidos por uma equação conhecida, mas de solução desconhecida. O treinamento de uma PINN envolve a minimização de uma função de perda que combina:

1. Dados conhecidos (se disponíveis): dados experimentais ou simulações que fornecem informações sobre o sistema.
2. Restrições físicas: resíduo das equações diferenciais que descrevem o comportamento do sistema.
3. Condições de contorno: condições iniciais e de contorno que devem ser satisfeitas pela solução.

A primeira condição é a minimização do **erro dos dados**, que já usamos nas regressões tradicionais. A segunda e a terceira são as **restrições físicas**. Estas três condições são combinadas em uma função de perda total, que é minimizada durante o treinamento da rede neural. O resultado é uma rede neural que não apenas se ajusta aos dados, mas também respeita as leis da física. Consequentemente, é capaz de extrapolar os dados.

Além disso, a PINN é capaz de descobrir os parâmetros da PDE que descrevem os dados. Por exemplo, podemos ter dados de um oscilador harmônico para o qual não sabemos a frequência e constante de amortecimento. A PINN é capaz de aprender a resolver a equação e descobrir estes parâmetros.

## Exercício 2

Ainda não decidi. As opções são:

- EDO do oscilador harmônico. Ver TCC Bianca e muitos tutoriais online.

- Evolução temporal da equação de onda 1D.

- EDP para difusão de calor 2D, ou membrana vibrante 2D.