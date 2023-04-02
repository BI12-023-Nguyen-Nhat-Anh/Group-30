import csv
class ElectricityConsumption:
    '''This class includes the following methods:
search_consumption(ConsumptionID): Searches for a consumption record by its ID.
search_consumption_by_customer_id(CustomerID): Searches for consumption records by a customer ID.
auto_get_consumption(): Automatically calculates the electricity consumption amounts for each customer and appends the data to the ElectricityConsumption.csv file.'''
    def __init__(self, ConsumptionID, CustomerID, Month, Year, ConsumptionAmount):
        self.ConsumptionID = ConsumptionID
        self.CustomerID = CustomerID
        self.Month = Month
        self.Year = Year
        self.ConsumptionAmount = ConsumptionAmount

    @staticmethod
    def search_consumption(ConsumptionID):
        with open('ElectricityConsumption.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(ConsumptionID):
                    return row
        return None

    @staticmethod
    def search_consumption_by_customer_id(CustomerID):
        results = []
        with open('ElectricityConsumption.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == str(CustomerID):
                    results.append(row)
        return results

    @staticmethod
    def auto_get_consumption():
        meter_readings = {}
        with open('MeterReading.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                customer_id = row[1]
                if customer_id not in meter_readings:
                    meter_readings[customer_id] = []
                meter_readings[customer_id].append({
                    'MeterReadingID': row[0],
                    'Month': int(row[4]),
                    'Year': int(row[5]),
                    'ReadingAmount': float(row[6]),
                })

        for customer_id, readings in meter_readings.items():
            # Sort the readings by year and month
            readings.sort(key=lambda x: (x['Year'], x['Month']))

            # Calculate the consumption amounts
            consumption_data = []
            for i in range(len(readings) - 1):
                ConsumptionID = len(consumption_data)
                consumption_amount = readings[i + 1]['ReadingAmount'] - readings[i]['ReadingAmount']
                consumption_data.append(
                    [ConsumptionID, customer_id, readings[i]['Month'], readings[i]['Year'], consumption_amount])

            # Append the consumption data to the CSV file
            with open('ElectricityConsumption.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerows(consumption_data)