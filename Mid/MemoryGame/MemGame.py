import pygame
import random
import os

# Configuration
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
GRID_SIZE = 4
CARD_SIZE = 120
MARGIN = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_BLUE = (20, 20, 50)
GOLD = (255, 215, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

class Card:
    def __init__(self, x, y, image, img_id):
        self.rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
        self.image = image
        self.img_id = img_id
        self.is_flipped = False
        self.is_matched = False

    def draw(self, screen):
        if self.is_matched:
            pygame.draw.rect(screen, GREEN, self.rect)
            screen.blit(self.image, self.rect)
        elif self.is_flipped:
            pygame.draw.rect(screen, WHITE, self.rect)
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, DARK_BLUE, self.rect)
            pygame.draw.rect(screen, WHITE, self.rect, 2)

class MemoryGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Memory Game - Pygame Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 32)
        self.large_font = pygame.font.SysFont("Arial", 64, bold=True)
        
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.best_score_file = os.path.join(self.path, ".best_score")
        self.best_score = self.load_best_score()
        
        self.reset_game()

    def load_best_score(self):
        try:
            with open(self.best_score_file, "r") as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return None

    def save_best_score(self):
        if self.best_score is None or self.moves < self.best_score:
            self.best_score = self.moves
            with open(self.best_score_file, "w") as f:
                f.write(str(self.best_score))

    def load_images(self):
        valid_extensions = [".jpg", ".gif", ".png", ".tga"]
        all_imgs = []
        for f in os.listdir(self.path):
            if any(f.lower().endswith(ext) for ext in valid_extensions):
                img = pygame.image.load(os.path.join(self.path, f))
                img = pygame.transform.scale(img, (CARD_SIZE, CARD_SIZE))
                all_imgs.append((img, f))
        
        needed = (GRID_SIZE * GRID_SIZE) // 2
        while len(all_imgs) < needed:
            surf = pygame.Surface((CARD_SIZE, CARD_SIZE))
            surf.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            all_imgs.append((surf, f"fallback_{len(all_imgs)}"))
            
        selected = random.sample(all_imgs, needed)
        pairs = selected + selected
        random.shuffle(pairs)
        return pairs

    def reset_game(self):
        self.moves = 0
        self.pairs_found = 0
        self.flipped_cards = []
        self.waiting = False
        self.wait_timer = 0
        self.game_over = False
        
        images = self.load_images()
        self.cards = []
        start_x = (SCREEN_WIDTH - (GRID_SIZE * (CARD_SIZE + MARGIN))) // 2
        start_y = 100
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                img, img_id = images.pop()
                x = start_x + j * (CARD_SIZE + MARGIN)
                y = start_y + i * (CARD_SIZE + MARGIN)
                self.cards.append(Card(x, y, img, img_id))

    def handle_click(self, pos):
        if self.waiting or self.game_over:
            return
            
        for card in self.cards:
            if card.rect.collidepoint(pos) and not card.is_flipped and not card.is_matched:
                card.is_flipped = True
                self.flipped_cards.append(card)
                
                if len(self.flipped_cards) == 2:
                    self.moves += 1
                    self.waiting = True
                    self.wait_timer = pygame.time.get_ticks()
                break

    def update(self):
        if self.waiting:
            current_time = pygame.time.get_ticks()
            if current_time - self.wait_timer > 600:
                c1, c2 = self.flipped_cards
                if c1.img_id == c2.img_id:
                    c1.is_matched = True
                    c2.is_matched = True
                    self.pairs_found += 1
                    if self.pairs_found == (GRID_SIZE * GRID_SIZE) // 2:
                        self.game_over = True
                        self.save_best_score()
                else:
                    c1.is_flipped = False
                    c2.is_flipped = False
                
                self.flipped_cards = []
                self.waiting = False

    def draw(self):
        self.screen.fill(GRAY)
        
        # UI
        moves_surf = self.font.render(f"Moves: {self.moves}", True, WHITE)
        self.screen.blit(moves_surf, (20, 20))
        
        best = self.best_score if self.best_score else "--"
        best_surf = self.font.render(f"Best: {best}", True, GOLD)
        self.screen.blit(best_surf, (SCREEN_WIDTH - 150, 20))
        
        for card in self.cards:
            card.draw(self.screen)
            
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0,0))
            win_surf = self.large_font.render("YOU WIN!", True, GOLD)
            rect = win_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            self.screen.blit(win_surf, rect)
            
            hint_surf = self.font.render("Press R to Restart", True, WHITE)
            hint_rect = hint_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            self.screen.blit(hint_surf, hint_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
            
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = MemoryGame()
    game.run()
