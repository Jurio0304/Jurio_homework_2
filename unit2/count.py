def count_CharAndWord(file):
    import os.path
    if os.path.isfile(file):
        with open(file, 'r') as f:
            word_count = 0
            character_count = 0
            for line in f:
                word = line.split()
                word_count += len(word)
                character_count += len(line)
        print('word number:', word_count)
        print('character number:',character_count)

count_CharAndWord('unit2/readme.md')