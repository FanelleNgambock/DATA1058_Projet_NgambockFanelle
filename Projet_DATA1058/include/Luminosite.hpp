class Luminosite
{
private:
    int pinCaptor;
    int lumValue;
public:
    Luminosite(int pin);
    ~Luminosite();
    void setup();
    int detection();
};

