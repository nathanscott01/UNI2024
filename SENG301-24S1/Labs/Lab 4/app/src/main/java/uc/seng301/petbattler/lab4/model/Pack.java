package uc.seng301.petbattler.lab4.model;

import jakarta.persistence.*;

import java.util.List;

@Entity
@Table(name = "pack")
public class Pack {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_pack")
    private long packId;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_player")
    private Player player;
    private String name;

    @OneToMany(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_pack")
    private List<Pet> pets;

    public Pack() {
        // Public Constructor
    }

    public Pack(String name, List<Pet> pets) {
        this.name = name;
        this.pets = pets;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("Pack (%d): %s%n\tPets:%n", packId, name));
        for (Pet pet : pets) {
            sb.append(String.format("\t\tPet (%d): %s -- Attack: %d, Health: %d%n", pet.getPetId(),
                    pet.getName(), pet.getAttack(), pet.getHealth()));
        }
        return sb.toString();
    }

    public long getPackId() {
        return packId;
    }

    public String getName() {
        return name;
    }

    public Player getPlayer() {
        return player;
    }

    public List<Pet> getPets() {
        return pets;
    }

    public void setPackId(long packId) {
        this.packId = packId;
    }

    public void setPlayer (Player player) {
        this.player = player;
    }

    public void setName (String name) {
        this.name = name;
    }

    public void setPets (List<Pet> pets) {
        this.pets = pets;
    }
}