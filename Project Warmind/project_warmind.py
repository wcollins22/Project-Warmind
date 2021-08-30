from dataclasses import dataclass
import random
from random import choice
import pickle

@dataclass
class Player:
    name: str
    max_health: int
    health: int
    max_mana: int
    mana: int
    p_class: str
    level: int
    xp: int
    curr_weapon: str
    health_potion: int
    mana_potion: int
    chest1 = False
    mag_circle = False
    crate = False

sword_skills = ["Vertical Arc", "Howling Octave", "Deadly Sins"]
spells = ["Fireball", "Lunar Tempest", "Soul Rain"]
inventory = ["Rusted Sword"]
area = "Entrance"

entrance_info = "\nThe entrance to The Abandoned Delves, the only light comes from the outside and a few lit torches from previous adventurers. The people at the town said that a group of people had dug this place up and never came back. You can go into the [Corridor] from here."

corridor_info = "\nAs you enter the corridor, the musty smell of the dungeon hits you hard. From the little light from torches, you can see that moss is growing to the stone walls. You can go to an [Armory], [Dim Room], or a [Mossy Room], or back to the [Entrance]."

armory_info = "\nAs you walk into the Armory, you realize one thing. Aside from the old weapons on the wall, there is only one important object in the room, a chest. You can interact with the [Chest] or go back to the [Corridor]."

armory_alt_info = "\nA room that had a chest in it that you have already opened. You can go back to the [Corridor]."

dim_info = "\nThe room is dimly lit and a bit spacious. As you look around, you see that there are about a total of three torches keeping the room lit. With this amount of darkness, you keep mind that you will need to be careful. You can go back to the [Corridor] or to a [Oddly Lit Room]"

odd_info = "\nYou walk into the room and see why it had an oddly lit color. The room is lit up by a magic circle on the floor, with books nearby. You can interact with the [Magic Circle] or go back to the [Dim Room]"

odd_alt_info = "\nYou have already figured out why the room is oddly lit. Stepping around the books, you can go back to the [Dim Room]."

mossy_info = "\nThe room is covered in wet moss. Looking up, you see that water is dripping from the cracks of the stone ceiling. You assume that the room is under some form of water that. You can go back to the [Corridor], a [Flooded Room], or a [Bright Room]."

flooded_info = "\nYou walk into the flooded room and realize that the water is about ankle deep. Thankfully, previous adventures hung up lanterns so water won't put the light out. Trudging through the flooded room, you can go to a [Storage Room], [Arena] or back to the [Mossy Room]."

bright_info = "\nYou walk into the mysterious bright room. Looking in, you see that there is a fountain spewing out water. You can interact with the [Water] or go back to the [Mossy Room]."

storage_info = "\nThe storage room is somewhat wet from the water that came from the flooded room. Despite that, the room seems to be in good condition. All but one crate is opened. You can open the [Crate] or go back to the [Flooded Room]."

storage_alt_info = "\nYou have already opened the big crate in the somewhat wet room. You can go back to the [Flooded Room]"

arena_info = "You defeated the ogre, but monsters will still remain. But the won't be as coordinated. The villagers can continue living in peace. You can go back to the [Flooded Room]."


def char_create(player: Player) -> None:
    print("Please create your character.")
    player.name = input("Name: ").title()
    while True:
        player.p_class = input("Pick Mage or Knight: ").title()
        if player.p_class == "Mage" or player.p_class == "Knight":
            break
        else:
            print("That is an invalid class!")


def print_Info(player: Player, location: str) -> None:
    print(f"You are in {location}")
    if location == "Entrance":
        print(entrance_info)
    elif location == "Corridor":
        print(corridor_info)
    elif location == "Armory":
        if player.chest1 == True:
            print(armory_alt_info)
        else:
            print(armory_info)
    elif location == "Dim Room":
        print(dim_info)
    elif location == "Oddly Lit Room":
        if player.mag_circle == True:
            print(odd_alt_info)
        else:
            print(odd_info)
    elif location == "Mossy Room":
        print(mossy_info)
    elif location == "Bright Room":
        print(bright_info)
    elif location == "Flooded Room":
        print(flooded_info)
    elif location == "Storage Room":
        if player.crate == False:
            print(storage_info)
        else:
            print(storage_alt_info)
    elif location == "Arena":
        print(arena_info)

def invalid_destination(location: str, destination: str) -> str:
    return f"You cannot go to {destination} from {location}."

