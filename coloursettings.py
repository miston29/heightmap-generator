#   insert colours in format of
#   (low, high, (r,g,b)) vlaues
#   comparison done as 
#   x > low
#   x <= high    (so end value, that is, 255 should be written as 255+1=256)
#   only the list named "colours" will be considered, you can save otheres here

colours = [
    (0, 16, (0, 0, 102)),           # dark blue
    (16, 70, (0, 102, 204)),        # ocean
    (70, 85, (102, 178, 255)),      # shore
    (85, 100, (230, 204, 153)),     # sand
    (100, 120, (112, 219, 112)),    # green
    (120, 160, (34, 139, 34)),      # forest green
    (160, 180, (25, 77, 51)),       # dark green
    (180, 220, (128, 128, 128)),    # gary stone
    (220, 255, (240, 248, 255))     # snow
]

colours2 = [
    (0, 17, (75, 0, 130)),         # Indigo / Deep Violet
    (17, 34, (128, 0, 128)),       # Purple
    (34, 51, (148, 0, 211)),       # Dark Violet
    
    (51, 68, (0, 0, 255)),         # Pure Blue
    (68, 85, (0, 128, 255)),       # Light Blue
    (85, 102, (0, 255, 255)),      # Cyan
    
    (102, 119, (0, 255, 128)),     # Spring Green
    (119, 136, (0, 255, 0)),       # Pure Green
    (136, 153, (128, 255, 0)),     # Lime Green
    
    (153, 170, (255, 255, 0)),     # Yellow
    (170, 187, (255, 165, 0)),     # Orange
    (187, 204, (255, 69, 0)),      # Orange Red
    
    (204, 221, (255, 0, 0)),       # Pure Red
    (221, 238, (255, 20, 147)),    # Deep Pink
    (238, 255, (255, 255, 255))    # White (Peak)
]
