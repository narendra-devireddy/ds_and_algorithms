def arrayOfProducts(array):
    # Write your code here.
    product_array = [1]*len(array)
	
	left_product = 1
	for i in range(len(array)):
		product_array[i]=left_product
		left_product*=array[i]
	
	right_product = 1
	for i in reversed(range(len(array))):
		product_array[i]*=right_product
		right_product*=array[i]
	return product_array