def transition(player: Player, location: str, destination: str) -> bool:
    if location == "Entrance":
        return destination == "Corridor"
    elif location == "Corridor":
        return destination == "Entrance" or destination == "Armory" or destination == "Dim Room" or destination == "Mossy Room"
    elif location == "Armory":
        if player.chest1 == False:
            return destination == "Chest" or destination == "Corridor"
        else:
            return destination == "Corridor"
    elif location == "Chest":
        return destination == "Corridor"
    elif location == "Dim Room":
        return destination == "Corridor" or destination == "Oddly Lit Room"
    elif location == "Oddly Lit Room":
        if player.mag_circle == False:
            return destination == "Magic Circle" or destination == "Dim Room"
        else:
            return destination == "Dim Room"
    elif location == "Magic Circle":
        return destination == "Dim Room"
    elif location == "Mossy Room":
        return destination == "Bright Room" or destination == "Corridor" or destination == "Flooded Room"
    elif location == "Bright Room":
        return destination == "Water" or destination == "Mossy Room"
    elif location == "Water":
        return destination == "Mossy Room"
    elif location == "Flooded Room":
        return destination == "Mossy Room" or destination == "Storage Room" or destination == "Arena"
    elif location == "Storage Room":
        if player.crate == False:
            return destination == "Crate" or destination == "Flooded Room"
        else:
            return destination == "Flooded Room"
    elif location == "Arena":
        return destination == "Flooded Room"
    elif location == "Inventory":
        return destination == "Entrance"
    elif location == "Save":
        return destination == "Entrance"
    elif location == "Load":
        return destination == "Entrance"
    else:
        return False


def input_destination_or_q(player: Player, location: str) -> str:
    while True:
        print("What would you like to do? [Q to quit]")
        destination = input("> ").title()
        if destination == "Q" or destination == "Inventory" or destination == "Save" or destination == "Load" or destination == "Potion" or transition(player, location, destination):
            return destination




@dataclass
class Slime:
    health: int


@dataclass
class Goblin:
    health: int

@dataclass
class Ogre:
  health: int


def random_monster() -> int:
    monster = random.randint(1, 2)
    return monster


def random_encounter() -> bool:
    encounter = random.randint(1, 5)
    if encounter == 1 or encounter == 2:
        return True
    else:
        return False


def is_player_dead(player: Player) -> bool:
    if player.health > 0:
        return False
    else:
        return True


def is_combat_over(slime: Slime, goblin: Goblin) -> bool:
    if slime.health < 1 or goblin.health < 1:
        return True
    else:
        return False


def print_player_stats(player: Player) -> str:
    return f"{player.name}:\nHealth: {player.health}\nMana: {player.mana}\nLevel: {player.level}"

def sword_skill_input() -> str:
  skill = input("Which sword skill would you like to use? ").title()
  return skill

def spell_input() -> str:
    spell = input("What spell do you want to cast? >").title()
    return spell

def mage_slime_combat(player: Player, slime: Slime, slime_choice: str) -> None:
    slime_moves = ["Slosh", "Predator", "Gloopy Trail"]
    slime_choice = choice(slime_moves)
    if slime.health > 0:
        move = input("\nDo you want to [Attack], use a [Spell], or use a [Potion]? ").title()
        if move == "Spell" and player.mana <= 4:
            print("\nYou have no mana and failed to attack!")
        elif move == "Spell":
            print(spells)
            spell = spell_input()
            if spell == "Fireball" and player.mana >= 5:
              player_damage = random.randint(5,12)
              slime.health -= player_damage
              player.mana -= 5
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Fireball" and player.mana < 5:
              print("\nNot enough mana. You fail to attack.")
            elif spell == "Lunar Tempest" and player.mana >= 10:
              player_damage = random.randint(12,20)
              slime.health -= player_damage
              player.mana -= 10
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Lunar Tempest" and player.mana < 10:
              print("\nNot enough mana. You fail to attack.")
            elif spell == "Soul Rain" and player.mana >= 15:
              player_damage = random.randint(20, 30)
              slime.health -= player_damage
              player.mana -= 15
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Soul Rain" and player.mana < 15:
              print("\nNot enough mana. You fail to attack.")
            elif spell == "Moonlight Wrath"  and player.mana >= 35:
                player_damage = random.randint(30, 45)
                slime.health -= player_damage
                player.mana -= 35
                print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Moonlight Wrath" and player.mana < 35:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"\nYou used {move}, it does {player_damage} damage.")
            slime.health -= player_damage
        elif move == "Potion":
          use_potion(player)
        enemy_damage = random.randint(1, 8)
        print(f"\nIt is now the slime's turn.\nThe slime attacks using {slime_choice}. It does {enemy_damage} damage.")
        player.health = player.health - enemy_damage
        print(f"Slime: {slime.health} hp")
        print(f"{player.name}: {player.health} hp")
        print(f"{player.name}: {player.mana} mana")


