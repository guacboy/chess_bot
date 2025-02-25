chess_piece_general_data_dict = {
    "black_king": {
        "unicode": "♚"},
    "black_queen": {
        "unicode": "♛"},
    "black_rook": {
        "unicode": "♜"},
    "black_bishop": {
        "unicode": "♝"},
    "black_knight": {
        "unicode": "♞"},
    "black_pawn": {
        "unicode": "♟"},
    
    "white_king": {
        "unicode": "♔"},
    "white_queen": {
        "unicode": "♕"},
    "white_rook": {
        "unicode": "♖"},
    "white_bishop": {
        "unicode": "♗"},
    "white_knight": {
        "unicode": "♘"},
    "white_pawn": {
        "unicode": "♙"},
}

chess_piece_specific_data_dict = {
    "br1": {
        "name": "black_rook",
    },
    "bn1": {
        "name": "black_knight",
    },
    "bb1": {
        "name": "black_bishop",
    },
    "bq": {
        "name": "black_queen",
    },
    "bk": {
        "name": "black_king",
    },
    "bb2": {
        "name": "black_bishop",
    },
    "bn2": {
        "name": "black_knight",
    },
    "br2": {
        "name": "black_rook",
    },
    "bp1": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp2": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp3": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp4": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp5": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp6": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp7": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "bp8": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    
    "wr1": {
        "name": "white_rook",
    },
    "wn1": {
        "name": "white_knight",
    },
    "wb1": {
        "name": "white_bishop",
    },
    "wq": {
        "name": "white_queen",
    },
    "wk": {
        "name": "white_king",
    },
    "wb2": {
        "name": "white_bishop",
    },
    "wn2": {
        "name": "white_knight",
    },
    "wr2": {
        "name": "white_rook",
    },
    "wp1": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp2": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp3": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp4": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp5": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp6": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp7": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
    "wp8": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
        "can_be_en_passant": False,
    },
}

cpg_data = chess_piece_general_data_dict # name shortcuts
cps_data = chess_piece_specific_data_dict

pawn_can_be_en_passant_list = {}

def invalid_move(explanation: str="") -> bool:
    print("*INVALID MOVE*", explanation)
    return False 

def pawn(chess_board_dict: dict, next_move: str, color: str) -> bool:
    # white to move
    reverse_search = 1
    third_rank = 5 # third rank from inital space
    
    # black to move
    if color == "black":
        reverse_search = -1
        third_rank = 4
    
    is_pawn = False
    
    # if attempting to capture a piece
    if len(next_move) == 4 and next_move[1] == "x":
        next_move_piece_notation = next_move[0] # example: d
        next_move_location_notation = next_move[-2:] # example: e4
        next_move_letter_notation = next_move[2] # example: e
        next_move_number_notation = next_move[3] # example: 4
        
        if next_move_piece_notation == next_move_letter_notation:
            return invalid_move("Pawn can not capture forward.")
        
        # locates pawn
        pawn = chess_board_dict.get(next_move_piece_notation + str(int(next_move_number_notation) - (1 * reverse_search)))
        
        if pawn != None:
            is_pawn = cps_data[pawn]["name"].endswith("pawn")

        if is_pawn:
            # if attempting to capture
            if chess_board_dict[next_move_location_notation] != None:
                # captures piece
                chess_board_dict[next_move_location_notation] = pawn
                # updates previous space to empty
                chess_board_dict[next_move_piece_notation + str(int(next_move_number_notation) - (1 * reverse_search))] = None
            #TODO: pawn enpassent

            # if attempting to en-passant an enemy's pawn
            elif (chess_board_dict[next_move_location_notation] == None
                  # capturing pawn is on the third rank
                  and (int(next_move_number_notation) - 1) == third_rank):
                enemy_pawn = chess_board_dict.get(next_move_letter_notation + str(int(next_move_number_notation) - (1 * reverse_search)))
                
                if enemy_pawn != None:
                    # check if the enemy pawn can be en-passant
                    if cps_data[enemy_pawn]["can_be_en_passant"] is False:
                        return invalid_move("Pawn can not be en-passant.")
                    
                    is_enemy_pawn = cps_data[enemy_pawn]["name"].endswith("pawn")
                
                if is_enemy_pawn != None:
                    # captures piece
                    chess_board_dict[next_move_location_notation] = pawn
                    # updates previous space to empty
                    chess_board_dict[next_move_piece_notation + str(int(next_move_number_notation) - (1 * reverse_search))] = None
                    # updates enemy pawn to empty
                    chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - (1 * reverse_search))] = None
            else:
                return invalid_move("No piece to capture.")
            
            return True # valid move
    # if moving piece
    else:
        next_move_letter_notation = next_move[0] # example: e
        next_move_number_notation = next_move[1] # example: 4
        
        # scans one and two spaces behind "next move" for a pawn
        for check_backwards in range(1, 3):
            # locates pawn
            pawn = chess_board_dict.get(next_move_letter_notation + str(int(next_move_number_notation) - (check_backwards * reverse_search)))
            
            if pawn != None:
                is_pawn = cps_data.get(pawn)["name"].endswith("pawn")
            
            if is_pawn:                    
                can_move_two_spaces = cps_data.get(pawn)["can_move_two_spaces"]
                
                # if moving pawn two spaces
                if check_backwards == 2:
                    #TODO: detect if a pawn can be en-passant
                    
                    # if it has already moved from inital position
                    if can_move_two_spaces is False:
                        return invalid_move("Pawn can not move two spaces.")
                
                # updates pawn eligbility to move two spaces after first move
                cps_data[pawn]["can_move_two_spaces"] = False
                
                # finds the pawn x spaces behind the "next move"
                chess_board_dict[next_move] = pawn
                # updates previous space to empty
                chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - (check_backwards * reverse_search))] = None
                
                return True # valid move
    
    return invalid_move("No pawn found.")
    
