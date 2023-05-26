class Steam
{
private:
    int sensorValue;
    int pinCaptor;

public:
    Steam(int pin);
    ~Steam();
    void setupcaptor();

    int steamLecture();
};
