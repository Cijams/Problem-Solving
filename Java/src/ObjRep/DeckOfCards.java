package ObjRep;
import java.util.Random;

public class DeckOfCards {
    private static Card[] Deck = new Card[52];

    public enum Types {
        TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,
        JACK, QUEEN, KING, ACE
    }

    public static void main(String[] args) {
        DeckOfCards.buildDeck();
        DeckOfCards.printDeck(Deck);
        DeckOfCards.shuffleDeck(Deck);
        System.out.println();
        DeckOfCards.printDeck(Deck);

        }

    private static void buildDeck() {
        int index = 0;
        for (Types t : Types.values()) {
            Deck[index] = new Card("BLACK", "CLUBS", t + "");
            Deck[index + 1] = new Card("BLACK", "SPADES", t + "");
            Deck[index + 2] = new Card("RED", "HEARTS", t + "");
            Deck[index + 3] = new Card("RED", "DIAMONDS", t + "");
            index += 4;
        }
    }

    private static void printDeck(Card[] d) {
        for (Card c : d)
            printCard(c);
    }

    private static void printCard(Card c) {
        System.out.println(c.getValue() + " " + c.getColor() + " " + c.getSuit());
    }

    private static void shuffleDeck(Card[] d) {
        for(int i = 0; i < 10; i++)
            _shuffle(d);
    }

    private static void _shuffle(Card[] d) {
        Random rand = new Random();
        Card temp;
        int number;
        for(int i = 0; i < 52; i++) {
            temp = d[i];
            number = rand.nextInt(52);
            d[i] = d[number];
            d[number] = temp;
            }
    }
}

class Card {
    private String color;
    private String suit;
    private String value;

    public Card(String color, String suit, String value) {
        this.color = color;
        this.suit = suit;
        this.value = value;
    }

    public String getColor() {
        return color;
    }

    public String getSuit() {
        return suit;
    }

    public String getValue() {
        return value;
    }
}
