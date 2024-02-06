import openpyxl 
from openpyxl.worksheet.datavalidation import DataValidation

def validate_headers(file):
    # Create the workbook and worksheet we'll be working with
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    valid_header = True
    error_message = []

    headers = '"Title, Publisher, Platform_YOP, Platform_eISBN, OCN, agreement_code, collection_name, title_metadata_last_modified"'
    #Create a data-validation object with list validation

    dv = DataValidation(type="list", formula1=headers, allow_blank=False)


    cellDictionairy = {
                        "A3" : "Title",
                        "B3": "Publisher",
                        "C3": "Platform_YOP", #int
                        "D3": "Platform_eISBN", #int
                        "E3": "OCN",            #int
                        "F3": "agreement_code",
                        "G3": "collection_name",
                        "H3": "title_metadata_last_modified" #date
    }


    cellKeys = list(cellDictionairy.keys())
    cellValues = list(cellDictionairy.values())
    for i in range(len(cellDictionairy)):


        cell = cellKeys[i]
        cell_field = ws[cell]
        dv.add(cell_field)

        correct_value = cellValues[i]

        if cell_field.value.upper() != correct_value.upper():
            error_message.append("Invalid header: Set cell " + cell + " to " + correct_value)
        
    print
    if len(error_message) != 0:
        valid_header = False
        print(error_message)
        return False
    print("Success")
    return True

    dv.showInputMessage = True
    dv.showErrorMessage = True
    ws.add_data_validation(dv)

validate_headers('source/storage/spreadsheets/ManualUpload.xlsx')