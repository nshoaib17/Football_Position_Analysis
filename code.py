def player_side(player_name):
    
    # Get first half data
    first_half = game_1_home_team[game_1_home_team['Period'] == 1]
    # Get x coordinates from first half
    player_x = first_half[f'{player_name}_x'].dropna()
    # Calculate average X position
    avg_x = player_x.mean()
    # Determine playing side based on average X position 
    if avg_x < 0.5:
        playing_side = "Left Side"
    elif avg_x > 0.5:
        playing_side = "Right Side"
    else:
        playing_side = 'Central'

    x_variance = player_x.var()
    
    print(f"{player_name} Analysis:")
    print(f"Average x position: {avg_x:.3f}")
    print(f"Left/Right side: {playing_side}")
    print(f"x variance: {x_variance:.3f}")
    

# Analysis for any player
player_analysis = player_side('Player11')