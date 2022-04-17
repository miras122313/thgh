



img_back = 'gg.jpg'







win_width = 900
win_height = 700
display.set_caption('pippong')
window = display.set_mode(( win_width, win_height ))
background = transform.scale(image.load(img_back), (win_width, win_height))









while run :

   if not finish :
        window.blit(background,(0, 0))

