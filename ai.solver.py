# ai_solver.py
from itertools import permutations

class AISolver:
    def _init_(self):
        # Contador de demostraciones por nivel
        self.demo_counter = {3: 0, 6: 0, 8: 0}
        # Almacena rutas por nivel: [ruta_optima, ruta_alternativa1, ...]
        self.routes = {3: [], 6: [], 8: []}
        self._generate_all_routes()

    def _solve_optimal(self, n, src, dest, aux):
        if n == 1:
            return [(src, dest)]
        return (
            self._solve_optimal(n-1, src, aux, dest) +
            [(src, dest)] +
            self._solve_optimal(n-1, aux, dest, src)
        )

    def _solve_alternative_1(self, n, src, dest, aux):
        # Usa un orden no óptimo: src -> dest -> aux como paso intermedio
        if n == 1:
            return [(src, aux), (aux, dest)]
        return (
            self._solve_alternative_1(n-1, src, dest, aux) +
            [(src, aux)] +
            self._solve_optimal(n-1, dest, src, aux) +
            [(aux, dest)] +
            self._solve_alternative_1(n-1, src, dest, aux)
        )

    def _solve_alternative_2(self, n, src, dest, aux):
        # Camino más largo: fuerza movimientos extra
        if n <= 2:
            return [(src, aux), (src, dest), (aux, dest)]
        return (
            self._solve_optimal(n-2, src, dest, aux) +
            [(src, aux), (src, dest), (aux, dest)] +
            self._solve_optimal(n-2, dest, src, aux) +
            [(dest, aux)] +
            self._solve_optimal(n-1, src, dest, aux)
        )

    def _generate_routes(self, n):
        optimal = self._solve_optimal(n, 0, 2, 1)
        alt1 = self._solve_alternative_1(n, 0, 2, 1)
        alt2 = self._solve_alternative_2(n, 0, 2, 1)
        return [optimal, alt1, alt2]

    def _generate_all_routes(self):
        for n in [3, 6, 8]:
            self.routes[n] = self._generate_routes(n)

    def get_next_route(self, num_discs):
        route_list = self.routes[num_discs]
        idx = self.demo_counter[num_discs] % len(route_list)
        self.demo_counter[num_discs] += 1
        return route_list[idx], idx + 1  # (ruta, número de demostración)