

abstract class Building {
    int health;

    public void damage(int damage) {
        this.health -= damage;
    }

}


class SomeBuilding extends Building {
    public SomeBuilding() {
        health = 20;
    }
}