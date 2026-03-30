def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here   for loop for words in sentences  -> count = set()  -> if word in sentence: count++
    wdict= {}
    count=0
    for sen in sentences:
        for word in sen:
            if word not in wdict:
                wdict[word] = 0
            wdict[word] += 1
            
    return wdict
            
        
    