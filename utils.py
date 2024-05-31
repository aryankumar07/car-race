import  pygame

def scale_image(img,factor):
    size = round(img.get_height()*factor), round(img.get_width()*factor)
    return pygame.transform.scale(img,size)


def scale_image_diiferent_factor(img, heightfactor,widthfactor):
    size = round(img.get_height()*heightfactor), round(img.get_width()*widthfactor)
    return pygame.transform.scale(img,size)


def blit_rotate_center(screen, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect.topleft)