def mage_goblin_combat(player: Player, goblin: Goblin, goblin_choice: str) -> None:
    goblin_moves = ["Screech", "Ambush", "Poke"]
    goblin_choice = choice(goblin_moves)
    if goblin.health > 0:
        move = input("\nDo you want to [Attack], use a [Spell], or use a [Potion]? ").title()
        if move == "Spell" and player.mana <= 4:
            print("\nYou have no mana and failed to attack!")
        elif move == "Spell":
          print(spells)
          spell = spell_input()
          if spell == "Fireball" and player.mana >= 5:
            player_damage = random.randint(5,12)
            goblin.health -= player_damage
            player.mana -= 5
            print(f"You used {spell}, it does {player_damage} damage.")
          elif spell == "Fireball" and player.mana < 5:
              print("\nNot enough mana. You fail to attack.")
          elif spell == "Lunar Tempest" and player.mana >= 10:
            player_damage = random.randint(12,20)
            print(f"You used {spell}, it does {player_damage} damage.")
            goblin.health -= player_damage
            player.mana -= 10
          elif spell == "Lunar Tempest" and player.mana < 10:
              print("\nNot enough mana. You fail to attack.")
          elif spell == "Soul Rain" and player.mana >= 15:
            player_damage = random.randint(20,30)
            goblin.health -= player_damage
            player.mana -= 15
            print(f"You used {spell}, it does {player_damage} damage.")
          elif spell == "Soul Rain" and player.mana < 15:
              print("\nNot enough mana. You fail to attack.")
          elif spell == "Moonlight Wrath" and player.mana >= 35:
            player_damage = random.randint(30,45)
            goblin.health -= player_damage
            player.mana -= 35
            print(f"You used {spell}, it does {player_damage} damage.")
          elif spell == "Moonlight Wrath" and player.mana < 35:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"You used {move}, it does {player_damage} damage.")
            goblin.health -= player_damage
        elif move == "Potion":
            use_potion(player)
    enemy_damage = random.randint(1, 8)
    print(f"\nIt is now the goblin's turn.\nThe goblin attacks using {goblin_choice}. It does {enemy_damage} damage.")
    player.health = player.health - enemy_damage
    print(f"Goblin: {goblin.health} hp")
    print(f"{player.name}: {player.health} hp")
    print(f"{player.name}: {player.mana} mana")


def knight_goblin_combat(player: Player, goblin: Goblin, goblin_choice: str) -> None:
    goblin_moves = ["Screech", "Ambush", "Poke"]
    goblin_choice = choice(goblin_moves)
    if goblin.health > 0:
        move = input("\nDo you want to [Attack], use a [Sword Skill], or use a [Potion]? ").title()
        if move == "Sword Skill" and player.mana <= 4:
            print("\nYou have no mana and failed to attack!")
        elif move == "Sword Skill":
            print(sword_skills)
            skill = sword_skill_input()
            if skill == "Vertical Arc"  and player.mana >= 5and player.mana >= 5:
              player_damage = random.randint(5,12)
              goblin.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 5
            elif skill == "Vertical Arc" and player.mana < 5:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Howling Octave" and player.mana >= 10:
              player_damage = random.randint(10,20)
              goblin.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 10
            elif skill == "Howling Octave" and player.mana < 10:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Deadly Sins" and player.mana >= 15:
              player_damage = random.randint(20,30)
              goblin.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 15
            elif skill == "Deadly Sins" and player.mana < 15:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"You used {move}, it does {player_damage} damage.")
            goblin.health -= player_damage
        elif move == "Potion":
            use_potion(player)
        enemy_damage = random.randint(1, 8)
        print(f"\nIt is now the goblin's turn.\nThe goblin attacks using {goblin_choice}. It does {enemy_damage} damage.")
        player.health = player.health - enemy_damage
        print(f"Goblin: {goblin.health} hp")
        print(f"{player.name}: {player.health} hp")
        print(f"{player.name}: {player.mana} mana")


