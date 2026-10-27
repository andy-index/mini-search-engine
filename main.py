import string
import os
import math

# IMPORTANT NOTE: Code works perfectly fine, however, .DS_Store keeps bugging the process

def read_files():
    # Retrives a list of all files in this dir
    file_list = os.listdir('documents/')

    raw_dict = {}

    # For each file in the list
    for file in file_list:
        if file.endswith('.txt'):
            with open(f"documents/{file}", mode='r', encoding='utf-8-sig') as file_name:
                docu = file_name.read()
                raw_dict.update({file: docu})

    # Returns the raw dictionary
    return raw_dict


def my_tokens(search_input):
	# Makes any string received lowercase
	search_input = search_input.lower()

	# Replaces all 32 characters with white spaces
	translation = str.maketrans(string.punctuation, "                                ")

    # Returns tokens
	return search_input.translate(translation).split()

def tokenized_dict():
    # Raw dictionary in a variable
    file_dict = read_files()
    # Recommended to create a NEW dict instead of returning the same dict

    # Iterate over raw dictionary and tokenize all values(strings)
    for key, value in file_dict.items():
        my_values = my_tokens(value)
        file_dict.update({key: my_values})

    return file_dict

# Inverted index     
token_dict = tokenized_dict()
inverted_dict = {}

# Outer loop to iterate over key:value pairs
for key, value in token_dict.items():
    
    # Inner loop to iterate over the values
    for item in value:
        
        # If value DOES NOT exist as a key in the new dict, it transforms into a key in the new dict
        if item not in inverted_dict.keys():
            inverted_dict.update({item: {key}})
        else:
           inverted_dict[item].add(key)

# inverted_dict now has the inverted index dictionary

def inter_function(query):
        # List of tokens from query in a variable
        token_query = my_tokens(query)   

        if not token_query:
            return 'Invalid input. Please type something.'   

        # Validates that every token exists in the dict
        for item in token_query:
            if item not in inverted_dict:
                return f'No document contains the word(s) \'{' '.join(token_query)}\'.'   


        set_var = inverted_dict[token_query[0]].copy() 
        # Loop intersects the sets
        for token in token_query[1:]: 
                         
            set_var  &= inverted_dict[token] 


        # If set is empty 
        if not set_var: 
            return 'No documents contain all these words.' 
          
        return set_var

def union_function(query):  
    token_query = my_tokens(query)

    if not token_query:
        return 'Invalid Input. Please type something.'

    not_key = []   

    for token in token_query:
        if token not in inverted_dict:       
            not_key.append(token)
    
    for item in not_key:
        token_query.remove(item)  
    
    if not token_query and not_key:
        return f'No document contains the word(s): \'{'\' \''.join(not_key)}\''
    elif not_key:
        print(f'No document contains the word(s): \'{'\' \''.join(not_key)}\'')
     
   # token_query should NEVER be empty, if is, it should not reach this point 
    uni_var = inverted_dict[token_query[0]].copy()

    for token in token_query[1:]:
        
        uni_var |= inverted_dict[token]
      
    return uni_var
     
def tf_funct(query):
    token_query = my_tokens(query)
    
    if not token_query:
        return 'Invalid input. Please type something.'

    tf_results = {}

    for term in token_query:
        tf_results[term] = {}
        
        for doc_name, tokens in token_dict.items():
            freq = tokens.count(term)
            if freq > 0:
                tf_results[term][doc_name] = freq / len(tokens)
        
    return tf_results

def idf_funct(query):
    token_query = my_tokens(query)
    
    if not token_query:
        return 'Invalid input. Please type something.'
        
    total_docs = len(token_dict)
    idf_results = {}
    
    for term in token_query:
        if term in inverted_dict:
            # Number of documents containing the term
            doc_count = len(inverted_dict[term])
            # Calculate IDF using natural logarithm
            idf_results[term] = math.log(total_docs / doc_count)
        else:
            idf_results[term] = 0.0  # Term does not exist in the corpus
            
    return idf_results

      
while True:
   
    # Ask user for input 
    query = input('Search for a document: Type \':quit\' when finished. ')
    
    # Breaks out of the loop
    if query == ':quit':
        break
    
    results = tf_funct(query)
    print(results)
    #print(union_function(query))


  





