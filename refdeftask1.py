##########
# TASK 1 #
##########

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = ""

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = "task1"
# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of the
# functions below, each of which currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# Do not change the names or parameters of any of these functions
# Make sure you read the function descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
#
# The script contains a test plan and code to perform soime basic tests
# on the functions and display the results of the tests
#
# To run the tests type  run_tests()  at the command line in the
# Python shell
#
# Do be advised, however, that the marker will use different test
# cases and even if your code passes all of the tests in this script
# there may be some other tests that it fails
#
# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

##########################
# Function 1 (2 marks)
##########################

def sets (S,T,U) :   
# Parameters: three sets S, T, U
# Returns:
#  A single set that combines sets S, T and U in the manner
#  shown as a shaded area on the Venn diagram in the document
#  sets.pdf that you will find in the Zip archive
#  you downloaded from Canvas
#  The original sets S, T and U are left unchanged

    return None    # code stub




##########################
# Function 2 (3 marks)
##########################

def new_dict (the_keys,the_data_items) :
# Parameters: two lists the_keys, the_data_items that may be of
#  different lengths
#  the_keys will contain a sequence of hashable values
#  (with no repeats) as it is going to supply the keys
#  for a dictionary
# Returns:
#  the paur  (new_dictionary, spare_data)
#  where  new_dictionary  is a dictionary in which elements
#         of the_keys appear as keys to the corresponding
#         elements in the_data_items
#  and    spare_data  is a list containing any spare data items
#
#  Case 1:
#  the_keys  and  the_data_items  are the same length (n)
#  so every key has a matching data item
#  new_dictionary  will contain n entries and the list
#  spare_data  will be empty
#  Example:  dict_from ([1,3,5],[1,9,25])
#  returns   ({1:1, 3:9, 5:25}, [])
#
#  Case 2:
#  the_keys  is longer than  the_data_items
#  so some keys have no matching data items
#  new_dictionary  will contain an entry for every element in
#  the_data_items, and some keys will be discarded
#  the list spare_data  will be empty.
#  Example:  dict_from ([3,5,8,9], [1,4])
#  returns   ({3:1, 5:4}, [])
#
#  Case 3:
#  the_keys  is shorter than  the_data_items
#  all keys are matched but some data items are left over
#  new_dictionary  will contain an entry for every element in
#  the_keys, and there will be some data items to spare
#  the list spare_data  will contain the spare data items
#  Example:  dict_from ([3,5], [1,4,6,7])
#  returns   ({3:1, 5:4}, [6,7])
#

    new_dictionary = None
    spare_data = None
    return (new_dictionary, spare_data)    # code stub



##########################
# Function 3 (3 marks)
##########################

def isCube (n) :
# This function works correctly: DO NOT CHANGE IT
# It is for use in the definition
# of the function cubes (below)
# Parameter: a whole number, n
# Returns:
#  A Boolean value
#   True if n is a cube
#   False otherwise
    i = 0
    i_cubed = 0
    if n < 0 :
        n = -n
    while i_cubed <= n :
        if i_cubed == n :
            return True
        i += 1
        i_cubed = i * i * i
    return False

def isSquare (n) :
# This function works correctly: DO NOT CHANGE IT
# It is for use in the definition
# of the function cubes (below)
# Parameter: a whole number, n
# Returns:
#  A Boolean value
#   True if n is a square
#   False otherwise
    i = 0
    i_squared = 0
    while i_squared <= n :
        if i_squared == n :
            return True
        i += 1
        i_squared = i * i
    return False


def powers (intlist) :
# Needs a function body to replace the code stub
# Parameter: a list of integers, intlist
# Returns:
#  A dictionary containing four entries
#  * The key 'cubes' mapped to a set containing all
#    the numbers in intlist that are cubes, and no others
#    If there are no cubic numbers in intlist the key
#    'cubes' should map to an empty set
#  * The key 'squares' mapped to a set containing all
#    the numbers in intlist that are squares, and no others
#    If there are no square numbers in intlist the key
#    'squares' should map to an empty set
# YOU ARE REQUIRED TO USE the functions isCube and isSquare
# (defined above) to determine whether or not the numbers in
# intlist are cubes / squares

    return None    # code stub



