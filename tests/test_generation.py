import generation.net_generation as gn
import generation.algorithms as al


class TestConnection:
    def test_weakly_connection_true(self):
        ex1 = {0: [1], 1: [4, 5], 2: [3], 3: [4], 4: [], 5: [4], 6: [1]}
        assert gn.is_weakly_connected(ex1) == 1

    def test_weakly_connection_false(self):
        ex2 = {0: [1], 1: [4, 5], 2: [3], 3: [], 4: [], 5: [4], 6: [1]}
        assert gn.is_weakly_connected(ex2) == 0

    def test_strongly_connection_true(self):
        ex1 = {0: [1], 1: [4, 5], 2: [1, 3], 3: [5], 4: [2, 3], 5: [6], 6: [1]}
        assert gn.is_strongly_connected(ex1) == (True, 0)

    def test_strongly_connection_false(self):
        ex2 = {0: [1], 1: [4, 5], 2: [3], 3: [4], 4: [], 5: [4], 6: [1]}
        assert gn.is_strongly_connected(ex2) == (False, {0, 1, 4, 5})


class TestBaseGeneration:
    def test_base_generation_5(self):
        n = 5
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_6(self):
        n = 6
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_7(self):
        n = 7
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_8(self):
        n = 8
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_9(self):
        n = 9
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_10(self):
        n = 10
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_11(self):
        n = 11
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_12(self):
        n = 12
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_13(self):
        n = 13
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_14(self):
        n = 14
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)

    def test_base_generation_15(self):
        n = 15
        graph = gn.generate_graph_base(n)
        assert gn.is_weakly_connected(graph) == 1, "{}".format(graph)


class TestMakeStronglyConnected:
    def test_make_strongly_connected_5(self):
        n = 5
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_6(self):
        n = 6
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_7(self):
        n = 7
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_8(self):
        n = 8
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_9(self):
        n = 9
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_10(self):
        n = 10
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_11(self):
        n = 11
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_12(self):
        n = 12
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_13(self):
        n = 13
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_14(self):
        n = 14
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)

    def test_make_strongly_connected_15(self):
        n = 15
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        assert gn.is_strongly_connected(graph) == (True, 0), "{}".format(graph)


class TestFordFulkerson:
    def test_ford_fulkerson(self):
        graph = {0: {1: 25, 2: 47, 3: 14, 4: 21},
                 1: {5: 11, 11: 13},
                 2: {5: 48, 6: 7, 7: 23},
                 3: {2: 27, 7: 20},
                 4: {3: 3, 10: 43},
                 5: {8: 9},
                 6: {5: 16, 7: 5, 8: 31},
                 7: {10: 52},
                 8: {9: 22, 11: 38},
                 9: {6: 15, 11: 60},
                 10: {6: 23, 9: 35, 11: 39},
                 11: {}}
        res = al.FordFulkerson(graph)
        assert res == (87, [0, 1, 2, 5], [3, 4, 6, 7, 8, 9, 10, 11]), "{}".format(res)


class TestNetGeneration:
    def test_net_generation_5(self):
        n = 5
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}".format(net)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_6(self):
        n = 6
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}".format(net)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_7(self):
        n = 7
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}".format(net)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_8(self):
        n = 8
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}".format(net)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_9(self):
        n = 9
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_10(self):
        n = 10
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_11(self):
        n = 11
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_12(self):
        n = 12
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_13(self):
        n = 13
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_14(self):
        n = 14
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_15(self):
        n = 15
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_16(self):
        n = 16
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_17(self):
        n = 17
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_18(self):
        n = 18
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_19(self):
        n = 19
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_20(self):
        n = 20
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_21(self):
        n = 21
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_22(self):
        n = 22
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_23(self):
        n = 23
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_24(self):
        n = 24
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

    def test_net_generation_25(self):
        n = 25
        graph = gn.generate_graph_base(n)
        gn.make_strongly_connected(graph)
        cutA, cutB, cut, r_cut = gn.make_cut(graph)
        net, flow1 = gn.make_flow(graph, r_cut)
        assert gn.check_graph_flow(net) == 1, "{}\n{}\n{}\n{}".format(net, flow1, cutA, cutB)
        gn.make_throughput(net, cut)
        flow2, A, B = al.FordFulkerson(net)
        assert flow1 == flow2, "{}".format(net)
        assert cutA == A
        assert cutB == B

