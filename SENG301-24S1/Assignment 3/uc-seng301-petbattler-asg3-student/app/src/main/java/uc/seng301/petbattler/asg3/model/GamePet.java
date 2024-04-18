package uc.seng301.petbattler.asg3.model;

public class GamePet {
    private final String name;
    private int attack;
    private int health;

    public GamePet(String name, int attack, int health) {
        this.name = name;
        this.attack = attack;
        this.health = health;
    }

    public String getName() {
        return name;
    }

    public int getAttack() {
        return attack;
    }

    public int getHealth() {
        return health;
    }

    public void takeDamage(int damageAmount) {
        health -= damageAmount;
    }

    public void heal(int healAmount) {
        health += healAmount;
    }

    public void buffAttack(int buffAmount) {
        attack += buffAmount;
    }

    public void debuffAttack(int debuffAmount) {
        attack -= debuffAmount;
    }
}
