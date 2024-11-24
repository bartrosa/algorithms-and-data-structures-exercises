from collections import defaultdict
import heapq
from typing import List, Tuple, Dict, Set
import random
import time
import statistics


class Graph:
    def __init__(self):
        self.vertices = {}  # id -> (lon, lat)
        self.adj = defaultdict(list)  # vertex -> [(neighbor, cost), ...]
        self.num_vertices = 0
        self.num_edges = 0
    
    def add_vertex(self, vertex_id: int, lon: float, lat: float) -> None:
        """Add a vertex with given ID and coordinates."""
        self.vertices[vertex_id] = (lon, lat)
        self.num_vertices += 1
    
    def add_edge(self, v1: int, v2: int, cost: int) -> None:
        """Add an undirected edge between v1 and v2 with given cost."""
        self.adj[v1].append((v2, cost))
        self.adj[v2].append((v1, cost))
        self.num_edges += 1

    @classmethod
    def from_file(cls, lines: List[str]) -> 'Graph':
        """Create a graph from the input file format."""
        graph = cls()
        
        # Read first line containing n (vertices) and m (edges)
        n, m = map(int, lines[0].split())
        
        # Read vertices
        current_line = 1
        for _ in range(n):
            vertex_id, lon, lat = map(float, lines[current_line].split())
            graph.add_vertex(int(vertex_id), lon, lat)
            current_line += 1
        
        # Read edges
        for _ in range(m):
            v1, v2, cost = map(int, lines[current_line].split())
            graph.add_edge(v1, v2, cost)
            current_line += 1
        
        return graph

def dijkstra_early_stop(graph: Graph, start: int, target: int) -> Tuple[int, int]:
    """
    Implementation of Dijkstra's algorithm with early stopping.
    Returns (distance, num_edges_relaxed)
    """
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    settled = set()
    edges_relaxed = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u == target:
            return d, edges_relaxed
            
        if u in settled:
            continue
            
        settled.add(u)
        
        for v, cost in graph.adj[u]:
            edges_relaxed += 1
            if v not in settled and dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))
    
    return float('inf'), edges_relaxed

def bidirectional_dijkstra(graph: Graph, start: int, target: int) -> Tuple[int, int]:
    """
    Implementation of bidirectional Dijkstra's algorithm.
    Returns (distance, num_edges_relaxed)
    """
    # Forward search from start
    dist_forward = defaultdict(lambda: float('inf'))
    dist_forward[start] = 0
    pq_forward = [(0, start)]
    
    # Backward search from target
    dist_backward = defaultdict(lambda: float('inf'))
    dist_backward[target] = 0
    pq_backward = [(0, target)]
    
    # Keep track of settled vertices
    settled = set()
    edges_relaxed = 0
    
    # Best distance found so far
    best_dist = float('inf')
    
    while pq_forward and pq_backward:
        # Choose which direction to explore
        if not pq_forward or (pq_backward and pq_backward[0][0] < pq_forward[0][0]):
            # Explore backward
            d, u = heapq.heappop(pq_backward)
            if u in settled:
                break
            settled.add(u)
            
            for v, cost in graph.adj[u]:
                edges_relaxed += 1
                if dist_backward[u] + cost < dist_backward[v]:
                    dist_backward[v] = dist_backward[u] + cost
                    heapq.heappush(pq_backward, (dist_backward[v], v))
                best_dist = min(best_dist, dist_forward[v] + dist_backward[v])
        else:
            # Explore forward
            d, u = heapq.heappop(pq_forward)
            if u in settled:
                break
            settled.add(u)
            
            for v, cost in graph.adj[u]:
                edges_relaxed += 1
                if dist_forward[u] + cost < dist_forward[v]:
                    dist_forward[v] = dist_forward[u] + cost
                    heapq.heappush(pq_forward, (dist_forward[v], v))
                best_dist = min(best_dist, dist_forward[v] + dist_backward[v])
    
    return best_dist, edges_relaxed

def generate_test_pairs(graph: Graph, num_pairs: int, seed: int = 42) -> List[Tuple[int, int]]:
    """Generate random (s,t) pairs for testing."""
    random.seed(seed)
    vertices = list(graph.vertices.keys())
    pairs = []
    for _ in range(num_pairs):
        s = random.choice(vertices)
        t = random.choice(vertices)
        while t == s:  # Ensure s ≠ t
            t = random.choice(vertices)
        pairs.append((s, t))
    return pairs

def run_performance_test(graph: Graph, test_pairs: List[Tuple[int, int]]) -> None:
    """
    Run performance tests on both algorithms and print statistics.
    """
    # Statistics collectors
    dijkstra_times = []
    dijkstra_edges = []
    bidirectional_times = []
    bidirectional_edges = []
    
    print("\nRunning performance tests on", len(test_pairs), "pairs...")
    print("-" * 50)
    
    # Test each pair
    for i, (s, t) in enumerate(test_pairs, 1):
        # Test Dijkstra with early stopping
        start_time = time.time()
        dist1, edges1 = dijkstra_early_stop(graph, s, t)
        time1 = time.time() - start_time
        
        # Test Bidirectional Dijkstra
        start_time = time.time()
        dist2, edges2 = bidirectional_dijkstra(graph, s, t)
        time2 = time.time() - start_time
        
        # Verify results match
        if dist1 != dist2:
            print(f"Warning: Distance mismatch for pair {i}: {dist1} vs {dist2}")
        
        # Collect statistics
        dijkstra_times.append(time1)
        dijkstra_edges.append(edges1)
        bidirectional_times.append(time2)
        bidirectional_edges.append(edges2)
        
        # Print progress every 100 pairs
        if i % 100 == 0:
            print(f"Processed {i} pairs...")
    
    # Calculate and print statistics
    print("\nPerformance Statistics:")
    print("=" * 50)
    print("\nDijkstra with Early Stopping:")
    print(f"Average time: {statistics.mean(dijkstra_times):.6f} seconds")
    print(f"Average edges relaxed: {statistics.mean(dijkstra_edges):.1f}")
    print(f"Max time: {max(dijkstra_times):.6f} seconds")
    print(f"Max edges relaxed: {max(dijkstra_edges)}")
    
    print("\nBidirectional Dijkstra:")
    print(f"Average time: {statistics.mean(bidirectional_times):.6f} seconds")
    print(f"Average edges relaxed: {statistics.mean(bidirectional_edges):.1f}")
    print(f"Max time: {max(bidirectional_times):.6f} seconds")
    print(f"Max edges relaxed: {max(bidirectional_edges)}")
    
    print("\nPerformance Improvement:")
    time_improvement = (statistics.mean(dijkstra_times) - statistics.mean(bidirectional_times)) / statistics.mean(dijkstra_times) * 100
    edge_improvement = (statistics.mean(dijkstra_edges) - statistics.mean(bidirectional_edges)) / statistics.mean(dijkstra_edges) * 100
    print(f"Time reduction: {time_improvement:.1f}%")
    print(f"Edge relaxation reduction: {edge_improvement:.1f}%")

# Example usage:
if __name__ == "__main__":
    # Read the graph
    print("Reading graph file...")
    with open('algorithms-and-data-structures/dijkstra/denmark/denmark.graph', 'r') as f:
        lines = f.readlines()
    
    graph = Graph.from_file(lines)
    print(f"Graph loaded: {graph.num_vertices} vertices, {graph.num_edges} edges")
    
    # Generate test pairs
    print("\nGenerating test pairs...")
    test_pairs = generate_test_pairs(graph, 10)
    
    # Run performance tests
    run_performance_test(graph, test_pairs)
