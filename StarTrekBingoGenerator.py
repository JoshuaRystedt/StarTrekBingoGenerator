#   This is a Python script for generating a random selection of Bingo spaces for Start Trek Binger by Gabrielle Rystetd
#
#   Copyright (C) 2018 by Joshua Rystedt
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   To read a copy of the GNU General Public License see <http://www.gnu.org/licenses/>.

# Imports
from random import shuffle

# Declare the list of options
optionsList = list(range(1, 32))

# Dictionary of options
optionsKeyDict = {
    1 : "Captain Kirk's Shirt Rips",
    2 : "Fate of humanity hangs in the balance",
    3 : "Red shirt dies",
    4 : "'S/He's dead, Jim'",
    5 : "Transporter malfunction",
    6 : "Pot shot at 20th century earth culture",
    7 : "Spock calculates something",
    8 : "Vulcan neck pinch is performed",
    9 : "Obvious use of styrofoam",
    10 : "Kirk beats someone up",
    11 : "Spock mind melds with someone/thing",
    12 : "Shuttlecraft would've been a better choice than transporter",
    13 : "'I'm a doctor, not a ______'",
    14 : "Red alert",
    15 : "Alien chick without a bra",
    16 : "Chekov talks about Russia",
    17 : "Sulu does martial arts",
    18 : "Environmental suits would've prevented problem",
    19 : "Kirk makes sexual reference",
    20 : "McCoy insults Spock",
    21 : "Spock insults humanity",
    22 : "Someone wears a disguise",
    23 : "Prime directive is ignored",
    24 : "A planet is destroyed",
    25 : "Everyone on bridge falls in different directions",
    26 : "Kirk asks scotty for more power",
    27 : "Someone dead is resurrected",
    28 : "Kirk talks a computer into self-destruction",
    29 : "Spock says 'illogical'",
    30 : "Phasers don't work",
    31 : "Phasers used to heat rocks",
}

# Shuffle list of options
def shuffleList():
    shuffle(optionsList)

# Print the first 24 items from the shuffled list
def generateCard():
    shuffleList()
    print " "
    print "-- HERE'S YOUR CARD! --"
    print " "
    print str(optionsList[0:5])
    print str(optionsList[5:10])
    print str(optionsList[10:12]) + " Free " + str(optionsList[12:14])
    print str(optionsList[14:19])
    print str(optionsList[19:24])
    print " "
    print "-- KEY: --"
    print " "
    for i in optionsList[0:24]:
        print str(i) + " = " + optionsKeyDict[i]
    print " "

# Generate the Bingo Card.
generateCard()
