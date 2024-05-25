#include <DHT.h>

#define DHTPIN 14     // Pinul la care este conectat senzorul DHT22
#define DHTTYPE DHT22 // Specificăm tipul de senzor DHT (DHT22 sau DHT11)
#define MQ135_PIN A0 // Pinul analogic la care este conectat senzorul MQ135

float loga10(float x) {
  return log(x) / log(10);
}
int mapToPPM(float tensiune) {
  return map(tensiune, 0, 5, 0, 300);   // Intervalul 0-2.2V mapează la 0-300 PPM
}

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("Citire senzor DHT22:");
  dht.begin();
  Serial.println("Citire senzor MQ135:");
}
//Metodologia calcului de PPM de toluen
//y1 = Rs/R0 = 0.32 pt (x1) 100 ppm
//y2 = Rs/R0 = 0.11 pt (x2) 1000 ppm
//k = lg(0.32/0/11) / lg (100/1000)= −0.464
//m = lg(0.32) - (-0.464)lg(100) = 0.433

void loop() {
  delay(2000); // Pauză de 2 secunde între citiri

  int valoareSenzor = analogRead(MQ135_PIN);
  float valoareTensiuneRL = float(analogRead(MQ135_PIN)*0.001220703125);
  //Serial.print(valoareTensiuneRL);
  //Serial.print(",");
  float ppm = 0.00;
  //relatia liniara a concentratiei ppm de gaze = slope * (Rs/Ro + intercept)
  float m = 0.433;
  float R0 = 100;
  float Rload = 4700;
  float x1=100;
  float x2 = 1000;
  float y1 = 0.32;
  float y2 = 0.11;
  float k = 0.433;
  //calculam Rs (Valpha este 2703 deoarece am conectat senzorul la 3.3 si la adc 12 biti valoarea maxima poate fi 2703)
  float Rs = (Rload *0.01) * ((valoareSenzor*0.00037) - 1);
  //Calculam Concentratia ppm
  float exponent = 2.31 * (loga10(Rs) - m);
  int C = pow(10,exponent);
  //Serial.print("C:");
  //Serial.print(C);
  //Serial.print(",");
  // Citim temperatura și umiditatea
  float temperatura = dht.readTemperature(); // Citire temperatura în grade Celsius
  float umiditate = dht.readHumidity();       // Citire umiditatea relativă în procente


  
  if (float(valoareTensiuneRL) <= 2.2) {
    ppm = map(float(valoareTensiuneRL), 0, 2.2, 0, 30)*10;

  } else if (float(valoareTensiuneRL) <= 3 && float(valoareTensiuneRL) > 2.2) {
    ppm = map(float(valoareTensiuneRL), 2.2, 3, 30, 70)*10;

  } else if (float(valoareTensiuneRL)*10 <= 34 && float(valoareTensiuneRL)*10 > 30) {
    ppm = 800; // Am ajustat limita superioară a intervalului

  } else if (float(valoareTensiuneRL) <= 8 && float(valoareTensiuneRL) > 3.4) {
    ppm = 1000; // Am ajustat limita inferioară a intervalului
}

  // Verificăm dacă citirea a fost cu succes
  if (isnan(temperatura) || isnan(umiditate)) {
    Serial.println("Eroare la citirea senzorului DHT22!");
    return;
  }
  float i = (temperatura * 1.8 + 32) - (0.55 - 0.0055 * umiditate) * ((temperatura * 1.8 + 32) - 58);
  
  
  //sub 65 este confort intre 65 si 80 alerta si dupa 80 este disconfort


  // Afișăm valorile citite pe ecranul serial
  //Serial.print("Temperatura: ");
  Serial.print(temperatura);
  //Serial.println(" °C");
  Serial.print(",");
  Serial.print(umiditate);
  //Serial.println(" %");

// Citim valoarea analogică de la senzorul MQ135
  
  //float Rs_ro = valoareSenzor / R0;
  // float concentratieGaz =  m * Rs_ro + intercept;
  //int valoareSenzor2 = valoareSenzor / 20;
  // Calculăm concentrația de gaz în aer
  // Aceasta este doar o estimare aproximativă și poate necesita calibrare pentru a fi precisă
  //float concentratieGaz = valoareSenzor / 4095.0 * 3.3; // Conversie la tensiune
  //int concentratieGaz2 = concentratieGaz; // Reglajul pentru MQ135

  //float rezistentaSenzorinAer = 3.3 - concentratieGaz / concentratieGaz;
  //float rezistenta0 = rezistentaSenzorinAer / 9.8;
  //float Rs = 4095.0 * 20000 / valoareSenzor - 20000;  //rs = 4095 * 20000 / valoaresenzor - 20000

  // Afișăm valoarea citită pe ecranul serial
  Serial.print(",");
  Serial.print(valoareSenzor);
  Serial.print(",");
  Serial.print(i);
  Serial.print(",");

    if (ppm < 300) {
    Serial.println("Calitate Foarte Buna a Aerului sub 300 ppm");
  } 
  else if (ppm >= 300 && ppm < 600) {
    Serial.println("Calitate Buna a Aerului 300-500 ppm");
  } 
  else if (ppm >= 600 && ppm < 900) {
    Serial.println("Calitate moderata a Aerului 500-700 ppm");
  } 
  else if (ppm >= 900 && ppm < 1200) {
    Serial.println("Calitate slaba a Aerului 700-1000 ppm");
  } 
  else {
    Serial.println("Calitate foarte slaba a Aerului peste 1000 ppm");
  }
  
  Serial.print("\n");
  
  delay(1000); // Pauză de 1 secundă între citiri

}
