logo = """
.------.            _     _            _    _            _    
|? /\  |           | |   | |          | |  (_)          | |   
| /  \.------.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|? /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ ?|                            _/ |                
      `------'                           |__/           
"""


def cardUI(whodeck, chips, bet):
    decklength = len(whodeck)
    print("""
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                           _/ |                
                          |__/           
""")

    if decklength == 1:
        print(f"""
    .------.
    |  /\ {str(whodeck[0])[0]}|
    | /  \ |
    | \  / |
    |{str(whodeck[0])[0]} \/  |
    '------'                                         
    
    Chips: {chips}
    Bet: {bet}
    """)
    elif decklength == 2:
        print(f"""
    .------.
    |  /\ {str(whodeck[0])[0]}|
    | /  \.------.
    | \  /|  /\ {str(whodeck[1])[0]}|
    |{str(whodeck[0])[0]} \/ | /  \ |
    `-----| \  / |
          |{str(whodeck[1])[0]} \/  |                                             
          `------'                                          
    
    Chips: {chips}
    Bet: {bet}
    """)

    elif decklength == 3:
        print(f"""
    .------.    .------.
    |  /\ {str(whodeck[0])[0]}|    |  /\ {str(whodeck[2])[0]}|
    | /  \.------./  \ |
    | \  /|  /\ {str(whodeck[1])[0]}|\  / |
    |{str(whodeck[0])[0]} \/ | /  \ | \/  |
    `-----| \  / |-----'
          |{str(whodeck[1])[0]} \/  |                                             
          `------'                                          
    
    Chips: {chips}
    Bet: {bet}
    """)

    elif decklength == 4:
        print(f"""
    .------.    .------.
    |  /\ {str(whodeck[0])[0]}|    |  /\ {str(whodeck[2])[0]}|
    | /  \.------./  \ .------.
    | \  /|  /\ {str(whodeck[1])[0]}|\  / |  /\ {str(whodeck[3])[0]}|
    |{str(whodeck[0])[0]} \/ | /  \ | \/  | /  \ |
    `-----| \  / |-----| \  / |
          |{str(whodeck[1])[0]} \/  |     |{str(whodeck[3])[0]} \/  |                                
          `------'     `------'                            
    
    Chips: {chips}
    Bet: {bet}
    """)

    else:
        print("Too many cards for UI generation. That was extremely lucky 0.o")
