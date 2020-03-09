import os,sys,datetime,csv,glob
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu,QAction
from PyQt5.QtWidgets import QPushButton,QFileDialog
from PyQt5.QtWidgets import QMessageBox,QTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
#from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery,QSqlTableModel
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from qgis.PyQt.QtWidgets import QWidget,QTableView,QDialog,QLineEdit,QMessageBox
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery,QSqlTableModel
#import psycopg2
import re
import time,subprocess,datetime  
import shutil
from tempfile import NamedTemporaryFile


#from .geocoding_dialog import GeoCodingDialog


def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	global tableWidget
	#global myupdatebtn
	#global featureid
	tableWidget = dialog.findChild(QTableWidget, "tableWidget")
		
	#add = dialog.findChild(QLineEdit, "address")
	
	#QMessageBox.information(dialog,"Info", str(feature.id()))
	#QMessageBox.information(dialog,"Info", str(feature.attribute("poi_id")))
	#createTable(dialog,tableWidget,feature.attribute("id"),10) 
	#createTable(dialog,tableWidget,feature.id(),10)
	#showcsvdata(dialog,tableWidget,feature.attribute("poi_id"))
	#readandconvertresults(dialog,tableWidget,feature.attribute("poi_id"))
	#featureid=feature.attribute("poi_id")
	poi_table(dialog,tableWidget,feature.attribute("address"))
	

# function that takes the last modified file in experiments folder  	
# (model deployment should be the last modified as the last step)
# and retrieves the converted results from model_deployment_results file  
	
def last_exp_file(self):    
							
	global latest_file
	temp1=os.getcwd() + "\\LGM-Geocoding-master"
	temp2=os.listdir(path=str(temp1))
	latest_file = ""
	if 'experiments' in temp2:
		list_of_files = glob.glob(str(temp1) + '\\experiments\\*')  
		#print(list_of_files)
		latest_file = max(list_of_files,key=os.path.getctime)
		#print('inside last_exp_file')
	#return latest_file
	else:
		latest_file = ("")
		
	return latest_file    	
	
	
	
	
def poi_table(self,tableWidget,address):

	tableWidget.setRowCount(1)
	tableWidget.setColumnCount(4)
	tableWidget.setHorizontalHeaderLabels("address score x_original y_original".split())
		
	
	file_path = last_exp_file(self) + "\\model_deployment_results\\original.csv"
	#print(file_path)
	
	#exp_path = "C:\\Users\\ivarkas\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\geocoding\\LGM-Geocoding-master\\experiments\\exp_11-12-2019_10-52-55"
	
	#file_path = exp_path + "//model_deployment_results" + "//predictionsrplconverted.csv"	
	
	with open(file_path,newline='',encoding='utf-8') as csv_file:   #ISO-8859-7
		csv_data = csv.reader(csv_file,delimiter=',')
		count=0	
		for row in csv_data:
			if str(row[0]) == str(address):
				
				a=row[0] # address
				b=row[1] #score
				c=row[2] # x_original
				d=row[3] #y_original
				
				
				d=d.replace(",","")
				a=a.replace(",","").replace("[","").replace("]","")
				#b=b.replace("'","")
				#c=c.replace("'","")
				
				#a=a.replace("[","").replace("]","")
				#b=b.replace("[","").replace("]","")
				#c=c.replace("[","").replace("]","")
				
				
				#a=a.split(' ',2)[:2]
				#b=b.split(' ',4)[2:4]
				#c=c.split(' ',6)[4:6]
				
				item8=QTableWidgetItem(str(a))
				item9=QTableWidgetItem(str(b))
				item10=QTableWidgetItem(str(c))
				item11=QTableWidgetItem(str(d))
				#item12=QTableWidgetItem(str(c))
				
				tableWidget.setItem(count,0, item8)
				tableWidget.setItem(count,1, item9)
				tableWidget.setItem(count,2, item10)
				tableWidget.setItem(count,3, item11)
				#tableWidget.setItem(count,4, item12)
				tableWidget.resizeColumnsToContents()
				tableWidget.resizeRowsToContents()
				count=count+1	
					
#def onclick(rindex,cindex):
	#flags = tableWidget.item(1,4).flags()
	#flags = tableWidget.item(1,3).flags()		
	
	