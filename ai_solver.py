# ai_solver.py
class AISolver:
    def __init__(self):
        # Contador de demostraciones por nivel
        self.demo_counter = {3: 0, 6: 0, 8: 0}
        # Diccionario para almacenar las rutas por nivel
        self.routes = {3: [], 6: [], 8: []}
        # ✅ Llamamos al método que genera todas las rutas
        self._generate_all_routes()

    def _solve_optimal(self, n, src, dest, aux):
        """Solución óptima clásica (mínimo de movimientos: 2^n - 1)"""
        if n == 1:
            return [(src, dest)]
        return (
            self._solve_optimal(n-1, src, aux, dest) +
            [(src, dest)] +
            self._solve_optimal(n-1, aux, dest, src)
        )

    def _solve_alternative_1(self, n, src, dest, aux):
        """Ruta alternativa: más pasos, pero válida"""
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
        """Ruta más larga: simula ineficiencia controlada"""
        if n == 1:
            return [(src, dest)]
        if n == 2:
            return [(src, aux), (src, dest), (aux, dest)]
        return (
            self._solve_optimal(n-1, src, aux, dest) +
            [(src, dest)] +
            self._solve_alternative_2(n-1, aux, src, dest)
        )

    def _generate_routes(self, n):
        """Genera 3 rutas diferentes para el nivel n"""
        try:
            optimal = self._solve_optimal(n, 0, 2, 1)          # Ruta óptima
            alt1 = self._solve_alternative_1(n, 0, 2, 1)       # Alternativa 1
            alt2 = self._solve_alternative_2(n, 0, 2, 1)       # Alternativa 2
            return [optimal, alt1, alt2]
        except RecursionError:
            # Por si hay problemas con recursión en n=8
            return [self._solve_optimal(n, 0, 2, 1)] * 3

    def _generate_all_routes(self):
        """Genera y almacena todas las rutas para niveles 3, 6 y 8"""
        for n in [3, 6, 8]:
            self.routes[n] = self._generate_routes(n)

    def get_next_route(self, num_discs):
        """
        Devuelve la siguiente ruta para el nivel dado.
        Alterna entre óptima → alternativa1 → alternativa2 → reinicia.
        También devuelve el número de demostración actual.
        """
        route_list = self.routes[num_discs]
        idx = self.demo_counter[num_discs] % len(route_list)
        self.demo_counter[num_discs] += 1
        return route_list[idx], idx + 1  # (ruta, número de demostración)