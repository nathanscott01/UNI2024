package uc.seng301.petbattler.asg4.pets;

import java.io.File;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import uc.seng301.petbattler.asg4.model.Pet;

/**
 * Pet API fetching functionality, makes use of {@link PetResponse} and Jackson
 * lib to map the returned JSON to a pet
 * @author seng301 teaching team
 */
public class PetService implements PetGenerator {
    private static final Logger LOGGER = LogManager.getLogger(PetService.class);
    private static final String CARD_URL = "https://tile.csse.canterbury.ac.nz/sap/api/v2/pets/";
    public static final int NUM_PETS = 81;
    private final ObjectMapper objectMapper = new ObjectMapper()
            .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    private final Random random;

    /**
     * Create a new pet service
     */
    public PetService() {
        random = new Random();
    }

    @Override
    public Pet getRandomPet() {
        int randomId = random.nextInt(NUM_PETS) + 1;
        String apiResponse = getResponseFromAPI(randomId);
        if (apiResponse != null && !apiResponse.isEmpty()) {
            PetResponse petResponse = parseResponse(apiResponse);
            if (petResponse != null) {
                return petResponse.toPet();
            }
        }
        return getOfflineResponse().toPet();
    }

    /**
     * Gets the response from the API
     * 
     * @return The response body of the request as a String
     */
    public String getResponseFromAPI(int petId) {
        String data = null;
        try {
            LOGGER.info("Fetching pet with id: {}", petId);
            URL url = new URL(CARD_URL + petId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();

            int responseCode = connection.getResponseCode();
            LOGGER.info("Api responded with status code: {}", responseCode);

            if (responseCode == 200) {
                Scanner scanner = new Scanner(url.openStream());
                StringBuilder stringResult = new StringBuilder();
                while (scanner.hasNext()) {
                    stringResult.append(scanner.nextLine());
                }
                data = stringResult.toString();
                scanner.close();
            } else {
                LOGGER.error("unable to process request to API, response code is '{}'", responseCode);
            }
        } catch (IOException e) {
            LOGGER.error("Error parsing API response", e);
        }
        return data;
    }

    /**
     * Parse the json response to a {@link PetResponse} object using Jackson
     * 
     * @param stringResult String representation of response body (JSON)
     * @return CardResponse decoded from string
     */
    private PetResponse parseResponse(String stringResult) {
        PetResponse petResponse = null;
        try {
            LOGGER.info(stringResult);
            petResponse = objectMapper.readValue(stringResult, PetResponse.class);
        } catch (JsonProcessingException e) {
            LOGGER.error("Error parsing API response", e);
        }
        return petResponse;
    }

    /**
     * Loads pet response from a text file if there is an issue with the API (e.g.
     * there is no internet connection, or the API is down)
     * If there is an error loading pets from this file the application will exit as
     * the state will be unusable
     *
     * @return {@link PetResponse} object with values manually assigned to those
     *         loaded from a file
     */
    private PetResponse getOfflineResponse() {
        LOGGER.warn("Falling back to offline pets");
        List<PetResponse> petResponse = null;
        try {
            petResponse = objectMapper.readValue(
                    new File(getClass().getClassLoader().getResource("all_pets.json").toURI()), new TypeReference<>() {
                    });
        } catch (URISyntaxException | IOException| NullPointerException e) {
            LOGGER.fatal("ERROR parsing offline data, app is now exiting as no further functionality wil work", e);
            System.exit(1);
        }
        return petResponse.get(random.nextInt(petResponse.size()));
    }

}
