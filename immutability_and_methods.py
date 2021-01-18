#String are immutable in Python. Which means, if we want to change the string, we must save it to a new variable. Or use the same variable and save it to our alteration.

quote = 'to be or not to be'

#length method
print(len(quote))

#upper method
print(quote.upper())

#capitalize method
print(quote.capitalize())

#find method
print(quote.find('be'))

#replace method
print(quote.replace('be', 'me'))

quote = quote.upper()
