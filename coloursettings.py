#   insert colours in format of
#   (low, high, (r,g,b)) vlaues
#   comparison done as 
#   x >= low
#   x < high    (so end value, that is, 255 should be written as 255+1=256)

colours2 = [
    (0, 16, (0, 0, 102)),       # Covers 0 to 16
    (16, 70, (0, 102, 204)),    # Covers everything strictly greater than 16, up to 70
    (70, 85, (102, 178, 255)),   # Covers everything strictly greater than 70, up to 85
    (85, 100, (230, 204, 153)),  # ...and so on
    (100, 120, (112, 219, 112)),
    (120, 160, (34, 139, 34)),
    (160, 180, (25, 77, 51)),
    (180, 220, (128, 128, 128)),
    (220, 255, (240, 248, 255))
]

colours = [
    # Violet / Purple
    (0, 17, (75, 0, 130)),         # Indigo / Deep Violet
    (17, 34, (128, 0, 128)),       # Purple
    (34, 51, (148, 0, 211)),       # Dark Violet
    
    # Blue / Cyan
    (51, 68, (0, 0, 255)),         # Pure Blue
    (68, 85, (0, 128, 255)),       # Light Blue
    (85, 102, (0, 255, 255)),      # Cyan
    
    # Green
    (102, 119, (0, 255, 128)),     # Spring Green
    (119, 136, (0, 255, 0)),       # Pure Green
    (136, 153, (128, 255, 0)),     # Lime Green
    
    # Yellow / Orange
    (153, 170, (255, 255, 0)),     # Yellow
    (170, 187, (255, 165, 0)),     # Orange
    (187, 204, (255, 69, 0)),      # Orange Red
    
    # Red / Pink / White
    (204, 221, (255, 0, 0)),       # Pure Red
    (221, 238, (255, 20, 147)),    # Deep Pink
    (238, 255, (255, 255, 255))    # White (Peak)
]