def knight_slime_combat(player: Player, slime: Slime,
                        slime_choice: str) -> None:
    slime_moves = ["Slosh", "Predator", "Gloopy Trail"]
    slime_choice = choice(slime_moves)
    if slime.health > 0:
        move = input("\nDo you want to [Attack], use a [Sword Skill] or use a [Potion]? ").title()
        if move == "Sword Skill" and player.mana <= 4:
            print("You have no mana and failed to attack!")
        elif move == "Sword Skill":
            print(sword_skills)
            skill = sword_skill_input()
            if skill == "Vertical Arc" and player.mana >= 5:
              player_damage = random.randint(5,12)
              slime.health -= player_damage
              print(f"\nYou used {skill}, it does {player_damage} damage.")
              player.mana -= 5
            elif skill == "Vertical Arc" and player.mana < 5:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Howling Octave" and player.mana >= 10:
              player_damage = random.randint(10, 20)
              slime.health -= player_damage
              print(f"\nYou used {skill}, it does {player_damage} damage.")
              player.mana -= 10
            elif skill == "Howling Octave" and player.mana < 10:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Deadly Sins" and player.mana >= 15:
              player_damage = random.randint(20, 30)
              slime.health -= player_damage
              print(f"\nYou used {skill}, it does {player_damage} damage.")
              player.mana -= 15
            elif skill == "\nDeadly Sins" and player.mana < 15:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"\nYou used {move}, it does {player_damage} damage.")
            slime.health -= player_damage
        elif move == "Potion":
            use_potion(player)
        enemy_damage = random.randint(1, 8)
        print(f"\nIt is now the slime's turn.\nThe slime attacks using {slime_choice}. It does {enemy_damage} damage.")
        player.health = player.health - enemy_damage
        print(f"Slime: {slime.health} hp")
        print(f"{player.name}: {player.health} hp")
        print(f"{player.name}: {player.mana} mana")

def boss_mage(player: Player, ogre: Ogre, ogre_choice: str) -> None:
    ogre_moves = ["Smash", "Roar", "Slap"]
    ogre_choice = choice(ogre_moves)
    if ogre.health > 0:
        move = input("\nDo you want to [Attack], use a [Spell], or use a [Potion]? ").title()
        if move == "Spell" and player.mana <= 4:
            print("You have no mana and failed to attack!")
        elif move == "Spell":
            print(spells)
            spell = spell_input()
            if spell == "Fireball" and player.mana >= 5:
              player_damage = random.randint(5,12)
              ogre.health -= player_damage
              player.mana -= 5
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Fireball" and player.mana == 5:
              print("\nNot enough mana. You fail to attack.")
            elif spell == "Lunar Tempest" and player.mana >= 10:
              player_damage = random.randint(12,20)
              ogre.health -= player_damage
              player.mana -= 10
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Lunar Tempest" and player.mana == 10:
              print("\nNot enough mana. You fail to attack.")
            elif spell == "Soul Rain" and player.mana >= 15:
              player_damage = random.randint(20, 30)
              ogre.health -= player_damage
              player.mana -= 15
              print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Soul Rain" and player.mana < 15:
              print("\nNot enough mana. You fail to attack")
            elif spell == "Moonlight Wrath" and player.mana >= 35:
                player_damage = random.randint(30, 45)
                ogre.health -= player_damage
                player.mana -= 35
                print(f"You used {spell}, it does {player_damage} damage.")
            elif spell == "Moonlight Wrath" and player.mana < 35:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"You used {move}, it does {player_damage} damage.")
            ogre.health -= player_damage 
        elif move == "Potion":
            use_potion(player)
        enemy_damage = random.randint(15, 25)
        print(f"\nIt is now the ogre's turn.\nThe ogre attacks using {ogre_choice}. It does {enemy_damage} damage.")
        player.health = player.health - enemy_damage
        print(f"Ogre: {ogre.health} hp")
        print(f"{player.name}: {player.health} hp")
        print(f"{player.name}: {player.mana} mana")

