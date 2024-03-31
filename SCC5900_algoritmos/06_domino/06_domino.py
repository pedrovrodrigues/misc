Y = "YES"
N = "NO"

def read_piece():
    piece = input().split()
    piece = (int(piece[0]), int(piece[1]))
    return piece

def solve(left: int, right: int, spaces: int, piece_list: list):
    if spaces == 0:
        return True if left == right else False
    # spaces > 0
    np = len(piece_list)
    if np < spaces:
        return False
    # enough pieces to finish
    for i in range(np):
        piece = piece_list[i]
        other_pieces = piece_list.copy()
        other_pieces.pop(i)
        if piece[0] == left:
            if solve(piece[1], right, spaces-1, other_pieces):
                return True
        if piece[1] == left:
            if solve(piece[0], right, spaces-1, other_pieces):
                return True
        # if piece[0] == right:
        #     if solve(left, piece[1], spaces-1, other_pieces):
        #         return True
        # if piece[1] == right:
        #     if solve(left, piece[0], spaces-1, other_pieces):
        #         return True
        # no next step worked -> continue
        del other_pieces
    # no piece worked -> return False
    return False


if __name__ == "__main__":
    n_spaces = int(input())
    while n_spaces > 0:
        n_pieces = int(input())
        pieces = []
        left = read_piece()
        right = read_piece()
        for j in range(n_pieces):
            piece = input().split()
            piece = (int(piece[0]), int(piece[1]))
            pieces.append(piece)
        ans = solve(left[1], right[0], n_spaces, pieces)
        print(Y if ans else N)
        # check for 0
        n_spaces = int(input())

