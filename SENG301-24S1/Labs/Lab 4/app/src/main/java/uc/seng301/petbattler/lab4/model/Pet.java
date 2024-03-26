package uc.seng301.petbattler.lab4.model;

import jakarta.persistence.*;

@Entity
@Table(name = "pet")
public class Pet {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_pet")
    private long petId;
    private String name;
    private int attack;
    private int health;
    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_pack")
    private Pack pack;

    public Pet() {
        // Public Constructor
    }

    public Pet(String name, int attack, int health) {
        // Public Constructor
        this.name = name;
        this.attack = attack;
        this.health = health;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("Pet (%d): %s -- Attack: %d, Health %d%n", petId, name, attack, health));
        return sb.toString();
    }

    public long getPetId() {
        return petId;
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

    public Pack getPack() {
        return pack;
    }

    public void setPetId(long petId) {
        this.petId = petId;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAttack(int attack) {
        this.attack = attack;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public void setPack(Pack pack) {
        this.pack = pack;
    }
}
