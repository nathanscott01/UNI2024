package uc.seng301.petbattler.lab4.model;
import jakarta.persistence.*;
import java.util.List;

//import java.util.List;
@Entity
@Table(name = "player")
public class Player {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_player")
    private long playerId;

    @OneToMany(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_player")
    private List<Pack> packs;

    private String name;

    public Player() {
        // a public constructor is needed
    }

    public Player(List<Pack> packs, String name) {
        this.packs = packs;
        this.name = name;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("Player (%d): %s%n\tPacks:%n", playerId, name));
        for (Pack pack: packs) {
            sb.append(String.format("\t\tPack (%d): %s%n\t\t\tPets:%n", pack.getPackId(), pack.getName()));
            for (Pet pet : pack.getPets()) {
                sb.append(String.format("\t\t\t\tPet (%d): %s -- Attack: %d, Health: %d%n", pet.getPetId(),
                        pet.getName(), pet.getAttack(), pet.getHealth()));
            }
        }
        return sb.toString();
    }

    /** Getters and Setters **/
    /** Generated using IntelliJ generation feature **/

    public long getPlayerId() {
        return playerId;
    }

    public void setPlayerId(long playerId) {
        this.playerId = playerId;
    }

    public List<Pack> getPacks() {
        return packs;
    }

    public void setPacks(List<Pack> packs) {
        this.packs = packs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
