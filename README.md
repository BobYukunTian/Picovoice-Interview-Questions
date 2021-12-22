# Picovoice Interview Questions 
### Solution by Bob Tian
## Q1 [C, Python] 

Assume we have a function get_book_info(isbn) that takes a string ISBN argument and retrieves an object containing the Title, Author, and Language of a book (each represented as a string) that takes a nontrivial amount of time to run (perhaps because it’s making a call to a database). Write a wrapper function that increases performance by keeping results in memory for the quick lookup. To prevent memory from growing unbounded, we only want to store a maximum of N book records. At any given time, we should be storing the N books that we accessed most recently. Assume that N can be a large number when choosing data structure(s) and algorithm(s). 

## Q2 [JavaScript, TypeScript] 

Implement a 5-star widget for an eCommerce site for users to record a product rating. The widget displays a horizontal row of stars that are either outlined or black according to the product rating, from left to right. E.g. ★★★☆☆ = rating of 3. Multiple 5-star widgets can be present on a single page. If a user has not rated a product, the widget will have 5 outlined stars (☆☆☆☆☆). Each product on the page has a UUID. Hovering over the Nth star will light up stars 1 to N with a grey colour (e.g. ★★★★☆). Clicking a star will record the rating by sending a request to a web server with enough information to record the product and the rating. After clicking, the widget will then display the rating the user submitted with black stars (e.g. ★★★★☆). Submitting the rating is handled without refreshing the page. NOTE: You do not need to implement the backend. 
