raw_data = [
    "introduction to biology, 45.99, 12, yes,"
    "calculus made easy , 29.50 ,0, no"
    "the great gatsby, 12.00 , 5, YES",
    "organic chemistry , 89.99,3,No",
    "world history vol 1, 33.2,-2,no"
  ]
book =raw_data[0]
print(book)

parts = book.split(",")
print(parts)

title = parts[0].strip()
print(title)

price = parts[1].strip()
print(price)