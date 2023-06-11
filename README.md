# Informatyka_Projekt_2

Program (wtyczka do QGIS'a) służy do podstawowych pomiarów na punktach posiadających współrzędne (różnica wysokości, długość odcinka, azymut, azymut odwrotny, pole powierzchni, zliczenie ilosci wybranych punktow). Użytkownik będzie mógł wybrać jednostki dostosowane do odpowiedniej funkcji ([metry], [grady, stopnie dziesiętne], [m2, ary, hektary]).

Wtyczka napisana jest dla wersji QGIS'a "QGIS 3.22.16". Niewykryto również żadnych błędów w działaniu programu dla wersji "QGIS 3.30.3".

Wtyczka jest napisana w języku programowania PYTHON 3.9.10. Program został testowany na systemach WINDOWS 11, WINDOWS 10.

Wtyczka posiada możliwość wybrania warstwy na której dokonywane są obliczenia (jeżeli użytkownik zaznaczy punkty z innej warstwy, niż z wybranej wtyczka nie dokona obliczeń). Wtyczka posiada możliwość wybrania jednostek, dla azymutu (grady, stopnie dziesiętne) oraz pola powierzchni (m2, ary, hektary). Zaimplementowana została opcja narysowania poligonu - narysowany poligon powstaje na nowej warstwie. Wtyczka ma możliwości dokonania obliczeń różnic wysokości pomiędzy dwoma punktami (metry). Obliczenie długości odcinka między dwoma punktami (metry). Obliczenie azymutu pomiędzy dwoma punktami (grady, stopnie dziesiętne) oraz azymutu odwrotnego (grady, stopnie dziesiętne). Pole powierzchni (m2, ary, hektary) liczone jest na podstawie środka cięzkości figury geometrycznej i łączenia punktów według kolejności ruchu wskazówek zegara następnie punkty poddane są metodą liczenia pola Gaussa. Wtyczka posiada możliwosć zliczenia punktów. Wtyczka ma możliwość również wczytania danych z pliku .txt (Przykład danych w wierszu "X;Y;h" "638935.159;485769.262;86.848", przykładowe dane można również znaleźć w repozytorium w pliku "Przykladowe_wspolrzedne.txt") (Możliwość inputu tylko współrzędnych z układu PL2000, dla innych wtyczka może błęnie policzyć dane). Po wczytaniu pliku, zeby wgrac nowe wspolrzedne trzeba zmienic nazwe wczytanej warstwy inaczej zostanie ona usunieta i zastapiona przez nowy plik. Wtyczka ma możliwość wykazu współrzędnych w samym GUI wtyczki (wykaz współrzędnych X, Y (metry)). Przycisk czyszczący wykaz współrzędnych oraz przycisk czyszczący wssący wszystkie pola. Przycisk zapisujący obliczenia do oddzielnego pliku .txt", który zapisuje sie w folderze domyslnym zapisywania plikow QGIS'a.

Program wszystkie obliczenia dokonuje dla układu współrzędnych PL2000, EPSG=2180.


Błędy: Obliczanie różnic wysokości nie będzie działać, gdy parametr wysokości nie będzie znajdował się w trzeciej kolumnie atrybutów punktów. Obliczanie wysokości nie bedzie działać, kiedy nie będzie atrybutu wysokości.
