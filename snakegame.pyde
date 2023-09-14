# The Snake game
# by Alexander Kilinkarov

from random import choice


class Game:
    def __init__(self, w, h, cell_w):
        self.playing = True
        self.score = 0
        self.field = [[0 for col in range(w)] for row in range(h)]
        self.w = w
        self.h = h
        self.cell_w = cell_w
        self.gameover = False
        self.fruit = False
        self.fps = 7
        frameRate(self.fps)
        
    def show(self):
        fill(100)

        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                square(col * self.cell_w, row * self.cell_w, self.cell_w)
        
        if self.fruit:
            fill(255, 0, 0)
            square(self.fruit[1] * self.cell_w, self.fruit[0] * self.cell_w, self.cell_w)
                
    def set_fruit(self, snake):
        self.fruit = choice([[col, row] for col in range(self.h) for row in range(self.w) if [col, row] not in snake.snake])
        
        
class Snake:
    def __init__(self, w, h):
        x = w//2
        self.snake = [[h-3, x], [h-2, x], [h-1, x]]
        self.direction = "n"
        self.color = color(0, 255, 0)
        
    def step(self, game):
        if self.direction == "n":
            if self.snake[0][0] == 0:
                self.snake = [[game.h-1, self.snake[0][1]]] + self.snake[:-1]
            else:
                self.snake = [[self.snake[0][0]-1, self.snake[0][1]]] + self.snake[:-1]
        elif self.direction == "s":
            if self.snake[0][0] == game.h-1:
                self.snake = [[0, self.snake[0][1]]] + self.snake[:-1]
            else:
                self.snake = [[self.snake[0][0]+1, self.snake[0][1]]] + self.snake[:-1]
        elif self.direction == "w":
            if self.snake[0][1] == 0:
                self.snake = [[self.snake[0][0], game.w-1]] + self.snake[:-1]
            else:
                self.snake = [[self.snake[0][0], self.snake[0][1]-1]] + self.snake[:-1]
        elif self.direction == "e":
            if self.snake[0][1] == game.w-1:
                self.snake = [[self.snake[0][0], 0]] + self.snake[:-1]
            else:
                self.snake = [[self.snake[0][0], self.snake[0][1]+1]] + self.snake[:-1]
        
        if self.snake[0] == game.fruit:
            game.score += 10
            game.set_fruit(self)
            game.fps += 1
            frameRate(game.fps)
            self.snake.extend(self.snake[-2:])
            
        if self.snake[0] in self.snake[1:]:
            game.gameover = True    
                
    def show(self, game):
        fill(self.color)
        for i in self.snake:
            y = i[0] * game.cell_w
            x = i[1] * game.cell_w
            square(x, y, game.cell_w)
            
                
def startGame():
    cell_w = 20
    w = width//cell_w
    h = height//cell_w
    
    global game, snake
    game = Game(w, h, cell_w)
    snake = Snake(w, h)
    game.set_fruit(snake)
    
            
def setup():
    size(800, 800)
    # fullScreen()
    stroke(70)
    
    startGame()
    background(30)
    
    
def draw():
    global game, snake
    background(30)
    
    game.show()
    snake.show(game)
    if not game.gameover:
        if game.playing:
            snake.step(game)
    else:
        fill(30, 200)
        rectMode(CENTER)
        rect(width//2, height//2, width * 0.8, height * 0.8)
        
        textAlign(CENTER)
        
        fill(200)
        textSize(28)
        text("Score {}".format(game.score), width//2, height//2-100)
        
        textSize(32)
        text("Game over", width//2, height//2)
    
    
def keyPressed():
    global game, snake

 
    if key == CODED:
        if game.playing:
            if keyCode == UP:
                if snake.direction != "s":
                    snake.direction = "n"   
            elif keyCode == DOWN:
                if snake.direction != "n":
                    snake.direction = "s"
            elif keyCode == LEFT:
                if snake.direction != "e":
                    snake.direction = "w"
            elif keyCode == RIGHT:
                if snake.direction != "w":
                    snake.direction = "e"
    else:
        if game.playing:  
            if key.lower() in "wasd" and game.playing:
                if key.lower() == "w":
                    if snake.direction != "s":
                        snake.direction = "n"   
                elif key.lower() == "s":
                    if snake.direction != "n":
                        snake.direction = "s"
                elif key.lower() == "a":
                    if snake.direction != "e":
                        snake.direction = "w"
                elif key.lower() == "d":
                    if snake.direction != "w":
                        snake.direction = "e"
                
        if key == "1":
            startGame()
        
        elif key.lower() == "p":
            game.playing = False if game.playing else True
                

            
    
    
    
