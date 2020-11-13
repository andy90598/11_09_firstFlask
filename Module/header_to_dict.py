def headerFormat(header):
    results = header.split("\n")
    headers={}
    for result in results:
        splitResult = result.split(": ")
        if len(splitResult[0])>1:
            headers[splitResult[0]] =splitResult[1]
    return headers