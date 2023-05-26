class Led
{
private:
    int pinBlueLed;
    int pinGreenLed;
    int pinRedLed;

public:
    Led(int pin1, int pin2, int pin3);
    ~Led();
    void setup();
    void onBlue();
    void onGreen();
    void onRed();
    void offBlue();
    void offGreen();
    void offRed();
};
