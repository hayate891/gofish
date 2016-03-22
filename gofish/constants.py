EMPTY, BLACK, WHITE = 0, 1, 2


class OffBoard(Exception): pass
class BadBoardSize(Exception): pass
class ParserFail(Exception): pass
class WrongNode(Exception): pass


handicap_points_19 = {
    0: [],
    1: [],
    2: [(16,4), (4,16)],
    3: [(16,4), (4,16), (16,16)],
    4: [(16,4), (4,16), (16,16), (4, 4)],
    5: [(16,4), (4,16), (16,16), (4, 4), (10, 10)],
    6: [(16,4), (4,16), (16,16), (4, 4), (4, 10), (16, 10)],
    7: [(16,4), (4,16), (16,16), (4, 4), (4, 10), (16, 10), (10, 10)],
    8: [(16,4), (4,16), (16,16), (4, 4), (4, 10), (16, 10), (10, 4), (10, 16)],
    9: [(16,4), (4,16), (16,16), (4, 4), (4, 10), (16, 10), (10, 4), (10, 16), (10, 10)]
}
