package uc.seng301.petbattler.lab5.model;

import jakarta.persistence.*;

import java.util.List;

@Entity
@Table(name = " pack")
public class Pack {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_pack")
    private Long packId;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_player")
    private Player player;

    @OneToMany(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_pack")
    private List<Pet> pets;

    private String name;

    public Pack() {
        // a (public) constructor is needed by JPA
    }

    public Long getPackId() {
        return packId;
    }

    public void setPackId(Long packId) {
        this.packId = packId;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Pet> getPets() {
        return pets;
    }

    public void setPets(List<Pet> pets) {
        this.pets = pets;
    }
}