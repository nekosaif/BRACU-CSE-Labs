#include <stdio.h>


int main()
{

    struct Paratha
    {
        int qty;
        int unit_price;
    };


    struct Vegetable
    {
        int qty;
        int unit_price;
    };


    struct MineralWater
    {
        int qty;
        int unit_price;
    };


    struct Paratha paratha;
    struct Vegetable vegetable;
    struct MineralWater mineralWater;

    int numberOfPeople;

    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.qty);

    printf("Unit Price: ");
    scanf("%d", &paratha.unit_price);

    printf("Quantity Of Vegetable: ");
    scanf("%d", &vegetable.qty);

    printf("Unit Price: ");
    scanf("%d", &vegetable.unit_price);

    printf("Quantity Of Mineral Water: ");
    scanf("%d", &mineralWater.qty);

    printf("Unit Price: ");
    scanf("%d", &mineralWater.unit_price);

    printf("Number Of People: ");
    scanf("%d", &numberOfPeople);

    int totalParathaPrice = paratha.qty * paratha.unit_price;
    int totalVegetablePrice = vegetable.qty * vegetable.unit_price;
    int totalMineralWaterPrice = mineralWater.qty * mineralWater.unit_price;

    int totalPrice = totalParathaPrice + totalVegetablePrice + totalMineralWaterPrice;

    float pricePerPerson = totalPrice / numberOfPeople;

    printf("Individual people will pay: %0.2f tk ", pricePerPerson);



    return 0;

}