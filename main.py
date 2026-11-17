import string
import os
import math
import time
import itertools

def read_files():
    # Retrives a list of all files in this dir
    file_list = os.listdir('documents_cranfield/')

    raw_dict = {}

    # For each file in the list
    for file in file_list:
        if file.endswith('.txt'):
            with open(f"documents_cranfield/{file}", mode='r', encoding='utf-8-sig') as file_name:
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
def build_inverted_index(token_dict):
    inverted_index = {}

    # Outer loop to iterate over key:value pairs
    for key, value in token_dict.items():
        
        # Inner loop to iterate over the values
        for item in value:
            
            # If value DOES NOT exist as a key in the new dict, it transforms into a key in the new dict
            if item not in inverted_index.keys():
                inverted_index.update({item: {key}})
            else:
                inverted_index[item].add(key)

    return inverted_index

token_dict = tokenized_dict()

# NOTE: inverted_dict now has the inverted index dictionary
inverted_dict = build_inverted_index(token_dict)


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
     
   # token_query should NEVER be empty, if so, it should not reach this point 
    uni_var = inverted_dict[token_query[0]].copy()

    for token in token_query[1:]:
        
        uni_var |= inverted_dict[token]
      
    return uni_var
     

def tf_idf_funct(query):
    token_query = my_tokens(query)
    
    if not token_query:
        return 'Invalid input. Please type something.'
        
    total_docs = len(token_dict)
    doc_scores = {}
    
    # Get all documents containing at least one query term using union_function
    matched_docs = union_function(query)
    if isinstance(matched_docs, str):
        # Returns error string if no matches found
        return matched_docs    
     
    # Calculate final aggregated score for each document
    for doc in matched_docs:
        tokens = token_dict[doc]
        doc_length = len(tokens)
        final_doc_score = 0.0
        
        for term in token_query:
            if doc_length > 0:
                # Normalized Term Frequency (count / total words in document)
                tf = tokens.count(term) / doc_length

            else:
                tf = 0.0
                
            if tf > 0 and term in inverted_dict:
                doc_count = len(inverted_dict[term])
                idf = math.log(total_docs / doc_count)
                
                # Accumulate the (TF * IDF) score for this term into the document's total score
                final_doc_score += tf * idf
                
        # Store the final aggregated score for the document
        doc_scores[doc] = final_doc_score

    # Sort documents by their score in descending order
    # sorted() returns a list of tuples
    sorted_doc_scores = sorted(doc_scores.items(), key = lambda x: x[1], reverse = True)
                
    return sorted_doc_scores[:5]
    
def run_search():
    while True:

        # Ask user for input 
        query = input('Search for a document: Type \':quit\' when finished. ')
        
        # Breaks out of the loop
        if query == ':quit':
            break

        # Test performance in ms   
        start = time.perf_counter()
        results = tf_idf_funct(query)
        end = time.perf_counter()
        search_time = (end - start) * 1000

        print(f"\nSearch results for: {query} (Latency: {search_time} ms)\n")

        # Version A: Boolean retrieval
        # ''' set_slice = set(itertools.islice(results, 0, 5))
        # print(set_slice) '''

        if isinstance(results, str):
            print(results)
        
        else:
            for rank, (doc, score) in enumerate(results, start=1):
                print(f"{rank}. {doc:<15} Score: {score:.5f}")

if __name__ == "__main__":
    run_search()


  