##########################
# Function 4 (3 marks)
##########################

def transmit (in_string) :
# A function that mimics the encoding of bit-strings for transmission
# via a data link
# Parameter: a character string in_string
#   in_string contains a sequence of '0' and '1' characters each of
#   which represents a single bit in a bit-string.
#   For example
#   The character string '0010111' represents the bit-string 0010111
# Returns: a character string out_string, representing high and low voltages
#   using 'U' (UP) and 'D' (DOWN), derived from in_string as follows
#   out_string starts with the sequence 'DD' (two DOWNs) and ends
#   with the sequence 'UU' (two UPs)
#   In between the start and end indicators the sequence of bits from
#   in_string are transmitted in out_string as follows
#   every '0' from in_string is transmitted as 'DUD'
#   every '1' from in_string is transmitted as 'UDU'
# For example
# transmit ('')    returns 'DDUU'
# transmit ('0')   returns 'DDDUDUU'
# transmit ('1')   returns 'DDUDUUU'
# transmit ('00')  returns 'DDDUDDUDUU'
# transmit ('001') returns 'DDDUDDUDUDUUU'
# transmit ('100') returns 'DDUDUDUDDUDUU'
# transmit ('110') returns 'DDUDUUDUDUDUU'
# and so on, so that
# transmit ('0010111') returns 'DDDUDDUDUDUDUDUDUUDUUDUUU'

    return None    # code stub




##########################
# Function 5 (3 marks)
##########################

def receive (in_string) :
# A function that extracts the original bit-string from the
# transmitted version produced by transmit (see function 4)
# so that after executing the following sequence of instructions
#   bits_to_send = '0010'
#   signal_seq = transmit(bits_to_send)
#   received_bits = receive(signal_seq)
# signal_seq is  'DDDUDDUDUDUDUDUU'  and received_bits is  '0010'

    return None    # code stub




##########################
# Function 6 (3 marks)    USE RECURSION
##########################

def contains_a_string (my_list) :
# A function that determines whether or not any of the elements in
# a list are character strings (data type str)
# You are required to USE RECURSION when implementing this function

# Parameter: a non-empty list called  my_list
# Returns: a truth value
#   True when one or more elements of my_list are character strings
#   False when none of the elements are character strings

# Note that the function isinstance can be used to check whether or
# not a data item is a string.
#   isinstance(s,str)
# returns True if s is a character string and False if it is not

    return None     # code stub


##########################
# Function 7 (3 marks)    USE RECURSION
##########################

def alpha_order (wordlist) :
# A function that determines whether or not the elements in a list
# of words are arranged in alphabetical order.
# You are required to USE RECURSION when implementing this function

# Parameter: a list of words, wordlist
#            each word in wordlist is a character string containing
#            only lowercase letters
# Returns: a truth value
#   True when the words in wordlist are in alphabetical order
#   False when they are not

    return None     # code stub



# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
# Do not change any part of this script between here and
# the end of the file
# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

###########################################################################

#                           TEST PLAN

############################################################################

test_plan = dict ()


fn = "sets"
test_plan [fn] = dict()
test_plan [fn] [1] = [[set(),set(),set()],set()]
test_plan [fn] [2] = [[{1},{2},{1,3,2}],{1,3}]
test_plan [fn] [3] = [[{1,2,3,4,5},{6,5,4,7,9},{1,5,6,2,11}],{1,2,3,11}]
test_plan [fn] [4] = [[{8,9,7},{6,3},{5,4,7}],{4,5,7,8,9}]


fn = "new_dict"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[],[]],(dict(),[])]
test_plan [fn] [2] = [[[10],[-8]],({10:-8},[])]
test_plan [fn] [3] = [[[2,4,6],[18,20,22,8]],({2:18,4:20,6:22},[8])]
test_plan [fn] [4] = [[[-5,9,7],[11,21,82,-9,0,3]],({-5:11,9:21,7:82},[-9,0,3])]
test_plan [fn] [5] = [[[1,2,13,9],['a','b','m']],({1:'a',2:'b',13:'m'},[])]


