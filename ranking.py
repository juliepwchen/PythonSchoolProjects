#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 6
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#
#   HTML parser: pip3 install beautifulsoup4 lxml
#############################################################################

#############################################################################
#   Task:       Ranking class 
#   Description: for storing data from the htmln data file and search.
##############################################################################
from bs4 import BeautifulSoup

class Ranking:
    def __init__(self, filename="lab6.txt"):
        self.__data = []
        self._parse_file(filename)

    # internal method: _parse_file
    # - initialize the Ranking object with data from the input file:
    # 
    # @param filename - input html file
    def _parse_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self._parseDataWithSoup(content)
        except IOError:
            print("Cannot open the file for read!")
        except ValueError as e:
            print(f"Value Errors: {str(e)}")
        except Exception as e:
            print(f"Errors occur when opening or reading the file: {str(e)}") 
    
    # internal method: _parseDataWithSoup
    # - parse document based on 2 tables
    # 
    # @param content - whole document as a string
    def _parseDataWithSoup(self, content):
        soup = BeautifulSoup(content, 'lxml')
        top20_table = soup.find('table', {'id': 'top20'})
        self._parseTop20(top20_table )
        otherPL_table = soup.find('table', {'id': 'otherPL'})
        self._parseOtherPL(otherPL_table)

    # internal method: _parseTop20
    # - parse Top 20 table for ranking, language, change
    # - store data into self.__data list structure
    # 
    # @param table - Tag <table> class from Beautiful Soup 
    def _parseTop20(self, table):
        rows = table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            cols = row.find_all('td')
            number = int(cols[0].text.strip())
            language = cols[4].text.strip()
            rank = float(cols[5].text.strip().strip('%'))
            change = cols[6].text.strip()
            self.__data.append({
                'number': number,
                'rank': rank,
                'language': language,
                'change': change
            })

    # internal method: _parseOtherPL
    # - parse other PL table for ranking, language
    # - store data into self.__data structure
    # 
    # @param table - Tag <table> class from Beautiful Soup 
    def _parseOtherPL(self, table):
        rows = table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            cols = row.find_all('td')
            number = int(cols[0].text.strip())
            language = cols[1].text.strip()
            rank = float(cols[2].text.strip().strip('%'))
            self.__data.append({
                'number': number,
                'rank': rank,
                'language': language,
                'change': None
            })

    # Getter method: getRankingData
    # 
    # @return self.__data
    def getRankingData(self): return self.__data

    # method: get_language_by_rank
    # 
    # @return language
    def get_language_by_rank(self, rank):
        for entry in self.__data:
            if entry['rank'] == rank:
                return entry['language']
        return None
    
    # method: get_rank_by_language
    # 
    # @return rank
    def get_rank_by_language(self, language):
        for entry in self.__data:
            if entry['language'].lower() == language.lower():
                return entry['rank']
        return None

    # method: get_change_by_language
    # 
    # @return change
    def get_change_by_language(self, language):
        for entry in self.__data:
            if entry['language'].lower() == language.lower():
                return entry['change']
        return None

    # method: languages_sorted_by_ranking
    # - allows for a search of languages, sorted by ranking
    #
    # @return a generator of language and ranking
    def languages_sorted_by_ranking(self):
        sorted_data = sorted(self.__data, key=lambda x: x['rank'], reverse=True)
        for entry in sorted_data:
            yield (entry['number'], entry['language'], entry['rank'])
    
    # method: languages_sorted_by_change
    # - yields languages, sorted by change
    # 
    # @return a generator of language and change (if exsits)
    def languages_sorted_by_change(self, positive=True):
        def parse_change(change):
            try:
                return float(change.strip('%'))
            except:
                return None
        
        filtered_data = [entry for entry in self.__data[:20] if entry['change']]
        filtered_data = [entry for entry in filtered_data if (parse_change(entry['change']) > 0) == positive]
        sorted_data = sorted(filtered_data, key=lambda x: parse_change(x['change']), reverse=True)
        
        for entry in sorted_data:
            yield (entry['language'], entry['change'])

    # method: search_languages
    # - allows for a search of one or more languages
    # 
    def search_languages(self, *languages):
            results = []
            for language in languages:
                found = False
                for entry in self.__data:
                    if entry['language'].lower() == language.lower():
                        change_info = entry.get('change', 'N/A')
                        if change_info is None:
                            change_info = "(no change info)"
                        results.append(f"{entry['language']}\t\t{float(entry.get('rank', 'N/A')):8.2f}\t{change_info}")
                        found = True
                        break
                if not found:
                    results.append(f"{language} not found")
            return results
