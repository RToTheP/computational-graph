import os
import unittest

from graph import evaluate_graph, evaluate_node, find_head_node, write_dot_file

class TestGraph(unittest.TestCase):
    def test_write_dot_file(self):
        path = "./test_output/test.dot"
        if os.path.exists(path):
            os.remove(path)

        edges = [(1,2), (3,2), (4,5), (6, 5), (2, 7), (5, 7)]
        nodes = {
            1 : 2,
            2 : "*",
            3 : "x",
            4 : 3,
            5 : "*",
            6 : "y",
            7 : "-"
        }

        write_dot_file(path, edges, nodes)
        result = os.path.exists(path)
        self.assertTrue(result)

    def test_evaluate_graph_2x_minus_3y(self):
        expected_result = -2
        edges = [(1,2), (3,2), (4,5), (6, 5), (2, 7), (5, 7)]
        nodes = {
            1 : 2,
            2 : "*",
            3 : "x",
            4 : 3,
            5 : "*",
            6 : "y",
            7 : "-"
        }
        inputs = {"x": 2, "y" : 2}
        result = evaluate_graph(edges, nodes, inputs)
        self.assertEqual(expected_result, result)

    def test_find_head_node_with_edges(self):
        edges = [(1,2), (3,2), (4,5), (6, 5), (2, 7), (5, 7)]
        nodes = {
            1 : 2,
            2 : "*",
            3 : "x",
            4 : 3,
            5 : "*",
            6 : "y",
            7 : "-"
        }
        expected = 7
        actual = find_head_node(edges, nodes)
        self.assertEqual(expected, actual)

    def test_find_head_node_single_node(self):
        edges = []
        nodes = {
            1 : 2
        }
        expected = 1
        actual = find_head_node(edges, nodes)
        self.assertEqual(expected, actual)

    def test_evaluate_graph_single_constant_node(self):
        expected_result = 1
        edges = []
        nodes = {
            1 : 1
        }
        result = evaluate_graph(edges, nodes)
        self.assertEqual(expected_result, result)

    def test_evaluate_graph_single_variable_node(self):
        expected_result = 1
        edges = []
        nodes = {
            1 : "x"
        }
        inputs = {
            "x" : 1
        }
        result = evaluate_graph(edges, nodes, inputs=inputs)
        self.assertEqual(expected_result, result)

    def test_evaluate_graph_multiply(self):
        expected_result = 4
        edges = [(1,2), (3,2)]
        nodes = {
            1 : 2,
            2 : "*",
            3 : "x",
        }
        inputs = {
            "x" : 2
        }
        result = evaluate_graph(edges, nodes, inputs=inputs)
        self.assertEqual(expected_result, result)

    def test_evaluate_graph_divide(self):
        expected_result = 2
        edges = [(1,2), (3,2)]
        nodes = {
            1 : 6,
            2 : "/",
            3 : "x",
        }
        inputs = {
            "x" : 3
        }
        result = evaluate_graph(edges, nodes, inputs=inputs)
        self.assertEqual(expected_result, result)

    def test_evaluate_graph_subtract(self):
        expected_result = 3
        edges = [(1,2), (3,2)]
        nodes = {
            1 : 6,
            2 : "-",
            3 : "x",
        }
        inputs = {
            "x" : 3
        }
        result = evaluate_graph(edges, nodes, inputs=inputs)
        self.assertEqual(expected_result, result)

    def test_evaluate_graph_add(self):
        expected_result = 6
        edges = [(1,2), (3,2)]
        nodes = {
            1 : 3,
            2 : "+",
            3 : "x",
        }
        inputs = {
            "x" : 3
        }
        result = evaluate_graph(edges, nodes, inputs=inputs)
        self.assertEqual(expected_result, result)   
    