def boss_knight(player: Player, ogre: Ogre, ogre_choice: str) -> None:
    ogre_moves = ["Smash", "Roar", "Slap"]
    ogre_choice = choice(ogre_moves)
    if ogre.health > 0:
        move = input("\nDo you want to [Attack], use a [Sword Skill], or use a [Potion]? ").title()
        if move == "Sword Skill" and player.mana <= 4:
          print("You have no mana. You fail to attack.")
        elif move == "Sword Skill":
            print(sword_skills)
            skill = sword_skill_input()
            if skill == "Vertical Arc" and player.mana >= 5:
              player_damage = random.randint(5,12)
              ogre.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 5
            elif skill == "Vertical Arc" and player.mana < 5:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Howling Octave" and player.mana >= 10:
              player_damage = random.randint(10, 20)
              ogre.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 10
            elif skill == "Howling Octave" and player.mana < 10:
              print("\nNot enough mana. You fail to attack.")
            elif skill == "Deadly Sins" and player.mana >= 15:
              player_damage = random.randint(20, 30)
              ogre.health -= player_damage
              print(f"You used {skill}, it does {player_damage} damage.")
              player.mana -= 15
            elif skill == "Deadly Sins" and player.mana < 15:
              print("\nNot enough mana. You fail to attack.")
        elif move == "Attack":
            if player.curr_weapon == "Rusted Sword":
                player_damage = random.randint(5, 10)
            elif player.curr_weapon == "Short Sword":
                player_damage = random.randint(10,18)
            elif player.curr_weapon == "Claymore":
                player_damage = random.randint(18,25)
            print(f"You used {move}, it does {player_damage} damage.")
            ogre.health -= player_damage
        elif move == "Potion":
          use_potion(player)
        enemy_damage = random.randint(15, 25)
        print(f"\nIt is now the ogre's turn.\nThe ogre attacks using {ogre_choice}. It does {enemy_damage} damage.")
        player.health = player.health - enemy_damage
        print(f"ogre: {ogre.health} hp")
        print(f"{player.name}: {player.health} hp")
        print(f"{player.name}: {player.mana} mana")

def add_xp(player: Player) -> None:
  player.xp += 20

def level_up(player: Player) -> None:
  add_xp(player)
  if player.level == 1:
    if player.xp >= 15:
      player.level = 2
      player.xp = 0
  elif player.level == 2:
    if player.xp >= 30:
      player.level = 3
      player.xp = 0
      
def use_potion(player: Player) -> None:
    print("\nDo you want to use a [Health Potion] or [Mana Potion]?")
    action = input("> ").title()
    if player.health_potion == 0 and player.mana_potion == 0:
      print("You have no potions.")
    elif action == "Health Potion":
        print("You drink a health potion, and recovered 30 health!")
        player.health += 30
        player.health_potion -= 1
    elif action == "Mana Potion":
        print("You drink a mana potion, and recovered 30 mana!")
        player.mana += 30
        player.mana_potion -= 1
      
def level_up_stats(player: Player) -> None:
  add_xp(player)
  level_up(player)
  if player.level == 2:
    player.max_health = 125
    player.max_mana = 125
  elif player.level == 3:
    player.max_health = 150
    player.max_mana = 150
  print("You have leveled up!\nMax health and Max mana both increase.")


def use_inventory(player: Player) -> None:
        print("\nThis is your inventory.")
        print(f"Health Potion: {player.health_potion}")
        print(f"Mana Potions: {player.mana_potion}")
        for item in inventory:
            print(item)
        print(f"You are currently using a {player.curr_weapon}")
        action = input("Do you want to [Equip] or go [Back]? ").title()
        if action == "Equip":
            equip = input("What do you want to equip? ")
            if equip in inventory:
                    player.curr_weapon = equip
            elif equip == player.curr_weapon:
                    print("You are already using this weapon.")
            else:
                    print("You do not have this item.")
        elif action == "Back":
            return
        else:
                print("Not Valid")


def combat_func(player: Player,slime_choice: str, goblin_choice: str) -> None:
      slime = Slime(70)
      goblin = Goblin(70)
      monster = random_monster()
      while not is_combat_over(slime, goblin):
          if player.p_class == "Mage":
              if monster == 1:
                  print("You are fighting a slime.")
                  mage_slime_combat(player, slime, slime_choice)
                  if is_player_dead(player):
                      print("You have died. GAME OVER\n")
                      break
              elif monster == 2:
                  print("You are fighting a goblin.")
                  mage_goblin_combat(player, goblin, goblin_choice)
                  if is_player_dead(player):
                      print("You have died. GAME OVER\n")
                      break
          if player.p_class == "Knight":
              if monster == 1:
                  print("You are fighting a slime.")
                  knight_slime_combat(player, slime, slime_choice)
                  if is_player_dead(player):
                      print("You have died. GAME OVER\n")
                      break
              elif monster == 2:
                  print("You are fighting a goblin.")
                  knight_goblin_combat(player, goblin, goblin_choice)
                  if is_player_dead(player):
                      print("You have died. GAME OVER\n")
                      break
          if is_combat_over(slime, goblin):
            add_potion(player)
            level_up_stats(player)
            print(f"\n{player.name} stats\nHealth: {player.health}\nMana: {player.mana}\nLevel: {player.level}")
            print("You have defeated the monster.")

