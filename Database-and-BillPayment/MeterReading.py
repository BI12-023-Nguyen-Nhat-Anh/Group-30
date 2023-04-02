import csv
import os

class MeterReading:
    def __init__(self, CustomerID, MeterReadingID, Time, Date, Month, Year, ReadingAmount):
        self.CustomerID = CustomerID
        self.MeterReadingID = MeterReadingID
        self.Time = Time
        self.Date = Date
        self.Month = Month
        self.Year = Year
        self.ReadingAmount = ReadingAmount

    @staticmethod
    def create_meter_reading(CustomerID, Time, Date, Month, Year, ReadingAmount):
        # Search for the customer
        with open('Customer.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(CustomerID):
                    # Auto-increase the MeterReadingID
                    with open('MeterReading.csv', 'r') as f_reading:
                        lines = f_reading.readlines()
                        MeterReadingID = len(lines)
                    # Append the data as a line to the CSV file
                    with open('MeterReading.csv', 'a') as f_reading:
                        writer = csv.writer(f_reading)
                        writer.writerow([MeterReadingID, CustomerID, Time, Date, Month, Year, ReadingAmount])
                    break

    @staticmethod
    def input_data_reading(MeterReadingID, Hour, Date, Month, Year, ReadingAmount):
        # Check if the MeterReadingID exists and if the month and year are not duplicates
        with open('MeterReading.csv', 'r') as f:
            reader = csv.reader(f)
            data_exists = False
            for row in reader:
                if row[0] == str(MeterReadingID):
                    data_exists = True
                if row[4] == str(Month) and row[5] == str(Year):
                    data_exists = False
                    break
            if not data_exists:
                return
        # Append the data as a line to the CSV file
        with open('MeterReading.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([MeterReadingID, Hour, Date, Month, Year, ReadingAmount])

    @staticmethod
    def search_meter_reading(MeterReadingID):
        with open('MeterReading.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(MeterReadingID):
                    return row
        return None

    @staticmethod
    def search_meter_reading_by_customer_id(CustomerID):
        results = []
        with open('MeterReading.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == str(CustomerID):
                    results.append(row)
        return results

    @staticmethod
    def update_meter_reading(MeterReadingID, action):
        # Read the existing meter readings
        with open('MeterReading.csv', 'r') as f:
            reader = csv.reader(f)
            rows = [row for row in reader]

        # Perform the specified action
        if action.lower() == "delete":
            rows = [row for row in rows if row[0] != str(MeterReadingID)]
        elif action.lower() == "modify":
            row_to_modify = MeterReading.search_meter_reading(MeterReadingID)
            if row_to_modify:
                rows.remove(row_to_modify)
                new_data = input("Enter the new data as MeterReadingID, Hour, Date, Month, Year, ReadingAmount: ").split
                # Collect the new data
                new_data = input("Enter the new data as Hour, Date, Month, Year, ReadingAmount: ").split(',')
                # Append the new data to the rows
                new_data.insert(0, MeterReadingID)
                rows.append(new_data)
        else:
            print("Invalid action. Please choose 'delete' or 'modify'.")
            return

        # Write the updated rows back to the CSV file
        with open('MeterReading.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
