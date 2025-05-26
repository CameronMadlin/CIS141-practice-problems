#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
#For example, water is very effective to fight fire.
#Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
#simple type effectiveness rules. Your solution only needs to work for these three sets of input:

attacker = ""
defender = ""

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        print("Super Effective")
    elif attacker == "Fire" and defender == "Water":
        print("Not Very Effective")
    elif attacker == "Electric" and defender == "Grass":
        print("Neutral")

type_advantage("Water", "Fire") # "Super Effective"
type_advantage("Fire", "Water") # "Not Very Effective"
type_advantage("Electric", "Grass") # "Neutral"
