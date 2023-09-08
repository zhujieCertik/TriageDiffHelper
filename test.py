import os;
import json;
import string;

# prepare set from input file
def prepareSet(inputFile):
    pidList = set()
    for line in open(inputFile):
        # print(line)
        jsonData = json.loads(line)
        # print(jsonData['Message'])
        msg = jsonData['Message']
        if msg.count("/efs/data/projects/"):
            # print(msg)
            list = msg.split("/efs/data/projects/")
            # print(list[1])
            # b52273d0-6c20-11ec-b59f-7dd4a7e83b0c/9b02844c20bdeec5d69dab1592570309138a949b/contracts/ERC1155Modular.sol:104
            tmp = list[1]
            tmpList = tmp.split("/")
            projectId = tmpList[0]
            # print(projectId)  # b52273d0-6c20-11ec-b59f-7dd4a7e83b0c
            pidList.add(projectId)
    print("len of "+ inputFile.split('.')[0] +" == " + str(len(pidList)))
    # print(pidList)
    return pidList


# filter and prepare output file
def prepareOutput(input_filename, output_filename, filter_set):
    # create file
    if os.path.exists(output_filename):
        os.remove(output_filename)
    out = open(output_filename, 'w')
    # filter and write file
    for line in open(input_filename):
        # print(line)
        jsonData = json.loads(line)
        # print(jsonData['Message'])
        msg = jsonData['Message']
        if msg.count("/efs/data/projects/"):
            # print(msg)
            list = msg.split("/efs/data/projects/")
            # print(list[1])
            # b52273d0-6c20-11ec-b59f-7dd4a7e83b0c/9b02844c20bdeec5d69dab1592570309138a949b/contracts/ERC1155Modular.sol:104
            tmp = list[1]
            tmpList = tmp.split("/")
            projectId = tmpList[0]
            # print(projectId)  # b52273d0-6c20-11ec-b59f-7dd4a7e83b0c
            if projectId in filter_set:
                out.writelines(list[1])
                out.writelines('\n')
    # close file
    out.close()



if __name__== '__main__':
    # config
    print("A is result of pre rule, B is result of current rule")
    filenameA = "a.txt"
    filenameB = "b.txt"
    outfilenameA = "outA.txt"
    outfilenameB = "outB.txt"

    # prepare set A
    pidListA = prepareSet(filenameA)
    # prepare set B
    pidListB = prepareSet(filenameB)

    # cal a-b
    in_a_not_in_b = pidListA - pidListB
    # print(in_a_not_in_b)
    print("len in_a_not_in_b == " + str(len(in_a_not_in_b)))

    # cal b-a
    in_b_not_in_a = pidListB - pidListA
    # print(in_b_not_in_a)
    print("len in_b_not_in_a == " + str(len(in_b_not_in_a)))

    # cal a & b
    both_have = pidListB & pidListA
    # print(both_have)
    print("len both_have == " + str(len(both_have)))

    # output a-b
    prepareOutput(filenameA, outfilenameA, in_a_not_in_b)

    # output b-a
    prepareOutput(filenameB, outfilenameB, in_b_not_in_a)

