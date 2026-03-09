'''3. Assume a file city.txt with details of 5 cities in given format (cityname population(in 
lakhs) area(in sq KM) ): 
Example: 
Dehradun 5.78 308.20 
Delhi 190 1484 
…………… 
Open file city.txt and read to: 
a. Display details of all cities 
b. Display city names with population more than 10Lakhs 
c. Display sum of areas of all cities'''
try:
    file=open("city.txt","r")
    lines=file.readlines()
    file.close()

    total_area=0

    print("Details of all cities:")
    for line in lines:
        data=line.strip().split()
        city=data[0]
        population=float(data[1])
        area=float(data[2])

        print("City:",city,"Population:",population,"Area:",area)

        total_area+=area

    print("\nCities with population more than 10 Lakhs:")
    for line in lines:
        data=line.strip().split()
        city=data[0]
        population=float(data[1])

        if population>10:
            print(city)

    print("\nSum of all areas:",total_area)

except Exception as e:
    print("Error:",e)