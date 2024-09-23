"""
Nathan Scott
COSC367 Lab 7
Roulette Wheel Select
"""


def roulette_wheel_select(population, fitness, r):
    """Return an individual from the population using r"""
    f_t = 0
    ft_list = []
    for i in range(len(population)):
        f_t += fitness(population[i])
        ft_list.append(f_t)
    for i in range(len(population)):
        if ft_list[i] >= r * f_t:
            return population[i]
