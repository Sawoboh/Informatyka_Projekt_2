# Informatyka_Projekt_2

Program (wtyczka do QGIS'a) służy do podstawowych pomiarów na punktach posiadających współrzędne (różnica wysokości, długość odcinka, azymut, azymut odwrotny, pole powierzchni, zliczenie ilosci wybranych punktow). Użytkownik będzie mógł wybrać jednostki dostosowane do odpowiedniej funkcji ([metry], [grady, stopnie dziesiętne], [m2, ary, hektary]).

Wtyczka napisana jest dla wersji QGIS'a "QGIS 3.22.16". Niewykryto również żadnych błędów w działaniu programu dla wersji "QGIS 3.30.3".

Wtyczka jest napisana w języku programowania PYTHON 3.9.10. Program został testowany na systemach WINDOWS 11, WINDOWS 10.

Wtyczka posiada możliwość wybrania warstwy na której dokonywane są obliczenia (jeżeli użytkownik zaznaczy punkty z innej warstwy, niż z wybranej wtyczka nie dokona obliczeń). Wtyczka posiada możliwość wybrania jednostek, dla azymutu (grady, stopnie dziesiętne) oraz pola powierzchni (m2, ary, hektary). Zaimplementowana została opcja narysowania poligonu - narysowany poligon powstaje na nowej warstwie. Wtyczka ma możliwości dokonania obliczeń różnic wysokości pomiędzy dwoma punktami (metry). Obliczenie długości odcinka między dwoma punktami (metry). Obliczenie azymutu pomiędzy dwoma punktami (grady, stopnie dziesiętne) oraz azymutu odwrotnego (grady, stopnie dziesiętne). 

Program wszystkie obliczenia dokonuje dla układu współrzędnych PL2000, EPSG=2180.


Błędy: Obliczanie różnic wysokości nie będzie działać, gdy parametr wysokości nie będzie znajdował się w trzeciej kolumnie atrybutów punktów. Obliczanie wysokości nie bedzie działać, kiedy nie będzie atrybutu wysokości.
