package uc.seng301.petbattler.asg3.model;

import java.util.Objects;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "pet")
public class Pet {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_pet")
    private Long petId;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_pack")
    private Pack pack;

    private String name;
    private int attack;
    private int health;
    private int tier;

    public Pet() {
        // a public constructor is needed by JPA
    }

    public Long getPetId() {
        return petId;
    }

    public void setPetId(Long petId) {
        this.petId = petId;
    }

    public Pack getPack() {
        return pack;
    }

    public void setPack(Pack pack) {
        this.pack = pack;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAttack() {
        return attack;
    }

    public void setAttack(int attack) {
        this.attack = attack;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getTier() {
        return tier;
    }

    public void setTier(int tier) {
        this.tier = tier;
    }

    @Override
    public String toString() {
        return String.format("%s -- Atk: %d Health: %d Tier: %d", name, attack, health, tier);
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Pet)) {
            return false;
        }
        Pet pet = (Pet) o;
        return name.equals(pet.getName()) && pack.getPackId().equals(pet.getPackId());
    }

    @Override
    public int hashCode() {
        return Objects.hash(petId, pack, name, attack, health, tier);
    }

    public Long getPackId() {
        return pack.getPackId();
    }
    public GamePet getGamePet() {
        return new GamePet(name, attack, health);
    }

}
