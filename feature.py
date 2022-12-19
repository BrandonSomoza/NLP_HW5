import sys
# checks if the token at index i in token_list is the first word
def check_first_word(i, token_list):
    if i < 1:
        return False
    line = token_list[i - 1].strip()
    if len(line) == 0:
        return True
    return False

# checks if the token at index i in token_list is the last word
def check_last_word(i,token_list):
    if i > len(token_list) - 2:
        return False
    line = token_list[i + 1].strip()
    if len(line) == 0:
        return True
    return False

# gets the previous word 
def get_prev_word(i, token_list):
    if check_first_word(i, token_list):
        return '<s>'
    elif i < 1:
        return '<s>'
    else:
        return token_list[i - 1].strip().split()[0]

# gets the previous pos
def get_prev_pos(i, token_list):
    if check_first_word(i, token_list):
        return '<s>'
    elif i < 1:
        return '<s>'
    else:
        return token_list[i - 1].strip().split()[1]

# gets the next word
def get_next_word(i, token_list):
    if check_last_word(i, token_list):
        return '</s>'
    elif i > len(token_list) - 2:
        return '</s>'
    else:
        return tokens[i + 1].strip().split()[0]

# gets the next pos
def get_next_pos(i, token_list):
    if check_last_word(i, token_list):
        return '</s>'
    elif i > len(token_list) - 2:
        return '</s>'
    else:
        return token_list[i + 1].strip().split()[1]

# checks if the word at index i of token_list is capital or not
def check_cap_word(i, token_list):
    word = token_list[i].strip().split()[0]
    if word[0].isupper():
        return '1'
    else:
        return '0'

# checks if the previous word is capital or not
def check_prev_cap_word(i, token_list):
    if check_first_word(i, token_list):
        return '0'
    if i < 1:
        return '0'
    else:
        word = token_list[i - 1].strip().split()[0]
        if word[0].isupper():  
            return '1'
        else:
            return '0'

# checks if the next word is capital or not
def check_next_cap_word(i, token_list):
    if check_last_word(i, token_list):
        return '0'
    elif i > len(token_list) - 2:
        return '0'
    else:
        word = token_list[i + 1].strip().split()[0]
        if word[0].isupper():
            return '1'
        else:
            return '0'


# open training file (second argument in commandline) and writes out the output to training.feature as per the instructions
with open(sys.argv[1] ,'r') as read_file:
    with open('training.feature', 'w') as write_file:
        tokens = read_file.readlines()
        for i, line in enumerate(tokens):
            line = line.strip()
            if len(line) == 0:
                write_file.write('\n')
            else:
                cur_word, cur_pos, cur_bio = line.split()
                cur_cap    = 'cur_cap='   + check_cap_word(i, tokens)

                prev_word  = 'prev_word=' + get_prev_word(i, tokens)
                prev_pos   = 'prev_pos='  + get_prev_pos(i, tokens)
                prev_cap   = 'prev_cap='  + check_prev_cap_word(i, tokens)

                next_word  = 'next_word=' + get_next_word(i, tokens)
                next_pos   = 'next_pos='  + get_next_pos(i, tokens)
                next_cap   = 'next_cap='  + check_next_cap_word(i, tokens)

                pp_word = 'pp_word=' + get_prev_word(i - 1, tokens)
                pp_pos  = 'pp_pos='  + get_prev_pos(i - 1, tokens)
                pp_cap  = 'pp_cap='  + check_prev_cap_word(i - 1, tokens)

                nn_word = 'nn_word=' + get_next_word(i + 1, tokens)
                nn_pos  = 'nn_pos='  + get_next_pos(i + 1, tokens)
                nn_cap  = 'nn_cap='  + check_next_cap_word(i + 1, tokens)

                line = '\t'.join([cur_word, cur_pos, cur_cap, prev_word, \
                                  prev_pos, prev_cap, next_word, next_pos, \
                                  next_cap, pp_word, pp_pos, pp_cap, nn_word,\
                                  nn_pos, nn_cap, cur_bio])
                write_file.write(line + '\n')

# open test file (third argument in commandline) and writes out the output to test.feature as per the instructions
with open(sys.argv[2], 'r') as read_file:
    with open('test.feature', 'w') as write_file:
        tokens = read_file.readlines()
        for i, line in enumerate(tokens):
            line = line.strip()
            if len(line) == 0:
                write_file.write('\n')
            else:
                cur_word, cur_pos = line.split()
                cur_bio   = 'cur_bio=##'
                cur_cap   = 'cur_cap='     + check_cap_word(i, tokens)

                next_word = 'next_word='   + get_next_word(i, tokens)
                next_pos  = 'next_pos='    + get_next_pos(i, tokens)
                prev_word = 'prev_word='   + get_prev_word(i, tokens)
                prev_pos  = 'prev_pos='    + get_prev_pos(i, tokens)
                prev_cap  = 'prev_cap='    + check_prev_cap_word(i, tokens)
                next_cap  = 'next_cap='    + check_next_cap_word(i, tokens)

                pp_word = 'pp_word=' + get_prev_word(i - 1, tokens)
                pp_pos  = 'pp_pos='  + get_prev_pos(i - 1, tokens)
                pp_cap  = 'pp_cap='  + check_prev_cap_word(i - 1, tokens)

                nn_word = 'nn_word=' + get_next_word(i + 1, tokens)
                nn_pos  = 'nn_pos='  + get_next_pos(i + 1, tokens)
                nn_cap  = 'nn_cap='  + check_next_cap_word(i + 1, tokens)

                line = '\t'.join([cur_word, cur_pos, cur_cap, prev_word, \
                                  prev_pos, prev_cap, next_word, next_pos, \
                                  next_cap, pp_word, pp_pos, pp_cap, nn_word,\
                                  nn_pos, nn_cap, cur_bio])
                write_file.write(line + '\n')