fn = "powers"
test_plan [fn] = dict()
test_plan [fn] [1] = [[list()],{'squares': set(),'cubes': set()}]
test_plan [fn] [2] = [[[-4,-2,-1,4,8]],{'squares': {4}, 'cubes': {-1,8}}]
test_plan [fn] [3] = [[[4,6,8]],{'squares': {4}, 'cubes': {8}}]
test_plan [fn] [4] = [[[3,5,7,9]],{'squares': {9}, 'cubes': set()}]


fn = "transmit" 
test_plan [fn] = dict()
test_plan [fn] [1] = [[''],'DDUU']
test_plan [fn] [2] = [['1'],'DDUDUUU']
test_plan [fn] [3] = [['01'],'DDDUDUDUUU']
test_plan [fn] [4] = [['0011'],'DDDUDDUDUDUUDUUU']
test_plan [fn] [5] = [['11100110'],'DDUDUUDUUDUDUDDUDUDUUDUDUDUU']


fn = "receive"
test_plan [fn] = dict()
test_plan [fn] [1] = [['DDUU'],'']
test_plan [fn] [2] = [['DDUDUUU'],'1']
test_plan [fn] [3] = [['DDDUDUDUUU'],'01']
test_plan [fn] [4] = [['DDDUDDUDUDUUDUUU'],'0011']
test_plan [fn] [5] = [['DDUDUUDUUDUDUDDUDUDUUDUDUDUU'],'11100110']


fn = "contains_a_string"
test_plan [fn] = dict()
test_plan [fn] [1] = [[['a']],True]
test_plan [fn] [2] = [[[1,'a']],True]
test_plan [fn] [3] = [[['0',0]],True]
test_plan [fn] [4] = [[[56,36.5]],False]
test_plan [fn] [5] = [[[98,True,-7]],False]


fn = "alpha_order"
test_plan [fn] = dict()
test_plan [fn] [1] = [[["plane"]],True]
test_plan [fn] [2] = [[["car","plane","train"]],True]
test_plan [fn] [3] = [[["plane","train","car"]],False]
test_plan [fn] [4] = [[["car","car"]],True]
test_plan [fn] [5] = [[["badboy","goodboy","gooddog","gumtree"]],True]


###########################################################################

#                           TEST DRIVER

############################################################################

def tester (ms) :
    results = dict()
    totalmark = 0
    for funcname in ms :
        results[funcname] = dict()
        totalfunc = 0
        tests = ms[funcname].copy()
        for case in tests :
            test      = tests [case]
            args      = test[0]
            arg0      = args[0]
            if isinstance (arg0,str) :
                arg0 = "'" + arg0 + "'"
            else :
                arg0 = str(args[0])
            strargs = "(" + arg0
            for arg in args[1:] :
                if isinstance (arg,str) :
                    arg = "'" + arg + "'"
                else :
                    arg = str(arg)
                strargs = strargs + "," + arg
            strargs   = strargs + ")"
            target    = test[1]
            if isinstance (target,str) :
                strtarget = "'" + target + "'"
            else :
                strtarget = str(target)
            try :
                call = funcname + strargs
                actual = eval(call)
                if isinstance (actual,str) :
                    stractual = "'" + actual + "'"
                else :
                    stractual = str(actual)

            except NameError :
                result = "Name error"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except RecursionError :
                result = "Recursion error (too many recursive calls)"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except :
                result = funcname + " crashed"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue

            if type(actual) != type(target) :
                result = "wrong type returned"
                
            else :
                if target == actual :
                    result = "pass"
                else :
                    result = "FAIL"

            results[funcname][case] = [strargs,strtarget,stractual,result]

    return results



def DisplayTestResults (results) :    
    display = "Test results\n"
    display += "Each function listed in the order tested\n\n"
    
    for fn in results :
        display += "\nTesting " + fn + "\n=========================="
        testres = results[fn]
        for test in testres :
            t = testres[test]
            #display += "\nTest " + str(test)
            display += "\nParameters:    " + t[0]
            display += "\nShould return: " + t[1]
            display += "\nActual return: " + t[2]
            display += "\nTest result:   " + t[3]
            display += "\n"
        display += "\n"
    return display




def run_tests () :
    global test_plan
    
    results = tester(test_plan)
    message = DisplayTestResults (results)
    print (message)

