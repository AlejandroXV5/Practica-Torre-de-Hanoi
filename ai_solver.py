import random

class AISolver:
    def get_next_route(self, num_discs):
        """Genera el camino óptimo para resolver el juego"""
        route = []
        self.solve_hanoi(num_discs, 0, 2, 1, route)
        demo_num = random.randint(1, 100)  # Simulación de múltiples demos
        return route, demo_num

    def solve_hanoi(self, n, source, target, auxiliary, route):
        """Algoritmo recursivo para resolver Torres de Hanoi"""
        if n == 1:
            route.append((source, target))
            return
        self.solve_hanoi(n - 1, source, auxiliary, target, route)
        route.append((source, target))
        self.solve_hanoi(n - 1, auxiliary, target, source, route)