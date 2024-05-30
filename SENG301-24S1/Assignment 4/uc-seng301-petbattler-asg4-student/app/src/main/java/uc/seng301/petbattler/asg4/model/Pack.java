package uc.seng301.petbattler.asg4.model;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

/**
 * Simple entity class representing pack
 * @author seng301 teaching team
 */
@Entity
@Table(name = "pack")
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

    /**
     * Default Pack constructor for JPA
     */
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

    /**
     * Add given pets to this pack
     * 
     * @param pets an array of pets to add to current pack
     */
    public void addPets(Pet... pets) throws IllegalArgumentException {
        if (!Collections.disjoint(this.pets.stream().map(Pet::getName).toList(), Stream.of(pets).map(Pet::getName).toList())) {
            throw new IllegalArgumentException("At least one of given pets already exists in list");
        }
        this.pets.addAll(Arrays.asList(pets));
    }

    @Override
    public String toString() {
        return "{" +
                " packId='" + getPackId() + "'" +
                ", player='" + getPlayer().getName() + "'" +
                ", pets='" + getPets() + "'" +
                ", name='" + getName() + "'" +
                "}";
    }

}