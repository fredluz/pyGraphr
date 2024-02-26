from collections import deque

class Algorithms:
    def __init__(self, graph):
        self.found_path = []
        self.visit_order = []
        self.graph = graph
        self.designations = ['Profundidade Primeiro', 'Largura Primeiro', 'Greedy BFS', 'A*', 'Dijkstra']
    
    def findShortestPath(self, visit_order):
        pass

    def dfs(self, start_node, end_node):
        # Verifica se o node atual já foi visitado
        if start_node not in self.visit_order:
            self.visit_order.append(start_node)
            print("current node: ", start_node)
            # Verifica se o node atual é o node final
            if start_node == end_node:
                self.found_path = list(self.visit_order)
            # Se já tivermos chegado ao node final, retornamos a ordem de visita e o caminho encontrado
            if self.found_path:
                return self.visit_order, self.found_path
            # Para cada vizinho do node atual, realizamos uma busca em profundidade
            for neighbor in self.graph.get_neighbors(start_node):
                if neighbor not in self.visit_order:
                    self.dfs(neighbor, end_node)
                    self.visit_order.remove(neighbor)
        # Retorna a ordem de visita e o caminho encontrado (redundante, mas sem isto o código não funciona)
        return self.visit_order, self.found_path
    
    def bfs(self, start_node, end_node):
        queue = deque([start_node])
        self.visit_order = []
        self.found_path = []
        # Enquanto a queue não estiver vazia, continuamos a busca
        while queue:
            current_node = queue.popleft()
            # Verifica se o node atual já foi visitado
            if current_node not in self.visit_order:
                self.visit_order.append(current_node)
                print("current node: ", current_node)
                # Verifica se o node atual é o node final
                if current_node == end_node:
                    self.found_path = list(self.visit_order)
                    break
                # Para cada vizinho do node atual, adicionamos à fila se ainda não foi visitado
                for neighbor in self.graph.get_neighbors(current_node):
                    if neighbor not in self.visit_order:
                        queue.append(neighbor)
        return self.visit_order, self.found_path
    def greedy_bfs(self, start_node, end_node):
        return [], []

    def a_star(self, start_node, end_node):
        return [], []

    def dijkstra(self, start_node, end_node):
        return [], []

    def perform_search(self, search_type, start_node, end_node):
        match search_type:
            case "Profundidade Primeiro":
                self.visit_order, self.found_path = self.dfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "Largura Primeiro":
                self.visit_order, self.found_path = self.bfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "Greedy BFS":
                self.visit_order, self.found_path = self.greedy_bfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "A*":
                self.visit_order, self.found_path = self.a_star(start_node, end_node)
                return self.visit_order, self.found_path
            case "Dijkstra":
                self.visit_order, self.found_path = self.dijkstra(start_node, end_node)
                return self.visit_order, self.found_path