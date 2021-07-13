
import pygame
from random import choice
from time import sleep

'variables'

run = True
size=100
colour_for_selecteds=(66,133,44)
selecteds_ids=[0]
boxes_all_ids=[]
boxes_all_colours=[]
types_of_colours=[(66,133,44),(219,68,55),(244,160,0),(15,157,88)]
types_of_colours_id=0
boxes_sqrt=7

'setting up'

pygame.init()
win = pygame.display.set_mode((boxes_sqrt*100,boxes_sqrt*100))
pygame.display.set_caption("Moving rectangle")

'functions'
    
def randomize_all_boxes_colours():

    global boxes_all_ids
    global boxes_all_colours
    global types_of_colours
    
    boxes_all_colours=[]
    boxes_all_ids=[]
    
    for i in range(boxes_sqrt**2):
        boxes_all_ids.append(i)
        boxes_all_colours.append(choice(types_of_colours))
        
def see_if_collision_between_two_boxes(box1,box2):
    
    return (box1+1==box2 and (not box1%boxes_sqrt==0)) or (box1-1==box2 and not (box1%boxes_sqrt)+1==0) or (box1+boxes_sqrt==box2 and (not box1%boxes_sqrt==0)) or box1-boxes_sqrt==box2

def check_all_boxes_for_match():

    global boxes_all_ids
    global selecteds_ids
    global boxes_all_colours
    global colour_for_selecteds

    for box in boxes_all_ids:
        for selected_box in selecteds_ids:
            
            if see_if_collision_between_two_boxes(box,selected_box):
                if boxes_all_colours[box]==colour_for_selecteds:
                    if not box in selecteds_ids:
                        
                        selecteds_ids.append(box)
                    
def render_all_boxes():

    global colour_for_selecteds
    
    colour_for_selecteds=types_of_colours[types_of_colours_id]
    i=0
    
    for y in range(boxes_sqrt):
        for x in range(boxes_sqrt):
            
            col=boxes_all_colours[i]
            
            if i in selecteds_ids:
                col=colour_for_selecteds
                
            pygame.draw.rect(win, col, (x*size, y*size, size,size))
            
            i+=1

def check_if_win():

    global selecteds_ids

    if len(selecteds_ids) == boxes_sqrt**2:
        
        selecteds_ids=[0]
        randomize_all_boxes_colours()

'randomize'
     
randomize_all_boxes_colours()

'main loop'

while run:

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_1]:
        types_of_colours_id=0
    elif keys[pygame.K_2]:
        types_of_colours_id=1
    elif keys[pygame.K_3]:
        types_of_colours_id=2
    elif keys[pygame.K_4]:
        types_of_colours_id=3
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    render_all_boxes()
    check_all_boxes_for_match()
    check_if_win()
    pygame.display.update()
    
pygame.quit()
