import openpyxl
import os
import yaml

from .getLanguage import getLanguage
import logging

import pandas as pd


#This class will determine the correct file standards (such as the sheet name, header format, etc.)
class FileTemplate:
    
    def __init__(self, f_path):
        self.file_path = f_path

        #The excel file provided must contain a sheet that has the name "PA-Rights"
        self.EXCEL_SHEET_NAME = "PA-Rights"
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            uni = yaml_file['University'] 



        #The standard is set so that cell A3 must have the value "Title",
        # Cell B3 must have the value "Publisher" ... and so on
        self.FINAL_HEADER_FIELDS = {
                            "A3": "Title",
                            "B3": "Publisher",
                            "C3": "Platform_YOP", 
                            "D3": "Platform_eISBN", 
                            "E3": "OCN",            
                            "F3": "agreement_code",
                            "G3": "collection_name",
                            "H3": "title_metadata_last_modified", 
                            "I3": uni
                        }
        
        # Any value will be accepted in the cell A1 as long as the cell is not empty
        self.NECESSARY_FIELDS = {
                        "A1": "Platform"
                        }

    #Getters
    def get_file_path(self):
        return self.file_path
    
    def get_sheet_name(self):
        return self.EXCEL_SHEET_NAME
    
    def get_necessary_fields(self):
        return self.NECESSARY_FIELDS
    
    def get_final_header_fields(self):
        return self.FINAL_HEADER_FIELDS
    
    def number_of_fixed_fields(self):
        return len(self.FINAL_HEADER_FIELDS)
    
    #Setters
    def set_file_path(self, f_path):
        self.file_path = f_path
    
    def set_excel_sheet_name(self, f_sheet):
        self.EXCEL_SHEET_NAME = f_sheet
    
    def set_necessary_fields(self, fields):
        self.NECESSARY_FIELDS = fields
    
    def set_final_header_fields(self, fields):
        self.FINAL_HEADER_FIELDS = fields


#The class which will determine if the file provided is valid
class FileValidator:

    #Variables
    file = None        #File object to be validated
    error_message = [] #Will remain empty if the file turns out to be valid
    workbook = None    #Will be used to open the file (if the file is accessible)
    worksheet = None   #Will be used to locate the excel sheet

    #To create validator object, pass in the file path to be validated
    def __init__(self, file_to_be_validated):
        self.file = file_to_be_validated
        self.error_message = []
        self.excess_error = []

    #Determine if the file can be accessed
    def file_can_be_accessed(self):
    
        path = self.file.get_file_path()
        sheet = self.file.get_sheet_name()


        file_name, file_extension = os.path.splitext(path)
        if (path == ""):
            self.error_message.append(0)
            # ("Error: No File Provided")

        elif file_extension not in [".xlsx"]:
            self.error_message.append(1)
            # ("Error: Invalid File")
        elif (not os.path.isfile(path)):
            self.error_message.append(2)
            # ("Error: File does not exist")
        else:
            try: #If we reach this part of the code, then the file is accessible, but the sheet "PA-Rights" may not exist, so we use a try except block
                self.workbook = openpyxl.load_workbook(path)
                self.worksheet = self.workbook[sheet]

            except (KeyError):
                self.error_message.append(3)
                # "Invalid sheet name: Set sheet name to PA-Rights"
            
        return (len(self.error_message) == 0) #If the length of the error message is still empty, this returns true 
        

    #Make sure none of the necessary fields are empty (e.g., platform name)
    def necessary_fields_not_empty(self):
        

        list2 = []
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            uni = yaml_file['University'] 


        for i in range (len(self.file.get_necessary_fields())):


            cell_keys = list(self.file.get_necessary_fields().keys()) #A key is the cell name (like "A1")
            cell_values = list(self.file.get_necessary_fields().values()) #A value is what's inside the field, like "Taylor&Frances"


            current_cell_value = self.worksheet[cell_keys[i]].value 
            maybe_missing = cell_values[i]

            if (current_cell_value == None):
                if cell_keys[i] == 'A1':
                    self.error_message.append(2)
                if 4 not in self.error_message:
                    self.error_message.append(4)
                if getLanguage() == 1:
                    list2.append("Champ manquant: Insérez le champ " + maybe_missing + " dans la cellule " + cell_keys[i])
                else:
                    list2.append("Missing Field: Insert " + maybe_missing + " field into cell " + cell_keys[i])

        self.excess_error = self.excess_error + list2


    def good_header_format(self):
        
        list2 = []

        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            uni = yaml_file['University'] 


        for i in range (len(self.file.get_final_header_fields())):


            cell_keys = list(self.file.get_final_header_fields().keys())
            cell_values = list(self.file.get_final_header_fields().values())


            current_cell_value = self.worksheet[cell_keys[i]].value
            expected_cell_value = cell_values[i]

            if (current_cell_value != expected_cell_value):
                if expected_cell_value == uni:
                    self.error_message.append(5)
                elif 4 not in self.error_message:
                    self.error_message.append(4)
                if getLanguage() == 1:
                    list2.append("Champ de cellule invalide: Définissez la cellule " + cell_keys[i] + " à " + cell_values[i])
                else:
                    list2.append("Invalid cell field: Set cell " + cell_keys[i] + " to " + cell_values[i])

        self.excess_error = self.excess_error + list2


    def getErrorMessage(self):
        return self.error_message
    

    #Determine if the file is valid
    def validFile(self):


        if (self.file_can_be_accessed()):
            self.necessary_fields_not_empty()
            self.good_header_format()
        logging.info(self.excess_error)
        return (len(self.error_message) == 0) #Returns true (yes - valid file) if the error message is empty



good_file1 = "exampleExcelFiles/UPEI_Ebooks_local_correct_sample1.xlsx"
good_file2 = "exampleExcelFiles/UPEI_Ebooks_local_correct_sample2.xlsx"
bad_file1 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample1.xlsx"
bad_file2 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample2.xlsx"
bad_file3 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample3.xlsx"
bad_file4 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample4.xlsx"
bad_file5 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample5.xlsx"
bad_file6 = "exampleExcelFiles/UPEI_Ebooks_local_incorrect_sample6.xlsx"

