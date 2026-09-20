import pygame
import sys
import json
import os

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 40

GRAVITY = 0.5
JUMP_POWER = -12
SPEED = 5
ENEMY_SPEED = 2

BG_COLOR = (30, 30, 40)
PLAYER_COLOR = (50, 150, 255)
WALL_COLOR = (100, 100, 100)
COIN_COLOR = (255, 215, 0)
LAVA_COLOR = (220, 50, 50)
TRAP_COLOR = (200, 100, 50) 
ENEMY_COLOR = (255, 100, 0)
FLYING_ENEMY_COLOR = (150, 50, 200)
SMART_ENEMY_COLOR = (255, 20, 80)
EXIT_CLOSED = (150, 50, 50)
EXIT_OPEN = (50, 200, 50)
BTN_COLOR = (200, 200, 200, 150)
BTN_HOVER = (255, 255, 255, 200)

MISSIONS = [
    [
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X        M         X",
        "X                  X",
        "X                  X",
        "X                  X",
        "P   X            X E",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X        XXX       X",
        "X    XX            X",
        "P  XXX    M   XX   E",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X           C      X",
        "X         XXX      X",
        "X      C           X",
        "X    XXX           E",
        "P XX               X",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X         M        E",
        "P     XXXXXXXX     X",
        "XXXXXXX      XXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X                  X",
        "X      C    C      X",
        "X     XXX  XXX     X",
        "X                  E",
        "P X              X X",
        "XXXXLLLLLLLLLLLLXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXX",
        "X            X",
        "X            X",
        "X            X",
        "X            X",
        "X            X",
        "X  C       C E",
        "X XXX     XXXX",
        "P XX       XXX",
        "XXXXLLLLLLLXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X C                X",
        "XXXXX              X",
        "X             XXXX X",
        "X  C               X",
        "X XXXX           C X",
        "X              XXXXX",
        "X                  E",
        "P       XXXXXXXXXXXX",
        "XXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X  C           C   X",
        "X XXX         XXX  X",
        "X                  X",
        "X    M       M     E",
        "X   XXXX   XXXX    X",
        "P XX   X   X   XX  X",
        "XXXX   XXXXX   XXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X C   C   C   C    E",
        "XXX  XXX  XXX XXX  X",
        "X                  X",
        "X                  X",
        "P  X   X   X   X  XX",
        "XXXLLLLLLLLLLLLLXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "XXXX            XXXX",
        "X      XXXXXX      X",
        "X C M X L  L X M C X",
        "XXXXXCX      XCXXXXX",
        "X                  X",
        "X     X          X E",
        "P XXXXXXXXXXXXXXXXXX",
        "XXXLLLLLLLLLLLLLLXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X  C   F      C    X",
        "X XXX        XXX   X",
        "X                  X",
        "X      T  T        E",
        "X    XXXXXXXX      X",
        "P  X               X",
        "XXXXLLLLLLLLLLLLXXXX"
    ],
    [
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X C              C X",
        "XXXX            XXXX",
        "X                  X",
        "X    XXXX  XXXX    X",
        "X    X        X    E",
        "X    X   F    X    X",
        "P XX X        X XX X",
        "XXLLLLLLLLLLLLLLLLXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X  C               X",
        "X XXX  S  C      E X",
        "X     XXXXXXXXXXXX X",
        "X                  X",
        "P                  X",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X       X          X",
        "X XXXXX X XXXXXXXX X",
        "X X     X X      X X",
        "X X XXXXX X XXXX X X",
        "X X X   X X    X   X",
        "X   X P X   XX X ECX",
        "XXXXX X XXXXXX XXXXX",
        "X M C X            X",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "XC       X       CEX",
        "XXXXXX   X   XXXXXXX",
        "X        X         X",
        "X       XXX        X",
        "X  F             F X",
        "X     XXXXXXX      X",
        "X                  X",
        "P  X           X   X",
        "XXXXLLLLLLLLLLLXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X  C  C  C  C  C   X",
        "X  X  X  X  X  X   X",
        "X                  X",
        "X  TX TX TX TX TX  X",
        "XX X  X  X  X  X   E",
        "X                  X",
        "P                  X",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X  C     C     C   X",
        "X  X     X     X   X",
        "X     F     F      X",
        "X                  X",
        "X    XXX   XXX     X",
        "X                  E",
        "X                  X",
        "P X      L      X  X",
        "XXXXXXLLLLLLLXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  X",
        "X                  X",
        "X  C S XXXXX S C   E",
        "X XXXX       XXXX  X",
        "X                  X",
        "X                  X",
        "P    XXXXXXXX      X",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X                  X",
        "X                  E",
        "P X CMX MCXC MXM CXX",
        "XXXXXXXXXXXXXXXXXXXX"
    ],
    [ 
        "XXXXXXXXXXXXXXXXXXXX",
        "X C X        X C   X",
        "XXX X        X XXX X",
        "X   X        X   X X",
        "X      XXXX      X X",
        "X  X  X  C X  X    X",
        "XXXXX X    X XXXXX X",
        "X              S   E",
        "P  XXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXX"
    ]
]

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.is_pressed = False
        self.font = pygame.font.SysFont(None, 36)

    def draw(self, surface):
        btn_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        color = BTN_HOVER if self.is_pressed else BTN_COLOR
        pygame.draw.rect(btn_surface, color, btn_surface.get_rect(), border_radius=10)
        surface.blit(btn_surface, (self.rect.x, self.rect.y))
        
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_input(self, pointers):
        self.is_pressed = False
        for p in pointers:
            if self.rect.collidepoint(p):
                self.is_pressed = True
                break
        return self.is_pressed

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.exact_x = float(x)
        self.exact_y = float(y)
        
        self.vel_y = 0.0
        self.on_ground = False
        self.prev_on_ground = False
        self.coins_collected = 0

    def update(self, move_left, move_right, jump, walls, lavas, traps, enemies, coins, exit_door, game):
        if self.rect.y > HEIGHT:
            game.player_died()
            return

        dx = 0
        if move_left:
            dx -= SPEED
        if move_right:
            dx += SPEED

        self.exact_x += dx
        self.rect.x = int(self.exact_x)
        self.check_collisions_x(walls)

        if jump and self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False

        
        self.vel_y += GRAVITY
        self.exact_y += self.vel_y
        self.rect.y = int(self.exact_y)
        
        self.on_ground = False
        self.check_collisions_y(walls)
        
        if self.on_ground and not self.prev_on_ground:
            t_x = self.rect.centerx // TILE_SIZE
            t_y = self.rect.bottom // TILE_SIZE
            key = str(game.current_mission) + "_" + str(t_x) + "_" + str(t_y)
            game.landing_heatmap[key] = game.landing_heatmap.get(key, 0) + 1
        self.prev_on_ground = self.on_ground

        hit_coins = pygame.sprite.spritecollide(self, coins, True)
        if hit_coins:
            self.coins_collected += len(hit_coins)
            game.score += 100 * len(hit_coins)

        if pygame.sprite.spritecollideany(self, lavas) or pygame.sprite.spritecollide(self, traps, True):
            game.player_died()

        hit_enemies = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in hit_enemies:
           
            if self.vel_y > 0 and self.rect.bottom <= enemy.rect.centery + 15:
                k_tx = enemy.rect.centerx // TILE_SIZE
                k_ty = enemy.rect.centery // TILE_SIZE
                k_key = str(game.current_mission) + "_" + str(k_tx) + "_" + str(k_ty)
                game.kill_heatmap[k_key] = game.kill_heatmap.get(k_key, 0) + 1
                
                enemy.kill() 
                self.vel_y = JUMP_POWER * 0.7 
                game.score += 250 
            else:
                game.player_died()

        if exit_door and self.rect.colliderect(exit_door.rect):
            if game.total_coins == 0 or self.coins_collected == game.total_coins:
                game.score += 500
                game.next_mission()

    def check_collisions_x(self, walls):
        for wall in pygame.sprite.spritecollide(self, walls, False):
            if self.rect.centerx < wall.rect.centerx:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        self.exact_x = float(self.rect.x)

    def check_collisions_y(self, walls):
        for wall in pygame.sprite.spritecollide(self, walls, False):
            if self.vel_y > 0:
                self.rect.bottom = wall.rect.top
                self.vel_y = 0
                self.on_ground = True
            elif self.vel_y < 0:
                self.rect.top = wall.rect.bottom
                self.vel_y = 0
        self.exact_y = float(self.rect.y)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect(topleft=(x + 5, y + 10))
        self.exact_x = float(self.rect.x)
        self.exact_y = float(self.rect.y)
        self.direction = 1 
        self.vel_y = 0.0

    def update(self, walls, player=None, game=None):
        if self.rect.y > HEIGHT:
            self.kill()
            return

        self.vel_y += GRAVITY
        self.exact_y += self.vel_y
        self.rect.y = int(self.exact_y)
        
        hit_walls_y = pygame.sprite.spritecollide(self, walls, False)
        for wall in hit_walls_y:
            if self.vel_y > 0:
                self.rect.bottom = wall.rect.top
                self.vel_y = 0
            elif self.vel_y < 0:
                self.rect.top = wall.rect.bottom
                self.vel_y = 0
        self.exact_y = float(self.rect.y)

        self.exact_x += float(ENEMY_SPEED * self.direction)
        self.rect.x = int(self.exact_x)
        
        hit_walls_x = pygame.sprite.spritecollide(self, walls, False)
        if hit_walls_x:
            if self.direction == 1:
                self.rect.right = hit_walls_x[0].rect.left
            else:
                self.rect.left = hit_walls_x[0].rect.right
            self.direction *= -1
            self.exact_x = float(self.rect.x)
        
        if game and pygame.sprite.spritecollide(self, game.traps, True):
            self.kill()


class FlyingEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(FLYING_ENEMY_COLOR)
        self.rect = self.image.get_rect(topleft=(x + 5, y + 5))
        self.exact_x = float(self.rect.x)
        self.direction = 1
        self.speed = ENEMY_SPEED + 1.0

    def update(self, walls, player=None, game=None):
        if self.rect.y > HEIGHT:
            self.kill()
            return
        
        self.exact_x += self.speed * self.direction
        self.rect.x = int(self.exact_x)
        
        hit_walls_x = pygame.sprite.spritecollide(self, walls, False)
        if hit_walls_x:
            if self.direction == 1:
                self.rect.right = hit_walls_x[0].rect.left
            else:
                self.rect.left = hit_walls_x[0].rect.right
            self.direction *= -1
            self.exact_x = float(self.rect.x)
        
        if game and pygame.sprite.spritecollide(self, game.traps, True):
            self.kill()


class SmartEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(SMART_ENEMY_COLOR)
        self.rect = self.image.get_rect(topleft=(x + 5, y + 10))
        self.exact_x = float(self.rect.x)
        self.exact_y = float(self.rect.y)
        self.vel_y = 0.0
        self.on_ground = False
        self.speed = float(ENEMY_SPEED - 0.25) 

        self.mode = "CHASE" 
        self.ambush_target = None
        self.ambush_timeout = 0
        self.trap_cooldown = 180 

        self.last_x = self.exact_x
        self.stuck_frames = 0
        
        self.nav_override = 0
        self.nav_dir = 1

    def update(self, walls, player, game=None):
        if not player or self.rect.y > HEIGHT:
            self.kill()
            return

        self.vel_y += GRAVITY
        self.exact_y += self.vel_y
        self.rect.y = int(self.exact_y)
        self.on_ground = False
        
        hit_walls_y = pygame.sprite.spritecollide(self, walls, False)
        for wall in hit_walls_y:
            if self.vel_y > 0:
                self.rect.bottom = wall.rect.top
                self.vel_y = 0
                self.on_ground = True
            elif self.vel_y < 0:
                self.rect.top = wall.rect.bottom
                self.vel_y = 0
        self.exact_y = float(self.rect.y)

        if abs(self.exact_x - self.last_x) <= 1.0:
            self.stuck_frames += 1
        else:
            self.stuck_frames = 0
        self.last_x = self.exact_x

        player_is_above = (player.rect.bottom < self.rect.top) and (abs(player.rect.centerx - self.rect.centerx) < TILE_SIZE * 2)
        player_is_unreachable = (self.rect.top - player.rect.bottom) > (TILE_SIZE * 2)

        if game and game.kill_heatmap and self.mode != "DODGE" and self.nav_override <= 0:
            e_tx = self.rect.centerx // TILE_SIZE
            e_ty = self.rect.centery // TILE_SIZE
            danger_key = str(game.current_mission) + "_" + str(e_tx) + "_" + str(e_ty)
            danger_level = game.kill_heatmap.get(danger_key, 0)
            
            is_player_strafing = player.vel_y > 0 and player.rect.bottom < self.rect.bottom and abs(player.rect.centerx - self.rect.centerx) < TILE_SIZE * 3
            
            if danger_level > 0 and is_player_strafing:
                self.mode = "DODGE"
                self.nav_override = 45 
                self.nav_dir = 1 if self.rect.centerx > player.rect.centerx else -1
                if self.on_ground:
                    self.vel_y = JUMP_POWER * 0.8
                    self.on_ground = False

        if self.nav_override > 0:
            self.nav_override -= 1
            if self.nav_override <= 0 and self.mode == "DODGE":
                self.mode = "CHASE"
        else:
            if self.stuck_frames > 20:
                self.nav_override = 60 
                self.nav_dir = -1 if (player.rect.centerx > self.rect.centerx) else 1
                self.stuck_frames = 0
                if self.mode == "AMBUSH":
                    self.mode = "CHASE"
                    self.ambush_target = None
                    self.trap_cooldown = 120
            
            elif player_is_above and self.on_ground:
                if player_is_unreachable:
                    self.nav_override = 90 
                    self.nav_dir = 1 if self.rect.centerx < WIDTH // 2 else -1
                else:
                    self.vel_y = JUMP_POWER
                    self.on_ground = False

        if self.trap_cooldown > 0:
            self.trap_cooldown -= 1

        
        if self.mode == "CHASE" and self.trap_cooldown <= 0 and game and game.landing_heatmap and self.nav_override == 0:
            best_heat = 0
            best_spot = None
            
            for key, heat in list(game.landing_heatmap.items()):
                parts = key.split('_')
                if len(parts) == 3 and parts[0] == str(game.current_mission):
                    cx, cy = int(parts[1]), int(parts[2])
                    if heat > best_heat:
                        t_x = cx * TILE_SIZE + TILE_SIZE // 2
                        is_in_middle = (WIDTH * 0.1) <= t_x <= (WIDTH * 0.9)

                        trap_rect = pygame.Rect(cx*TILE_SIZE, (cy-1)*TILE_SIZE + TILE_SIZE//2, TILE_SIZE, TILE_SIZE//2)
                        ground_rect = pygame.Rect(cx*TILE_SIZE, cy*TILE_SIZE, TILE_SIZE, 2)
                        
                        wall_col = False
                        for w in walls:
                            if w.rect.colliderect(trap_rect):
                                wall_col = True
                                break
                                
                        ground_exists = False
                        for w in walls:
                            if w.rect.colliderect(ground_rect):
                                ground_exists = True
                                break
                                
                        trap_col = False
                        for t in game.traps:
                            if t.rect.colliderect(trap_rect):
                                trap_col = True
                                break
                                
                        exit_col = False
                        if game.exit_door:
                            exit_safe_zone = game.exit_door.rect.inflate(TILE_SIZE * 4, TILE_SIZE * 4)
                            if trap_rect.colliderect(exit_safe_zone):
                                exit_col = True
                        
                        if not wall_col and ground_exists and not trap_col and not exit_col and is_in_middle:
                            best_heat = heat
                            best_spot = (t_x, cx, cy)
            
            if best_spot:
                self.ambush_target = best_spot
                self.mode = "AMBUSH"
                self.ambush_timeout = 600 

        dx = 0.0
        if self.mode == "DODGE":
            target_x = self.rect.centerx + (self.nav_dir * 100)
            dx = (self.speed + 1.5) * self.nav_dir 

        elif self.nav_override > 0:
            target_x = self.rect.centerx + (self.nav_dir * 100)
            dx = self.speed * self.nav_dir
            
        elif self.mode == "AMBUSH" and self.ambush_target:
            target_x = self.ambush_target[0]
            self.ambush_timeout -= 1
            
            if self.ambush_timeout <= 0:
                self.mode = "CHASE"
                self.trap_cooldown = 120
                self.ambush_target = None
            
            elif self.on_ground and abs(self.rect.centerx - target_x) <= 10:
                cx = self.ambush_target[1]
                cy = self.ambush_target[2]
                
                new_trap = Trap(cx * TILE_SIZE, (cy - 1) * TILE_SIZE)
                game.traps.add(new_trap)
                game.all_sprites.add(new_trap)
                
                self.trap_cooldown = 400
                self.mode = "WAIT" 
                self.ambush_target = None
                target_x = self.rect.centerx
            
            else:
                if target_x < self.rect.centerx - 5:
                    dx = -self.speed
                elif target_x > self.rect.centerx + 5:
                    dx = self.speed
            
        elif self.mode == "WAIT":
            target_x = self.rect.centerx
            if abs(player.rect.centerx - self.rect.centerx) < 200:
                self.mode = "CHASE"
        else: 
            target_x = player.rect.centerx
            if target_x < self.rect.centerx - 5:
                dx = -self.speed
            elif target_x > self.rect.centerx + 5:
                dx = self.speed

        self.exact_x += dx
        self.rect.x = int(self.exact_x)
        
        hit_walls_x = pygame.sprite.spritecollide(self, walls, False)
        if hit_walls_x:
            if dx > 0:
                self.rect.right = hit_walls_x[0].rect.left
            elif dx < 0:
                self.rect.left = hit_walls_x[0].rect.right
            self.exact_x = float(self.rect.x)
            
            if self.on_ground:
                self.vel_y = JUMP_POWER 
                self.on_ground = False

        if self.on_ground and dx != 0:
            direction_x = TILE_SIZE if dx > 0 else -TILE_SIZE
            gap_rect = pygame.Rect(self.rect.centerx + direction_x, self.rect.bottom + 5, 2, 2)
            
            is_gap_ahead = True
            for wall in walls:
                if wall.rect.colliderect(gap_rect):
                    is_gap_ahead = False
                    break
            
            platform_rect = pygame.Rect(self.rect.centerx + direction_x, self.rect.top - 10, 2, 2)
            
            is_platform_ahead = False
            for wall in walls:
                if wall.rect.colliderect(platform_rect):
                    is_platform_ahead = True
                    break

            if is_gap_ahead:
                safe_landing = False
                for i in range(1, 4):
                    check_x = self.rect.centerx + (TILE_SIZE * i * (1 if dx > 0 else -1))
                    check_rect = pygame.Rect(check_x, 0, 2, HEIGHT)
                    for w in walls:
                        if w.rect.colliderect(check_rect):
                            safe_landing = True
                            break
                    if safe_landing:
                        break
                
                if not safe_landing:
                    self.exact_x -= dx 
                    self.rect.x = int(self.exact_x)
                    self.nav_override = 60
                    self.nav_dir = -1 if dx > 0 else 1
                else:
                    if player.rect.centery <= self.rect.centery + TILE_SIZE:
                        self.vel_y = JUMP_POWER * 0.95
                        self.on_ground = False
            
          
            elif player.rect.bottom < self.rect.bottom - TILE_SIZE and is_platform_ahead:
                self.vel_y = JUMP_POWER * 0.95
                self.on_ground = False


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE // 2))
        self.image.fill(TRAP_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y + TILE_SIZE // 2))

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(COIN_COLOR)
        self.rect = self.image.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 64)
        self.debug_font = pygame.font.SysFont(None, 24)
        
        self.state = "LOGIN" 
        self.current_player = "V" 

        self.current_mission = 0
        self.lives = 3
        self.score = 0
        
        self.analytics_file = "player_analytics.json"
        self.global_database = self.load_database()
        
        if "V" not in self.global_database:
            self.global_database["V"] = {"heatmap": {}, "kill_heatmap": {}, "history": []}
        
        self.landing_heatmap = self.global_database["V"]["heatmap"]
        self.kill_heatmap = self.global_database["V"].get("kill_heatmap", {})
        self.player_history = self.global_database["V"]["history"]
        
        self.btn_left = Button(30, HEIGHT - 100, 80, 80, "<")
        self.btn_right = Button(130, HEIGHT - 100, 80, 80, ">")
        self.btn_jump = Button(WIDTH - 120, HEIGHT - 100, 90, 80, "JUMP")
        
        self.btn_login = Button(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50, "LOGIN AS 'V'")
        self.btn_play = Button(WIDTH//2 - 160, HEIGHT - 100, 150, 50, "PLAY GAME")
        self.btn_logout = Button(WIDTH//2 + 10, HEIGHT - 100, 150, 50, "SAVE & QUIT")
        
        self.btn_continue = Button(WIDTH//2 - 75, HEIGHT//2 + 100, 150, 50, "CONTINUE")
        
        self.active_touches = {}
        self.exit_door = None
        self.player = None

    def load_database(self):
        if os.path.exists(self.analytics_file):
            try:
                with open(self.analytics_file, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_database(self):
        self.global_database["V"] = {
        "heatmap": self.landing_heatmap,
        "kill_heatmap": self.kill_heatmap,
        "history": self.player_history
        }
        with open(self.analytics_file, "w") as f:
            json.dump(self.global_database, f)

    def start_game(self):
        self.current_mission = 0
        self.score = 0
        self.lives = 3
        self.state = "PLAYING"
        self.load_level()

    def record_history(self, result_msg):
        h_num = len(self.player_history) + 1
        record = f"H{h_num}: {result_msg} | Score: {self.score} | Mission: {self.current_mission + 1}"
        self.player_history.append(record)
        
        if len(self.player_history) > 100:
            self.player_history.pop(0)
        
        self.save_database()

    def load_level(self):
        if self.current_mission >= len(MISSIONS):
            self.record_history("GAME BEATEN")
            self.game_over = True
            return

        self.game_over = False
        level_data = MISSIONS[self.current_mission]
        
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.total_coins = 0
        self.exit_door = None
        self.player = None 

        for row_index, row in enumerate(level_data):
            for col_index, cell in enumerate(row):
                if cell == 'P':
                    self.player = Player(col_index * TILE_SIZE, row_index * TILE_SIZE)
                    self.all_sprites.add(self.player)

        for row_index, row in enumerate(level_data):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == 'X':
                    wall = Block(x, y, WALL_COLOR)
                    self.walls.add(wall)
                    self.all_sprites.add(wall)
                elif cell == 'L':
                    lava = Block(x, y, LAVA_COLOR)
                    self.lavas.add(lava)
                    self.all_sprites.add(lava)
                elif cell == 'T':
                    trap = Trap(x, y)
                    self.traps.add(trap)
                    self.all_sprites.add(trap)
                elif cell == 'C':
                    coin = Coin(x, y)
                    self.coins.add(coin)
                    self.all_sprites.add(coin)
                    self.total_coins += 1
                elif cell == 'M':
                    enemy = Enemy(x, y)
                    self.enemies.add(enemy)
                    self.all_sprites.add(enemy)
                elif cell == 'F': 
                    enemy = FlyingEnemy(x, y)
                    self.enemies.add(enemy)
                    self.all_sprites.add(enemy)
                elif cell == 'S':
                    enemy = SmartEnemy(x, y)
                    self.enemies.add(enemy)
                    self.all_sprites.add(enemy)
                elif cell == 'E':
                    self.exit_door = Block(x, y, EXIT_CLOSED)
                    self.all_sprites.add(self.exit_door)

        if not self.player:
            print(f"Warning: Level {self.current_mission + 1} has no 'P' character. Player cannot spawn.")
            self.game_over = True 

    def player_died(self):
        self.lives -= 1
        if self.lives <= 0:
            self.record_history("GAME OVER")
            self.state = "HISTORY"
        else:
            self.load_level()

    def next_mission(self):
        self.save_database() 
        self.current_mission += 1
        self.load_level()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_database() 
                    running = False
                
                elif event.type in (pygame.FINGERDOWN, pygame.FINGERMOTION):
                    self.active_touches[event.finger_id] = (event.x * WIDTH, event.y * HEIGHT)
                
                elif event.type == pygame.FINGERUP:
                    if event.finger_id in self.active_touches:
                        del self.active_touches[event.finger_id]

            pointers = list(self.active_touches.values())
            if pygame.mouse.get_pressed()[0]:
                pointers.append(pygame.mouse.get_pos())

            self.screen.fill(BG_COLOR)

            if self.state == "LOGIN":
                title_text = self.title_font.render("BLOCK GAME", True, PLAYER_COLOR)
                prompt_text = self.font.render("Select Profile to Load Data", True, (255, 255, 255))
                
                self.screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//4))
                self.screen.blit(prompt_text, (WIDTH//2 - prompt_text.get_width()//2, HEIGHT//2 - 30))
                
                if self.btn_login.check_input(pointers):
                    self.state = "HISTORY"
                self.btn_login.draw(self.screen)

            elif self.state == "HISTORY":
                welcome_text = self.title_font.render(f"Welcome back, {self.current_player}!", True, COIN_COLOR)
                history_title = self.font.render("Your Recent History:", True, (255, 255, 255))
                
                self.screen.blit(welcome_text, (WIDTH//2 - welcome_text.get_width()//2, 50))
                self.screen.blit(history_title, (WIDTH//2 - history_title.get_width()//2, 120))
                
                start_y = 170
                recent_history = self.player_history[-8:]
                if not recent_history:
                    empty_text = self.font.render("No history yet. Play a game!", True, (150, 150, 150))
                    self.screen.blit(empty_text, (WIDTH//2 - empty_text.get_width()//2, start_y))
                else:
                    for entry in reversed(recent_history): 
                        hist_text = self.font.render(entry, True, (200, 220, 255))
                        self.screen.blit(hist_text, (WIDTH//2 - hist_text.get_width()//2, start_y))
                        start_y += 40
                
                if self.btn_play.check_input(pointers):
                    self.start_game()
                if self.btn_logout.check_input(pointers):
                    self.save_database()
                    self.state = "LOGIN"
                
                self.btn_play.draw(self.screen)
                self.btn_logout.draw(self.screen)

            elif self.state == "PLAYING":
                btn_left_pressed = self.btn_left.check_input(pointers)
                btn_right_pressed = self.btn_right.check_input(pointers)
                btn_jump_pressed = self.btn_jump.check_input(pointers)

                keys = pygame.key.get_pressed()
                
                move_left = keys[pygame.K_LEFT] or keys[pygame.K_a] or btn_left_pressed
                move_right = keys[pygame.K_RIGHT] or keys[pygame.K_d] or btn_right_pressed
                jump = keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w] or btn_jump_pressed

                if self.game_over:
                    text = self.title_font.render(f"YOU WIN! Final Score: {self.score}", True, (50, 255, 50))
                    self.screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
                    
                    if self.btn_continue.check_input(pointers):
                        self.state = "HISTORY"
                        self.active_touches.clear() 

                    self.btn_continue.draw(self.screen)
                else:
                    if self.exit_door:
                        if self.total_coins == 0 or self.player.coins_collected == self.total_coins:
                            self.exit_door.image.fill(EXIT_OPEN)
                        else:
                            self.exit_door.image.fill(EXIT_CLOSED)

                    self.enemies.update(self.walls, self.player, self)
                    
                    if self.player:
                        self.player.update(move_left, move_right, jump, 
                        self.walls, self.lavas, self.traps, self.enemies, 
                        self.coins, self.exit_door, self)
                    
                    self.all_sprites.draw(self.screen)

                    mission_text = self.font.render(f"Mission: {self.current_mission + 1} / {len(MISSIONS)}", True, (255, 255, 255))
                    coin_text = self.font.render(f"Coins: {self.player.coins_collected if self.player else 0} / {self.total_coins}", True, COIN_COLOR)
                    score_text = self.font.render(f"Score: {self.score}", True, (150, 255, 150))
                    lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 100, 100))
                    name_tag = self.font.render(f"Player: {self.current_player}", True, (100, 200, 255))
                    
                    self.screen.blit(mission_text, (10, 10))
                    self.screen.blit(coin_text, (10, 40))
                    self.screen.blit(score_text, (10, 70))
                    self.screen.blit(lives_text, (10, 100))
                    self.screen.blit(name_tag, (WIDTH - name_tag.get_width() - 10, 10))

                    self.btn_left.draw(self.screen)
                    self.btn_right.draw(self.screen)
                    self.btn_jump.draw(self.screen)

            for p in pointers:
                pygame.draw.circle(self.screen, (255, 0, 0), (int(p[0]), int(p[1])), 25, 3)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("20-Mission Platformer")
    game = Game(screen)
    game.run()
