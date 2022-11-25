def logger(primer, result):
    with open('logger.txt', 'a') as data:
        rasp_primer = ''.join(map(str, primer))
        rasp_primer = rasp_primer + '='
        result = str(result) + ';\n'
        data.write(rasp_primer)
        data.write(result)