def is_fight_over(ogre: Ogre) -> bool:
  if ogre.health < 1:
    return True
  else:
    return False
              
def boss_fight(player: Player, ogre_choice: str) -> None:
  ogre = Ogre(150)
  print("You are fighting the boss.")
  while not is_fight_over(ogre):
    if player.p_class == "Mage":
      boss_mage(player, ogre, ogre_choice)
      if is_player_dead(player):
        print("You have DIED. GAME OVER")
        break
    elif player.p_class == "Knight":
      boss_knight(player, ogre, ogre_choice)
      if is_player_dead(player):
        print("You have DIED. GAME OVER")
        break
    if is_fight_over(ogre):
      print("You have defeated the boss. GOOD JOB")

def drop_chance() -> bool:
  chance = random.randint(1, 5)
  if chance == 1 or chance == 2:
    return True
  else:
    return False

def potion_dropped() -> str:
  if drop_chance:
    potion = random.randint(1, 2)
    if potion == 1:
      potion = "Health Potion"
      print("\nYou got a health potion!")
    elif potion == 2:
      potion = "Mana Potion"
      print("\nYou got a mana potion!")
    return potion
  
def add_potion(player: Player) -> None:
  potion = potion_dropped()
  if potion == "Health Potion":
    player.health_potion += 1
  elif potion == "Mana Potion":
    player.mana_potion += 1
  
def save(player: Player) -> None:
    with open('save.pickle', 'wb') as f:
                pickle.dump(player, f)
                f.close()



def main():
    try:
        with open('save.pickle', 'rb') as f:
                player = pickle.load(f)
                f.close()
    except FileNotFoundError:
        player = Player("", 100, 100, 100, 100, "", 1, 0, "Rusted Sword", 0, 0)
        char_create(player)
    goblin_moves = ["Move1", "Move2", "Move 3"]
    goblin_choice = choice(goblin_moves)
    slime_moves = ["Move1", "Move2", "Move 3"]
    slime_choice = choice(slime_moves)
    ogre_moves = ["Smash", "Roar", "Slap"]
    ogre_choice = choice(ogre_moves)
    
    location = area
    while True:
        if is_player_dead(player):
            break
        print_Info(player, location)
        print("\nIf you want to see your inventory, type [Inventory]. If you want to use a potion, type [Potion].")
        destination = input_destination_or_q(player, location)
        if destination == "Save":
            save(player)
        if destination == "Arena":
            boss_fight(player, ogre_choice)
        if destination != "Inventory":
            if random_encounter():
                combat_func(player,slime_choice, goblin_choice)
            if is_player_dead(player):
                 break
        if destination == "Q":
            break
        elif destination == "Inventory":
            use_inventory(player)
        elif destination == "Potion":
            use_potion(player)
        elif location == "Armory" and destination == "Chest" and player.chest1 == False:
            player.chest1 = True
            print("\nYou got a Short Sword")
            inventory.append("Short Sword")
        elif location == "Oddly Lit Room" and destination == "Magic Circle" and player.mag_circle == False:
            if player.p_class == "Mage":
                print(
                    "\nYou find out that the monsters are using this to turn people into monsters. Looking through the nearby books, you learn a new spell!"
                )
                spells.append("Moonlight Wrath")
                player.mag_circle = True
            else:
                print(
                    "\nYou look at the magic circle not knowing what it does. If you were a mage, you might possibly know."
                )
        elif location == "Bright Room" and destination == "Water":
            print("\nAll health and mana have been restored!")
            player.health = player.max_health
            player.mana = player.max_mana
        elif location == "Storage Room" and destination == "Crate" and player.crate == False:
            if player.p_class == "Knight":
                print("\nYou got a Claymore!")
                inventory.append("Claymore")
                player.crate = True
            else:
                print(
                    "\nYou are not strong enough to pick up the Claymore. You might be able to if you were a Knight."
              )
        else:
          location = destination
        

if __name__ == "__main__":
    main()
