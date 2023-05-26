class Humidity
{
private:
    int pinCaptor;
    int captorReading;
public:
    Humidity(int pin);
    ~Humidity();
    void setupSoil();

    int humidityLecture();
};