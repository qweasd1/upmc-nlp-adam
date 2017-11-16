
def parse_from_adam(input_file_path,result):

    with open(input_file_path) as file:
        for line in file:
            line = line.strip().split("\t")
            abbr = line[0]
            long = line[2].split("|")[0].split(":")[0]
            freq = int(line[4])

            if abbr not in result:
                result[abbr] = {}
            longs = result[abbr]

            if long not in longs:
                longs[long] = freq
            else:
                longs[long] += freq



# result = {}
#
# parse_from_adam("adam_database.txt",result)
