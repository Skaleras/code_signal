def solution(inputArray):
    products = []
    for i in range(len(inputArray)-1):
        product_i = inputArray[i] * inputArray[i+1]
        products.append(product_i)
    max(products)