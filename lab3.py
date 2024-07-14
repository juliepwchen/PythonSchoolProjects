#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 3
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################

#############################################################################
#   Task:       Iterables, files
#   Description: 
#   1) Open the file and perform exception handling on the file.
#   2) Read in all of the data from the file into a iterable data structure. 
#   3) Close the file.
#   4) Create a new data structure that maps each country name
#      to its associated population and land area.
#   5) Allow the user to make 2 selections based on the following questions:
#      "Does the user want to see information on a "country" or choose a "ranking"
#      -- If the user picks "country", ask the user for the name of the country. 
#      Print out the associated population and land area of the country.
#      -- If the user picks ranking, the user should be asked whether the 
#         user wants ranking based on "population" or "land area.
#         Then 	prompt the user for the ranking that the user wants. 
#         Print out the country name with the corresponding rank.
##############################################################################

# function: main
# - build im-memory records from data file
# - allow user to query
def main():
    filename = "population_by_country_2020.txt"
    try:
        with open(filename, 'r') as infile:
            infile.readline()    # skip first line: headers
            lines = infile.readlines()
            table = mapCountryToPopulationAndLandArea(lines)
            userInquiry(table)
    except IOError:
        print("Could not open input file.")
    except ValueError as exceptObj:
        print(f"Value Errors: {str(exceptObj)}")
    except RuntimeError as error:
        print(f"Runtime Error: {str(error)}")
    except Exception as exceptObj: 
        print(f"Error: {str(exceptObj)}")

# function: mapCountryToPopulationAndLandArea
# - Create a data structure to map countries to population and land area
# 
# @param lines - in-memory table
# @return country_data - table containing the mapping
def mapCountryToPopulationAndLandArea(lines):
    country_data = {}
    for line in lines:
        fields = line.strip().split('\t')
        country_data[fields[0].lower()] = (int(fields[1]), int(fields[5]))
       
    return country_data

# function: userInquiry
# - prompt user to query & print out associated information
# 
# @param table - table containing the mapping
def userInquiry(table):
    while True:
        option = input("Do you want to see info based on a country or ranking? ").lower()
        if (option == "country"):
            country = input("Which country do you want to see? ").lower()
            if country in table:
                print(f"The {country.title()} has population {table[country][0]} and land area {table[country][1]} sq km.\n")
                break
            else: 
                print("Country not found. Please try again.")
        elif (option.lower() == "ranking"):
            criteria = input("Do you want to see the associated country based on population or land area rank? ").lower()
            if (criteria in ["population", "land area"]):
                ranking = int(input("What ranking country do you want to see based on population? "))
                sorted_countries = sorted(table.keys(), key=lambda x: table[x][0 if criteria == 'population' else 1], reverse=True)
                country_name = sorted_countries[ranking-1]
                print(f"The country ranking #{ranking} by {criteria} is {country_name.title()}.")
                break
            else: print("Invalid input. Please try again!")
        else: print("Invalid input. Please try again!")

main()