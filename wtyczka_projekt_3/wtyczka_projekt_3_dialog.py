# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaProjekt3Dialog
                                 A QGIS plugin
 Wtyczka robi podstawowe operacje na punktach (np. liczy rónice wysokości, liczy pole powierzchni). 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Adrian Maksymiuk, Dawid Jundo
        email                : 01169882@pw.edu.pl, 01169882@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from math import atan2, sqrt, pi

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsField, QgsFeature, QgsGeometry, QgsVectorLayer, QgsPointXY, QgsProject
from PyQt5.QtCore import QVariant
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_projekt_3_dialog_base.ui'))
    

class WtyczkaProjekt3Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaProjekt3Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.roznica_wysokosci.clicked.connect(self.roznica_wyskosci_funkcja)
        self.zlicz_punkty.clicked.connect(self.licz_elementy)
        self.wyswietlanie_wspolrzednych.clicked.connect(self.wspolrzedne_funkcja)
        self.pole_powierzchni.clicked.connect(self.pole_powierzchni_funkcja)
        self.wyczyszczenie_tablicy.clicked.connect(self.wyczyszczenie_tablicy_funkcja)
        self.przycisk_zamkniecia.clicked.connect(self.wyczyszczenie_danych_funkcja)
        self.azymut.clicked.connect(self.azymut_funkcja)
        self.dlugosc_odcinka.clicked.connect(self.dlugosc_odcinka_funkcja)
        self.resetuj_wszystko.clicked.connect(self.wyczyszczenie_danych_funkcja)
    
    def dlugosc_odcinka_funkcja(self):
        liczba_elementów = len(self.mMapLayerComboBox_layers.currentLayer().selectedFeatures())
        if liczba_elementów == 2:
            wybrane_elementy = self.mMapLayerComboBox_layers.currentLayer().selectedFeatures() 
            K=[]
            for element in wybrane_elementy:
                wsp = element.geometry().asPoint()
                X = wsp.x()
                Y = wsp.y()
                K.append([X, Y])
            odl=sqrt((K[0][0]-K[1][0])**2+(K[0][1]-K[1][1])**2)
            self.dlugosc_odcinka_wynik.setText(f'Odległosć pomiędzy punktami wynosi: {odl:.3f}')
            self.blad_rozwiazanie.clear()
        elif liczba_elementów < 2:
            self.dlugosc_odcinka_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za mało punktów")
        elif liczba_elementów > 2:
            self.dlugosc_odcinka_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za dużo punktów")
                
                
    def azymut_funkcja(self):
        liczba_elementów = len(self.mMapLayerComboBox_layers.currentLayer().selectedFeatures())
        if liczba_elementów == 2:
            wybrane_elementy = self.mMapLayerComboBox_layers.currentLayer().selectedFeatures() 
            K=[]
            for element in wybrane_elementy:
                wsp = element.geometry().asPoint()
                X = wsp.x()
                Y = wsp.y()
                K.append([X, Y])
            Az = atan2((K[1][1]-K[0][1]), (K[1][0]-K[0][0]))
            if 'stopnie_dziesietne' == self.jednostka_azymut.currentText():
                Az =Az*180/pi
                if Az < 0:
                    Az += 360
                elif Az > 360:
                    Az -= 360
                self.azymut_wynik.setText(f'Azymut wynosi: {Az:.7f}')
                Az_odw = Az+180
                if Az_odw < 0:
                    Az_odw += 360
                elif Az_odw > 360:
                    Az_odw -= 360
                self.azymut_odwrotny_wynik.setText(f'Azymut odwrotny wynosi: {Az:.7f}')
                self.blad_rozwiazanie.clear()
            elif 'grady' == self.jednostka_azymut.currentText():
                Az =Az*200/pi
                if Az < 0:
                    Az += 400
                elif Az > 400:
                    Az -= 400
                self.azymut_wynik.setText(f'Azymut wynosi: {Az:.4f}')
                Az_odw = Az+200
                if Az_odw < 0:
                    Az_odw += 400
                elif Az_odw > 400:
                    Az_odw -= 400
                self.azymut_odwrotny_wynik.setText(f'Azymut odwrotny wynosi: {Az:.4f}')
                self.blad_rozwiazanie.clear()
        elif liczba_elementów < 2:
            self.azymut_wynik.setText("Błąd")
            self.azymut_odwrotny_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za mało punktów")
        elif liczba_elementów > 2:
            self.azymut_wynik.setText("Błąd")
            self.azymut_odwrotny_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za dużo punktów")
            
            
            
    def licz_elementy(self):
        liczba_elementów = len(self.mMapLayerComboBox_layers.currentLayer().selectedFeatures())
        self.pokaz_ilosc_punktow.setText(str(liczba_elementów))
        
    def wspolrzedne_funkcja(self):
        wybrane_elementy = self.mMapLayerComboBox_layers.currentLayer().selectedFeatures()
        K = []
        iden = 0
        for element in wybrane_elementy:
            wsp = element.geometry().asPoint()
            X = wsp.x()
            Y = wsp.y()
            K.append([X, Y])
            iden += 1
            self.wspolrzedne.append(f'Kordynaty punktu {iden}: X = {X:.3f}, Y = {Y:.3f}')
            
    def roznica_wyskosci_funkcja(self):
        liczba_elementów = len(self.mMapLayerComboBox_layers.currentLayer().selectedFeatures())
        if liczba_elementów == 2: 
            wybrane_elementy = self.mMapLayerComboBox_layers.currentLayer().selectedFeatures() 
            K=[]
            for element in wybrane_elementy:
                wsp = element.geometry().asPoint()
                Z = wsp.z()
                K.append(Z)
                roznica_wysokosci=K[0]-K[1]
            self.roznica_wysokosci_wynik.setText(f'{roznica_wysokosci:.3f}')
            self.blad_rozwiazanie.clear()
        elif liczba_elementów < 2:
            self.roznica_wysokosci_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za mało punktów")
        elif liczba_elementów > 2:
            self.roznica_wysokosci_wynik.setText("Błąd")
            self.blad_rozwiazanie.setText("Wybrano za dużo punktów")
            
            
    def pole_powierzchni_funkcja(self):
        liczba_elementów = len(self.mMapLayerComboBox_layers.currentLayer().selectedFeatures())
        if liczba_elementów >= 3:
            wybrane_elementy = self.mMapLayerComboBox_layers.currentLayer().selectedFeatures()
            K = []
            iden = 0
            for element in wybrane_elementy:
                wsp = element.geometry().asPoint()
                X = wsp.x()
                Y = wsp.y()
                K.append([X, Y])
            suma=0
            for i in range(len(K)):
                if i<len(K)-1:
                    P=(K[i][0]*(K[i+1][1]-K[i-1][1]))
                    print(P)
                    suma += P
            P=(K[-1][0]*(K[0][1]-K[-2][1]))
            suma += P
            suma=0.5*abs(suma)   
            if 'metry2' == self.jednostka_pole.currentText():
                self.pole_powierzchni_wynik.setText(str(suma))
            if 'ary' == self.jednostka_pole.currentText():
                self.pole_powierzchni_wynik.setText(str(suma/100))
            if 'hektary' == self.jednostka_pole.currentText():
                self.pole_powierzchni_wynik.setText(str(suma/10000))
            self.poligon_wybor.toggled.connect(lambda checked: self.radioButton1Toggled(checked, K))
            
        elif liczba_elementów < 3:
            self.pole_powierzchni_wynik.setText("Wybrano za mało punktów")
    
    def radioButton1Toggled(self, checked, K):
        if checked:
            layer_name = 'poligon_obliczonego_pola'
            existing_layers = QgsProject.instance().mapLayersByName(layer_name)

            for warstaw_poligon in existing_layers:
                QgsProject.instance().removeMapLayer(warstaw_poligon)
            
            warstaw_poligon = QgsVectorLayer('Polygon?crs=EPSG:2180', 'poligion_obliczonego_pola', 'memory')
            warstaw_poligon.startEditing()
            
            field = QgsField("Area", QVariant.Double)
            warstaw_poligon.addAttribute(field)

            polygon = QgsGeometry.fromPolygonXY([[QgsPointXY(point[0], point[1]) for point in K]])
            
            area = polygon.area()
            attributes = [area]
            
            feature = QgsFeature()
            feature.setGeometry(polygon)
            feature.setAttributes(attributes)
            warstaw_poligon.addFeature(feature)
            
            warstaw_poligon.commitChanges()
            warstaw_poligon.updateExtents()
            QgsProject.instance().addMapLayer(warstaw_poligon)
            
    def wyczyszczenie_tablicy_funkcja(self):
        self.wspolrzedne.clear()
        
    def wyczyszczenie_danych_funkcja(self):
        self.wspolrzedne.clear()
        self.pole_powierzchni_wynik.clear()
        self.roznica_wysokosci_wynik.clear()
        self.pokaz_ilosc_punktow.clear()
        self.azymut_odwrotny_wynik.clear()
        self.blad_rozwiazanie.clear()
        self.azymut_wynik.clear()
        self.dlugosc_odcinka_wynik.clear()
        
        
        
         
