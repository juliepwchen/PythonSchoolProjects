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
        infile = open(filename, "r")
        try: 
            table = indexTablePerCountry(infile)
            userInquiry(table)
        finally: 
            infile.close()
    except IOError:
        print("Could not open input file.")
    except ValueError as exceptObj:
        print(f"Value Errors: {str(exceptObj)}")
    except RuntimeError as error:
        print(f"Runtime Error: {str(error)}")
    except Exception as exceptObj: 
        print(f"Error: {str(exceptObj)}")

# function: userInquiry
# - prompt user to query & print out associated information
# 
# @param table - in-memory table
def userInquiry(table):
    rankingTable = {}
    option = input("Do you want to see info based on a country or ranking? ")
    if (option == "country"):
        country = input("Which country do you want to see? ")
        print(f"The {country} has population {table[country][0]} and land area {table[country][1]} sq km.\n")
    elif (option == "ranking"):
        criteria = input("Do you want to see the associated country based on population or land area rank? ")
        if (criteria == "population"):
            ranking = int(input("What ranking country do you want to see based on population? "))
            rankingTable = indexRanking(table, 0)
            print(f"The country ranking # {ranking} by population is {rankingTable[ranking]}.\n")
        elif (criteria == "land area"):
            ranking = int(input("What ranking country do you want to see based on land area? "))
            rankingTable = indexRanking(table, 1)
            print(f"The country ranking # {ranking} by land area is {rankingTable[ranking]}.\n")

# function: indexTablePerCountry
# - build in-memory table from input file
# 
# @param infile - input text data file
# @return dictionary { country:[population, landarea] }
def indexTablePerCountry(infile):
    line = infile.readline()    # skip first line: headers
    indexPerCountry = {}
    for line in infile:
        record = processPerRecord(line)
        indexPerCountry[record[0]] = record[1:3]
    return indexPerCountry

# function: indexRanking
# - build an index table based on ranking
# 
# @param table - original dictionaray table
# @index_to_sort_by - index based on population (0) or land area (1)
# @return a dictionary { ranking:country }
def indexRanking(table, index_to_sort_by):
    sorted_data = dict(sorted(table.items(), key=lambda x: x[1][index_to_sort_by]))
    index = len(sorted_data)
    new_dict = {}
    for key in sorted_data:
        new_dict[index] = key
        index -= 1
    return new_dict
        
# function: processPerRecord
#
# @param record - a line in data file
# @return [country, population, landarea]
def processPerRecord(record):
    record = record.rstrip()    # strip newline
    values = record.split()
    values = formatCountryName(values)
    # country = values[0]
    # population = int(values[1])
    # yearlyDelta = float(values[2].rstrip("%"))
    # netDelta = int(values[3])
    # density = int(values[4])
    # landarea = int(values[5])
    # migrants = int(values[6])
    # fertrate = float(values[7])
    # medage = int(values[8])
    # urbanpopulation = float(values[9].rstrip("%"))
    # worldshare = float(values[10].rstrip("%"))
    return [values[0], int(values[1]), int(values[5])]

# function: formatCountryName
#
# @param words - a list of words
# @return a list of words with country reformated
def formatCountryName(words):
    concatenated_words = ""
    for word in words:
        if any(char.isdigit() for char in word):
            break
        concatenated_words += word + " "
    return [concatenated_words.strip()] + words[len(concatenated_words.split()):]

main()

