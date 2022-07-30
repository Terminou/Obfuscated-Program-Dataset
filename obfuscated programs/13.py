stockfish.set_elo_rating(3000)
stockfish.set_depth(15)

def evaluate_position(white_turn=True, board_flipped=is_board_flipped):
    start_time = time.time()
    # take a screenshot of the board
    take_screenshot('image1.png')
    image = cv2.imread('image1.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray image.png', gray)
    im = Image.open('gray image.png')

    # Set up the board from the Chess library
    board = chess.Board()
    # Remove all the pieces because they will be specified in the next step
    board.clear()
    # Set the turn to White to play, unless otherwise specified
    board.turn = white_turn 

    nn=0;
    n=0
    for i in range(8):
        for j in range(8):

            im1=im.crop((j*(box_width), i*(box_width), (j+1)*(box_width-0), (i+1)*(box_width-0)))
            im1.save('pieces//'+str(nn)+'.png')
            n+=1        

            n=myList[i][j]
            # Read each cropped chess square and identify the chess piece and color.
            image = cv2.imread('pieces//'+str(nn)+'.png')
            BlackPiece=np.sum(image==0)
            WhitePiece=np.sum(image==255)
            res_val=(0,0,True)
            if BlackPiece>min(BlackPixelValues)-50:
                # Identify the chess piece based on he number of black pixels closest to the 
                # values from the BlackPieces dictionary.
                col_key, res_val = min(BlackPieces.items(), key=lambda x: abs(BlackPiece - x[1][0]))
            if WhitePiece>min(WhitePixelValues)-50:
                # Identify the chess piece based on he number of white pixels closest to the 
                # values from the BlackPieces dictionary.
                col_key, res_val = min(WhitePieces.items(), key=lambda x: abs(WhitePiece - x[1][0]))
            # set the chess piece on the board based on it position, piece type, and color. 
            board.set_piece_at(n,piece=chess.Piece(piece_type=res_val[1],color=res_val[2]))
            nn+=1

    #create the FEN based on the current position 
    turn_fen=' w - - 1 0' if board.turn == True else ' b - - 0 1'
    current_fen=board.board_fen()+turn_fen
    # Assign the postion in Stockfish based on FEN
    stockfish.set_fen_position(current_fen)
    # Get the top moves
    top_moves=stockfish.get_top_moves()
    #Get the best move
    my_move=top_moves[0]['Move']
    # Move the chess piece based on the best move
    board.push(chess.Move.from_uci(my_move))

    #Create output
    print('Time:',time.time()-start_time)
    print('Best Move:', my_move)
    print('Evaluation:', stockfish.get_evaluation())
    print('Top moves:')
    for i in top_moves:
        print(i)

    if board_flipped:
        board.apply_transform(chess.flip_vertical)
        board.apply_transform(chess.flip_horizontal)
        display(board)
    else:
        display(board)